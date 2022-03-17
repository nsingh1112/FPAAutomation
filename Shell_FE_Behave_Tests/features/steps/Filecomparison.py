from behave import *

from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.ShellHubFunctions import ShellHubFunctions
from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities
from Shell_FE_Selenium_Core.Utilities.FileComparisonUtilities import FileComparisonUtilities
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.ShellHubControls import ShellHubControls


@When('user compare the shell logo')
def step_impl(context):
    context.shellhub_functions = ShellHubFunctions()
    context.shellhub_functions.access_shell_hub()
    logo_img = ShellHubControls.logo_img
    result = FileComparisonUtilities().compare_image(localimage = 'logo.svg', remoteimage = logo_img, svg=True)
    AssertionUtilities.assert_if_true(result)

@When('user compare the url "{url}" page')
def step_impl(context, url ):
    context.shellhub_functions = ShellHubFunctions()
    context.shellhub_functions.navigate_to_url(url)
    result = FileComparisonUtilities().compare_screenshot(local_image = 'hugohomepage.png')
    AssertionUtilities.assert_if_true(result)

