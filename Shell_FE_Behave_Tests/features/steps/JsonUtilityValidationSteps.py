from behave import Given, When, Then
from Shell_FE_Requests_Core.Utilities.JsonCompareUtilities import JsonCompareUtils
import Shell_FE_Requests_Core.Utilities.JsonCompareUtilities
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Requests_Core.Utilities.AssertionUtilities import AssertionUtilities


@Then(u'user compare json response with expected data')
def step_impl(context):
    compare = JsonCompareUtils.response_isequal(RequestsBase.response, RequestsBase.response)
    AssertionUtilities.assert_if_true(compare)


@Then(u'user search value in response with key')
def step_impl(context):
    value = JsonCompareUtils.search_values_in_response_with_key(RequestsBase.response, "name")
    print(value[0])


@Then(u'user checks values presence in the response text')
def step_impl(context):
    check = JsonCompareUtils.is_value_present_in_res("Sanya Patel", RequestsBase.response)
    AssertionUtilities.assert_if_true(check)


@Then(u'user gets the specific node value')
def step_impl(context):
    node_value = JsonCompareUtils.get_node_value(RequestsBase.response, "0.name")
    AssertionUtilities.assert_equals(node_value, "Sanya Patel")


@Then(u'user finds the difference between json responses')
def step_impl(context):
    JsonCompareUtils.deep_difference(RequestsBase.response, RequestsBase.response)
