"""
A controller module containing the business logic for any 'hello' endpoints.
"""
import logging
import scrooge_mcbot.clients as clients
import scrooge_mcbot.models as models

LOGGER = logging.getLogger()


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
        logging.info(policy)
        current_billable = int(policy['billing_amount'])

        # Get module
        module = policy['module']

        # Get new quote for device
        quotes = clients.root_insurance.get_gadget_quote(module)

        # Compare premia and store if net saving
        for quote in quotes:
            if quote['package_name'] != policy['package_name']:
                continue
            if quote['base_premium'] < current_billable:
                potential_savings += current_billable - quote['base_premium']
                potential_quotes.append(quote['quote_package_id'])

    response = 'We can save you R{}!'.format(potential_savings / 100)
    return response, response
