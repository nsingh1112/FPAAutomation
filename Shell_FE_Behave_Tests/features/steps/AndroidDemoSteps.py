import sys
import time

from behave import *
from Shell_FE_Appium_Core.AppiumBase import AppiumBase

#AppiumBase.read_config()
#AppiumBase.read_values()
#driver = AppiumBase.launch_app()


@given('I have launched the apidemos app')
def open_views(context):
    element = context.driver.find_element_by_accessibility_id('Views')

    element.click()
    time.sleep(2)


@when('I test views')
def open_views(context):
    # AppiumBase.click_by_accessibility_id(driver,'Controls')
    element = context.driver.find_element_by_accessibility_id('Controls')
    element.click()


@then('I verify checkbox and radio buttons')
def verify_check_box(context):
   element = context.driver.find_element_by_accessibility_id('1. Light Theme')
   element.click()
   check_box = context.driver.find_element_by_accessibility_id('Checkbox 1')
   check_box.click()



