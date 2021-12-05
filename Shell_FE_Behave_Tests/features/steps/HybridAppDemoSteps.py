import time

from behave import *
from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionLibrary.ChromeAppDemoFunctions import HybridAppFunctions


@given('I launched the mobile native chrome app')
def pre_AppConfig(context):
    context.feature.hybridApp_Demo = HybridAppFunctions()
    context.feature.hybridApp_Demo.open_Chrome()




@when('I am clicking on search and pass values to search')
def search_Box(context):
    context.feature.hybridApp_Demo.click_search_Box()




@then('I Search for the text')
def searching_text(context):
    context.feature.hybridApp_Demo.send_Value("Python Automation Testing")



@when('I test the web_view')
def switching_view(context):
    #list_of_appView = context.hybridApp_Demo.get_AppCotext()
    print("APPview :", context.feature.hybridApp_Demo.get_AppViews())
    context.feature.hybridApp_Demo.switching_View("WEBVIEW_chrome")
    print("APPview after switch:", context.feature.hybridApp_Demo.get_AppViews())


@then('I replace the search text')
def replace_text(context):
    # context.feature.hybridApp_Demo.remove_text()
    # time.sleep(10)
    context.feature.hybridApp_Demo.replace_value("Appium python Testing")
    time.sleep(10)



