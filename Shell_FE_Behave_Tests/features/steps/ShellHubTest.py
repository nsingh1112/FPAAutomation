from behave import *

from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.ShellHubFunctions import ShellHubFunctions
from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities


@Given('user navigates to the Shell hub site')
def step_impl(context):
    context.shellhub_functions = ShellHubFunctions()
    context.shellhub_functions.access_shell_hub()


@Then('user verifies that "{url}" is displayed')
def step_impl(context, url):
    actual_url = context.shellhub_functions.validate_url_equality(url)
    AssertionUtilities.assert_equals(url, actual_url)


@When('user searches for keyword "{keyword}" from search-box')
def step_impl(context, keyword):
    context.shellhub_functions.search_value(keyword)


@Then('user validates the title of the window "{title}"')
def step_impl(context, title):
    actual_title = context.shellhub_functions.validate_title_equality(title)
    AssertionUtilities.assert_equals(title, actual_title)


@When('user navigates back to "{url}"')
def step_impl(context, url):
    context.shellhub_functions.navigate_back_to_shell_hub(url)


@When('user clicks on Yammer link')
def step_impl(context):
    context.shellhub_functions.click_yammer()


@Then('user verifies if totally "{value}" windows are displayed')
def step_impl(context, value):
    actual_value = context.shellhub_functions.get_window_count(value)
    AssertionUtilities.assert_equals(int(actual_value), int(value))


@When('user navigates to the child window using title "{title}"')
def step_impl(context, title):
    context.shellhub_functions.switch_to_Yammer(title)


@When('user closes the child window')
def step_impl(context):
    context.shellhub_functions.close_Yammer()


@When('user logs out of the application')
def step_impl(context):
    context.shellhub_functions.log_out()


@Then('user validates the Select account screen')
def step_impl(context):
    select_account_displayed = context.shellhub_functions.check_select_account()
    AssertionUtilities.assert_if_true(select_account_displayed)
