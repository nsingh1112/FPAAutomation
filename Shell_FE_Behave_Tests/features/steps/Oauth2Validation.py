from behave import Given, When, Then
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.AssertionUtilities import AssertionUtilities

@When(u'user sends a POST request to retrieve details')
def step_impl(context):
    """
    User needs to provide mandatory details to retrieve access token and then use access token to raise another request
    token_url = Url from which toke  needs to be retrieved
    client_id = consumer key of your connected app
    username = your login username for org
    password =  your org login password
    client_secret = consumer secret of your connected app
    test_url = instance URL you need to make a request
    :param context:
    :return:
    """
    client_id = ""
    client_secret = ""
    token_url = ""
    test_url = ""
    username = ""
    password = ""

    data =  {'grant_type': 'password','username': username, 'password': password, 'client_id': client_id, 'client_secret': client_secret}
    access_token = RequestsBase.get_access_token(url= token_url, data=data)
    if access_token.status_code == 200:
        access_token = access_token.json()["access_token"]
        api_call_headers = {'Authorization': 'Bearer ' + access_token}
        RequestsBase.get_request(url=test_url, headers=api_call_headers)
        AssertionUtilities.assert_equals('200', str(RequestsBase.response_status_code()))
    else:
        AssertionUtilities.assert_if_true(access_token)



