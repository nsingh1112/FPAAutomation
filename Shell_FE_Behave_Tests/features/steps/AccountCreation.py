from behave import Given, When, Then

from Shell_FE_Behave_Tests.ApiApplicationLibrary.FunctionalLibrary.AccountApi import AccountApi
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.AssertionUtilities import AssertionUtilities
from Shell_FE_Requests_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Behave_Tests.ApiApplicationLibrary.FunctionalLibrary.Oauth2 import Oauth2
from Shell_FE_Requests_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Requests_Core.Utilities.JsonComparisonUtilities import JsonComparisonUtils


@Given(u'user logs into Salesforce application as "{role}" role')
def step_impl(context, role):
    context.feature.oauth2 = Oauth2()
    context.access_token = context.feature.oauth2.get_access_token(role)
    AssertionUtilities.assert_equals('200', str(RequestsBase.response_status_code()))
    access_token = context.access_token.json()["access_token"]
    value_dict = dict(access_token=access_token)
    FileUtilities.write_into_json(value_dict, "AccountCreation/AccessToken.json")


@When("user creates the account")
def step_impl(context):
    context.feature.account = AccountApi()
    context.feature.account.create_account()
    AssertionUtilities.assert_equals("201", str(RequestsBase.response_status_code()))


@When(u'user fetches the account ID')
def step_impl(context):
    id_value = JsonComparisonUtils.search_values_in_response_with_key(RequestsBase.response, 'id')
    dict_a = dict(id=id_value[0])
    FileUtilities.write_into_json(dict_a, "account_id.json")




