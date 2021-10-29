import sys
import time

from behave import *
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtlities

AppiumBase.read_config()
AppiumBase.read_values()
driver = AppiumBase.launch_app()
wait_utilities = WaitUtilities(driver)
android_utilities = AndroidUtlities(driver)


@given('I have launched the apidemos app')
def open_views(context):
    wait_utilities.wait_for_element('text', 'Views')
    android_utilities.click('accessibility_id', 'Views')
    wait_utilities.wait_for_element('text', 'Controls')


@when('I test views')
def open_views(context):
    android_utilities.click('accessibility_id', 'Controls')
    wait_utilities.implicit_wait(10)
    # AppiumBase.click_by_accessibility_id('Controls')


@then('I verify checkbox and radio buttons')
def verify_check_box(context):
    android_utilities.click('accessibility_id', '1. Light Theme')
    android_utilities.click('accessibility_id', 'Checkbox 1')

    # AppiumBase.click_by_accessibility_id('1. Light Theme')
    # AppiumBase.click_by_accessibility_id('Checkbox 1')


# element = context.driver.find_element_by_accessibility_id('1. Light Theme')
# element.click()
# check_box = context.driver.find_element_by_accessibility_id('Checkbox 1')
# check_box.click()

@when('I Click on Views')
def step_impl(context):
    pass


@then('I verify popups')
def step_impl(context):
    pass


@when('I Click on Expandable Lists')
def step_impl(context):
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
