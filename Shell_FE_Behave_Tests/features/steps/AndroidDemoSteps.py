from behave import *
from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionLibrary.ApiDemoAppFunctions import ShellApiDemos


@given('I have launched the apidemos app')
def open_views(context):
    context.feature.api_Demos_functions = ShellApiDemos()
    context.feature.api_Demos_functions.click_views()


@when('I test views')
def open_controls(context):
    context.feature.api_Demos_functions.click_controls()


@then('I verify checkbox and radio buttons')
def verify_check_box(context):
    context.feature.api_Demos_functions.click_checkbox()


@when('I Click on Views')
def verify_back_btn(context):
    context.feature.api_Demos_functions.check_back_button()


@then('I verify popups')
def check_scroll_function(context):
    #context.feature.api_Demos_functions.check_drag_and_drop()
    context.feature.api_Demos_functions.check_scroll()
    context.feature.api_Demos_functions.check_tap()


@when('I Click on Expandable Lists')
def check_tap_function(context):
    pass



@then('I Verify all lists')
def step_impl(context):
    pass


@then('I verify DragAndDrop')
def step_impl(context):
    pass


@when('I Click on App')
def step_impl(context):
    pass


@then('I verify alerts')
def step_impl(context):
    pass


@when('I click on Date')
def step_impl(context):
    pass


@then(u'I select Date')
def step_impl(context):
    pass


@when(u'I Click on Gallery')
def step_impl(context):
    pass


@then(u'I Select Picture')
def step_impl(context):
    pass
