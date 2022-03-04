from behave import *
from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionalLibrary.ApiDemoAppFunctions import ShellApiDemos


@given('I have launched the apidemos app')
def open_views(context):
    context.api_Demos_functions = ShellApiDemos()
    context.api_Demos_functions.click_views()


@when('I test views')
def open_controls(context):
    context.api_Demos_functions.click_controls()


@then('I verify checkbox and radio buttons')
def verify_check_box(context):
    context.api_Demos_functions.click_checkbox()


@when('I Click on Views')
def verify_back_btn(context):
    context.api_Demos_functions.check_back_button()


@then('I verify popups')
def check_scroll_function(context):
    #context.feature.api_Demos_functions.check_drag_and_drop()
    context.api_Demos_functions.check_scroll()
    context.api_Demos_functions.check_tap()

