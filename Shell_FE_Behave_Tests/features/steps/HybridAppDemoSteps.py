import time

from behave import *

# AppiumBase.read_config()
# AppiumBase.read_values()
# AppiumBase.startAppiumServer()
# AppiumBase.stopAppiumServer()
# driver = AppiumBase.launch_app()
# wait_utilities = WaitUtilities(driver)
# android_utilities = AndroidUtlities(driver)
# assert_utilities = AssertUtilities(driver)
from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionLibrary.ChromeAppDemoFunctions import HybridAppFunctions


@given('I launched the mobile native chrome app')
def pre_AppConfig(context):
    context.feature.hybridApp_Demo = HybridAppFunctions()
    context.feature.hybridApp_Demo.open_Chrome()

    # android_utilities.click("id","com.android.chrome:id/terms_accept")
    # wait_utilities.wait_for_element("id","com.android.chrome:id/next_button")
    # android_utilities.click("id","com.android.chrome:id/next_button")
    # wait_utilities.wait_for_element("id","com.android.chrome:id/positive_button")
    # android_utilities.click("id","com.android.chrome:id/positive_button")
    # wait_utilities.wait_for_element("id","com.android.chrome:id/search_box_text")


@when('I am clicking on search and pass values to search')
def search_Box(context):
    context.feature.hybridApp_Demo.click_search_Box()

    # print("Current context :" ,android_utilities.get_AppContext())
    # android_utilities.send_keys("id","com.android.chrome:id/search_box_text","Python Automation Testing")
    # android_utilities.press_KeyCode(66)
    # time.sleep(5)
    # print("Current context :", android_utilities.get_AppContext())
    # android_utilities.switch_Context("WEBVIEW_chrome")
    # android_utilities.click("xpath","//span[contains(text(),'Images')]")
    # time.sleep(5)


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



