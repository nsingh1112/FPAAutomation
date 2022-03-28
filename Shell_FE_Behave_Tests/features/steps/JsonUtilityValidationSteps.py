from behave import Given, When, Then

from Shell_FE_Behave_Tests.ApiApplicationLibrary.FunctionalLibrary.JsonComparisionData import JsonComparison
from Shell_FE_Requests_Core.Utilities.JsonComparisonUtilities import JsonComparisonUtils
import Shell_FE_Requests_Core.Utilities.JsonComparisonUtilities
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Requests_Core.Utilities.AssertionUtilities import AssertionUtilities
from Shell_FE_Behave_Tests.ApiApplicationLibrary.FunctionalLibrary import JsonComparisionData


@Then(u'user compare json response with expected data')
def step_impl(context):
    context.feature.jsoncomparison = JsonComparison()
    compare = JsonComparisonUtils.response_isequal(RequestsBase.response, RequestsBase.response)
    AssertionUtilities.assert_if_true(compare)


@Then(u'user search value in response with key "{name}"')
def step_impl(context, name):
    value = JsonComparisonUtils.search_values_in_response_with_key(RequestsBase.response, name)
    print(value[0])


@Then(u'user checks values presence in the response text')
def step_impl(context):
    expected_value = context.feature.jsoncomparison.get_expected_text()
    check = JsonComparisonUtils.is_value_present_in_res(expected_value, RequestsBase.response)
    AssertionUtilities.assert_if_true(check)


@Then(u'user gets the node "{node_data}" value')
def step_impl(context, node_data):
    node_value = JsonComparisonUtils.get_node_value(RequestsBase.response, node_data)
    AssertionUtilities.assert_equals(node_value, context.feature.jsoncomparison.get_expected_node_value())


@Then(u'user finds the difference between json responses')
def step_impl(context):
    JsonComparisonUtils.deep_difference(RequestsBase.response, RequestsBase.response)


@Then(u'user check for the response time should not be greater than threshold')
def step_impl(context):
    timer = RequestsBase.get_response_time()
    expected_threshold = context.feature.jsoncomparison.get_threshold_value()
    AssertionUtilities.assert_less_or_equals(timer, expected_threshold)


