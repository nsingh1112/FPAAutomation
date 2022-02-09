import time

from behave import *
from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionLibrary.iOSDemoAppFunctions import IOSDemoFunction
from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionLibrary.WebBrowserFunctions import BrowserFunctions


@given('I have launched the UI Catalog App')
def launch_application(context):
    context.feature.iOS_Demos_functions = IOSDemoFunction()
    context.feature.iOS_Browser = BrowserFunctions()


@when('I test Alert Views')
def checking_alert(context):
    context.feature.iOS_Demos_functions.open_alert()
    context.feature.iOS_Demos_functions.simple_alert()
    context.feature.iOS_Demos_functions.okay_cancel_alert()
    context.feature.iOS_Demos_functions.multiple_choice_alert()
    context.feature.iOS_Demos_functions.text_entry_alert()
    context.feature.iOS_Demos_functions.confirm_cancel_alert()
    context.feature.iOS_Demos_functions.home_page()
    context.feature.iOS_Demos_functions.check_orientation()
    context.feature.iOS_Demos_functions.check_background_app()
    # context.feature.iOS_Demos_functions.activate_my_app()
    # context.feature.iOS_Demos_functions.check_background_app()
    # context.feature.iOS_Demos_functions.re_launch_app()


@when('I do parallel App testing')
def step_impl(context):
    # context.feature.iOS_Browser.check_background()
    # context.feature.iOS_Browser.launch_web()
    # context.feature.iOS_Browser.get_context()
    # context.feature.iOS_Browser.verify_title()  click_username , pass_value ,
    pass
