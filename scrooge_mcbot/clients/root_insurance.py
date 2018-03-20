from root import insurance
import logging


def get_phone_brands():
    client = insurance.Client()
    return client.gadgets.list_phone_brands()


def get_policies(policyholder_id):
    client = insurance.Client()
    policyholder = client.policyholders.get(policyholder_id)
    return policyholder['policy_ids']


def get_policy(policy_id):
    client = insurance.Client()
    return client.policies.get(policy_id)


def get_gadget_quote(module_data):
    client = insurance.Client()
    if 'model' in module_data:
        module_data['model_name'] = module_data['model']
        del module_data['model']
    quote = insurance.Quotes(client)
    quote = quote.create(module_data)
    return quote


def cancel_policy(policy_id, reason):
    client = insurance.Client()
    client.policies.cancel(policy_id, reason)


def create_application(policyholder_id, quote_id, amount, serial_number):
    client = insurance.Client()
    return client.applications.create(policyholder_id, quote_id, amount, serial_number)


def issue_policy(application_id):
    client = insurance.Client()
    return client.policies.issue(application_id)
