from behave import Given, When, Then
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.AssertionUtilities import AssertionUtilities
from Shell_FE_Behave_Tests.ApiApplicationLibrary.FunctionalLibrary.UsersApi import UsersApi

@When(u'user sends a POST request to retrieve access token')
def step_impl(context):
    context.feature.users_api = UsersApi()
    context.access_token = context.feature.users_api.get_access_token()

@Then(u'user validates if the response status is {expected_code} ')
def step_impl(context, expected_code):
    AssertionUtilities.assert_equals(expected_code, str(RequestsBase.response_status_code()))

@Then(u'user sends a GET request to access details')
def step_impl(context):
    access_token = context.access_token.json()["access_token"]
    context.feature.users_api.oauth2_request(access_token)
    AssertionUtilities.assert_equals('200', str(RequestsBase.response_status_code()))

