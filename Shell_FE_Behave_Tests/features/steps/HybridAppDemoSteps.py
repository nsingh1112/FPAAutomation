import time

from behave import *
from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionLibrary.HybridAppDemoFunctions import HybridAppFunctions


@given('I launched the mobile native chrome app')
def pre_AppConfig(context):
    context.feature.hybridApp_demo = HybridAppFunctions()
    context.feature.hybridApp_demo.open_chrome()


@when('I am clicking on search and pass values to search')
def search_Box(context):
    context.feature.hybridApp_demo.click_search_box()


@then('I Search for the text')
def searching_text(context):
    context.feature.hybridApp_demo.send_value("Python Automation Testing")


@when('I test the web_view')
def switching_view(context):
    # list_of_appView = context.hybridApp_Demo.get_AppCotext()
    print("APPview :", context.feature.hybridApp_demo.get_app_views())
    context.feature.hybridApp_demo.switching_view("WEBVIEW_chrome")
    print("APPview after switch:", context.feature.hybridApp_demo.get_app_views())


@then('I replace the search text')
def replace_text(context):
    # context.feature.hybridApp_demo.remove_text()
    # time.sleep(10)
    # context.feature.hybridApp_demo.replace_value("Appium python Testing")
    # time.sleep(10)
    context.feature.hybridApp_demo.switching_view("NATIVE_APP")
    context.feature.hybridApp_demo.click_search_url()
    context.feature.hybridApp_demo.send_value("New Test automation Tool")
