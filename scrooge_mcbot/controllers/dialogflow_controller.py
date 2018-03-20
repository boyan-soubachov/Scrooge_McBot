"""
A controller module containing the business logic for any 'hello' endpoints.
"""
import logging
import scrooge_mcbot.clients as clients
import scrooge_mcbot.models as models

LOGGER = logging.getLogger()


def _apply_savings(replacements):
    new_policies = []
    for repl in replacements:
        policy = repl['policy']
        quote = repl['quote']
        # Cancel old policy
        clients.root_insurance.cancel_policy(policy['policy_id'], 'Too damn expensive!')

        # Exercise new policy
        policyholder_id = policy['policyholder_id']
        app = clients.root_insurance.create_application(
            policyholder_id,
            quote['quote_package_id'],
            quote['base_premium'],
            policy['module']['serial_number'])
        LOGGER.info('app: %s', app)
        new_policy = clients.root_insurance.issue_policy(app['application_id'])
        new_policies.append(new_policy)
    return new_policies


def find_out_savings(id_number):
    potential_savings = 0.0
    potential_quotes = []
    # Get policyholder ID from id number
    policyholder_id = models.file_db.get_policyholder_id(id_number)
    if not policyholder_id:
        raise Exception('Could not find policy holder ID number')

    LOGGER.info('policyholder id: %s', policyholder_id)

    # Get current policies
    client_policies = clients.root_insurance.get_policies(policyholder_id)

    # For each policy in current policies
    for policy_id in client_policies:
        policy = clients.root_insurance.get_policy(policy_id)
        if policy['status'] in ('cancelled'):
            continue

        logging.info(policy)
        current_billable = int(policy['billing_amount'])

        # Get module
        module = policy['module']

        # Get new quote for device
        quotes = clients.root_insurance.get_gadget_quote(module)

        # Compare premia and store if net saving
        highest_saving = 0
        for quote in quotes:
            if quote['package_name'] != policy['package_name']:
                continue
            if quote['base_premium'] < current_billable:
                savings = current_billable - quote['base_premium']
                if savings > highest_saving:
                    highest_saving = savings
                    cheapest_quote = quote

        if highest_saving > 0:
            potential_savings += highest_saving
            potential_quotes.append({
                'policy': policy,
                'quote': cheapest_quote
            })

    if len(potential_quotes) > 0:
        _apply_savings(potential_quotes)

    response = 'We can save you R{}!'.format(potential_savings / 100)
    return response, response
