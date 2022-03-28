from behave import *
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.ShellHubFunctions import ShellHubFunctions
from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities


@Then('user validates the entire page for Accessibility')
def step_impl(context):
    context.shellhub_functions = ShellHubFunctions()
    no_of_violations = context.shellhub_functions.check_shell_hub_accessibility()
    assert no_of_violations == 0, "Accessibility tests failed due to violations present in the webpage."

