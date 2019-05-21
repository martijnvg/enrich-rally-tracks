def create_policy(es, params):
    es.transport.perform_request('PUT', '/_enrich/policy/' + params['policy-name'], body=params['body'])

def execute_policy(es, params):
    es.transport.perform_request('POST', '/_enrich/policy/' + params['policy-name'] + '/_execute')

def register(registry):
    registry.register_runner("create-policy", create_policy)
    registry.register_runner("execute-policy", execute_policy)