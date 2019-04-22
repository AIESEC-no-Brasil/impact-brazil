import json
from urllib.parse import urlparse, quote
import requests
from . import config, getkey
import boto3
import datetime
client = boto3.client('sqs')


# Special printing function
def _print_silent(string, silent=True, print_function=print):
    if not silent:
        print_function(string)


# Make a GraphQL Call
def gql_execute(url, query, variables=None):
    data = {'query': query,
            'variables': json.dumps({} if variables is None else variables)}

    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json'}

    req = requests.post(url, json=data, headers=headers)

    return req


# Generate a token
def generate_token(silent, print_function):
    # if config.api_key == '':
    if True:
        _print_silent("API key is blank, generating new key", silent, print_function)
        config.api_key = getkey.get_access_token(config.token_get_url)
        _print_silent("Generated key: " + config.api_key, silent, print_function)
        return True
    return False


# Run a GraphQL query against the GIS API
def gis_get(query, silent=True, print_function=print, custom_api_key=None, variables=None):
    if custom_api_key is None:
        generate_token(silent, print_function)

    url = config.expa_api_url.format(config.api_key if custom_api_key is None else custom_api_key)

    _print_silent("Running query: " + query.replace("\n", " ").replace("\r", ""), silent, print_function)

    try:
        if variables is not None:
            _print_silent("Variables: " + json.dumps(variables), silent, print_function)
            req = gql_execute(url, query, variables=variables)
        else:
            req = gql_execute(url, query)

    except Exception as e:
        raise Exception('There was an unexpected error: ' + str(e))

    if req.text == "":
        raise Exception('There was no output', req)

    if req.status_code not in (200, 201):
        raise Exception('There was an error running the query: ' + req.text, req)

    json_out = json.loads(req.text)

    # Did we error?
    if 'errors' in json_out:
        raise Exception('There was an error running the query: ' + req.text, req)

    # We have to return the 3rd level of the output
    # because the output is in the format of
    # data { allOpportunities { data ...
    # But of course this could not be true, so if there's an error just return json_out as is
    try:
        json_out = next(iter(next(iter(json_out.values())).values()))
    except Exception as e:
        pass
    finally:
        return json_out


# Shorthand for expa_get(...)['data']
def gis_get_data(query, silent=True, print_function=print, custom_api_key=None, variables=None):
    data = gis_get(query, silent, print_function, custom_api_key, variables)
    try:
        return data['data']
    except KeyError:
        raise Exception(json.dumps(data))


# Get paginated data
# Requirements:
# 1. Your GQL query must have paging { total_pages } and data {}
# 2. You must leave a space for a format string for pages: {}
def gis_get_paginated(query, silent=True, print_function=print, variables=None):
    # TODO: Add error handling
    if variables is None:
        variables_with_page = {'page': 1}
    else:
        variables_with_page = variables
        variables_with_page['page'] = 1

    _print_silent("Running GQL query: " + query, silent, print_function)
    _print_silent("Getting page 1", silent, print_function)

    qout = gis_get(query, variables=variables_with_page)

    total_pages = qout['paging']['total_pages']

    _print_silent(f"Total pages is {total_pages}", silent, print_function)

    qoutdata = qout['data']

    for i in range(2, total_pages + 1):
        _print_silent(f"Getting page {i} of {total_pages}", silent, print_function)

        variables_with_page['page'] = i
        qout_iter = gis_get(query, variables=variables_with_page)

        qoutdata = qoutdata + qout_iter['data']

    qout['data'] = qoutdata
    return qout


# Runs a Rest API call
def gis_get_rest(call, silent=True, print_function=print):
    generate_token(silent, print_function)

    # FIXME: we shouldn't just be doing .replace()
    url = config.expa_rest_api_url + call.replace('[', '%5B').replace(']', '%5D')
    url += ('&' if urlparse(url).query else '?') + 'access_token=' + config.api_key

    _print_silent("Running REST call: " + url, silent, print_function)
    r = requests.get(url)
    # TODO: Add error handling
    return r.json()


# Applies for an opportunity
# Returns: (bool success, json response)
def yop_apply_opportunity(api_key, opp_id, gip_answer=None, user_id=None):
    # First, we check profile completedness
    try:
        # Get current person ID
        if user_id is None:
            current_person = gis_get('{ currentPerson { id } }', custom_api_key=api_key, silent=False)
            current_person_id = current_person['id']
        else:
            current_person_id = user_id

        # Now get their details
        person_profile = gis_get('query getPerson($id: ID) { getPerson(id: $id) { academic_experiences { id },'
                                 'professional_experiences { id }, summary } }', variables={'id': current_person_id},
                                 custom_api_key=api_key, silent=False)

    except Exception as e:
        return False, json.dumps({'error': str(e)})

    # Now, ideally, GIS should check if other parameters are missing and error below
    # We need to check for academic_exp, professional_exp and summary
    if len(person_profile['academic_experiences']) == 0 or len(person_profile['professional_experiences']) == 0 or \
            len(person_profile['summary']) == 0:
        return False, json.dumps({'error': 'Incomplete profile', 'error_code': 'E_INCOMPLETE_PROFILE'})

    # Now submit the application and hope it worked!
    url = config.expa_rest_api_apply_url.format(api_key)
    request = requests.post(url, data={'application[opportunity_id]': opp_id, 'application[gt_answer]': gip_answer})

    response = client.send_message(
        QueueUrl='https://sqs.us-west-1.amazonaws.com/846501484982/temp',
        MessageBody=json.dumps({
            'personId': current_person_id,
            'operationId': opp_id,
            'date': str(datetime.datetime.now())
        })
    )

    return request.status_code == 201, request.json()
