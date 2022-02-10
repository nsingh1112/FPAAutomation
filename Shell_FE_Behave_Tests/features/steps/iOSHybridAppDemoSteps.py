import time

from behave import *
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.iOSUtilities import IOSUtilities
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from appium.webdriver.common.mobileby import MobileBy

@given(u'I launched the mobile native Safari app')
def step_impl(context):
    # WaitUtilities.wait_for_element_to_be_clickable(AppiumBase.driver.find_element(MobileBy.IOS_CLASS_CHAIN,"**/XCUIElementTypeCell['name == 'com.apple.mobilesafari.framework-customization-sectionContent'']/XCUIElementTypeOther") )
    print(IOSUtilities.get_app_contexts())
    IOSUtilities.click_element(AppiumBase.driver.find_element(MobileBy.IOS_CLASS_CHAIN,"**/XCUIElementTypeCell[`name "
                                                                                       "== "
                                                                                       "'com.apple.mobilesafari"
                                                                                       ".framework-customization"
                                                                                       "-sectionContent"
                                                                                       "'`]/XCUIElementTypeOther"))
    time.sleep(10)



@when(u'I am testing the search functionality')
def step_impl(context):
    pass


@when(u'I test the swicth context')
def step_impl(context):
    pass


@then(u'I am testing the web_view after switching')
def step_impl(context):
    pass
