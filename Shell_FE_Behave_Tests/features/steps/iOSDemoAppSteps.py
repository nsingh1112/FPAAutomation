from behave import *
from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionLibrary.iOSDemoAppFunctions import IOSDemoFunction


@given('I have launched the UI Catalog App')
def launch_application(context):
    context.feature.iOS_Demos_functions = IOSDemoFunction()


@when('I test Alert Views')
def checking_alert(context):
    context.feature.iOS_Demos_functions.open_alert()
    context.feature.iOS_Demos_functions.simple_alert()
    context.feature.iOS_Demos_functions.okay_cancel_alert()
    context.feature.iOS_Demos_functions.multiple_choice_alert()
    context.feature.iOS_Demos_functions.text_entry_alert()
    context.feature.iOS_Demos_functions.confirm_cancel_alert()
    context.feature.iOS_Demos_functions.home_page()
