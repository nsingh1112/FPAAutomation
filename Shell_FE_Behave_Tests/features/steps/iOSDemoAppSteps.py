import time

from behave import *
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities
from Shell_FE_Appium_Core.Utilities.iOSUtilities import IOSUtilities


@given('I have launched the Integration App')
def step_impl(context):
    AndroidUtilities.take_screenshot("iOSTest")
    IOSUtilities.click_element(AppiumBase.driver.find_element_by_accessibility_id('Alerts'))
    IOSUtilities.send_text_to_element(AppiumBase.driver.find_element_by_accessibility_id('textField'),
                                      "This is my text")
    time.sleep(5)
    IOSUtilities.clear_text(AppiumBase.driver.find_element_by_accessibility_id('textField'))
    IOSUtilities.click_back_button()
    text = IOSUtilities.get_text(AppiumBase.driver.find_element_by_accessibility_id("Deadlock app"))
    attr = IOSUtilities.get_attribute(AppiumBase.driver.find_element_by_accessibility_id("Deadlock app"), "name")
    print("########## Get Text ##################### :", text)
    print("########## Get attr ##################### :", attr)
    IOSUtilities.tap_element(AppiumBase.driver.find_element_by_accessibility_id('Scrolling'))
    IOSUtilities.tap_element(AppiumBase.driver.find_element_by_accessibility_id('ScrollView'))
    time.sleep(2)
    IOSUtilities.scroll_to_text("50")
    # time.sleep(2)
    # IOSUtilities.scroll_up("1")
    time.sleep(5)
