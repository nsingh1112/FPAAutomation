import time

#from behave import *
#from Shell_FE_Appium_Core.AppiumBase import AppiumBase
#from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
#from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtlities
#from Shell_FE_Appium_Core.Utilities.AssertUtilities import AssertUtilities

#AppiumBase.read_config()
#AppiumBase.read_values()
#AppiumBase.startAppiumServer()
#AppiumBase.stopAppiumServer()
#driver = AppiumBase.launch_app()
#wait_utilities = WaitUtilities(driver)
#android_utilities = AndroidUtlities(driver)
#assert_utilities = AssertUtilities(driver)

#@given('I lauched the mobile native chrome app')
#def pre_AppConfig(context):
    #android_utilities.click("id","com.android.chrome:id/terms_accept")
    #wait_utilities.wait_for_element("id","com.android.chrome:id/next_button")
    #android_utilities.click("id","com.android.chrome:id/next_button")
    #wait_utilities.wait_for_element("id","com.android.chrome:id/positive_button")
    #android_utilities.click("id","com.android.chrome:id/positive_button")
    #wait_utilities.wait_for_element("id","com.android.chrome:id/search_box_text")

''''@when('I am clicking on search and pass values to search')
def search_Box(context):
    print("Current context :" ,android_utilities.get_AppContext())
    android_utilities.send_keys("id","com.android.chrome:id/search_box_text","Python Automation Testing")
    android_utilities.press_KeyCode(66)
    time.sleep(5)
    print("Current context :", android_utilities.get_AppContext())
    android_utilities.switch_Context("WEBVIEW_chrome")
    android_utilities.click("xpath","//span[contains(text(),'Images')]")
    time.sleep(5)



@then('I Search for the text')
def step_impl(context):
    pass

@when('I test the webview')
def step_impl(context):
    pass

@then('I click on the link')
def step_impl(context):
    pass'''
