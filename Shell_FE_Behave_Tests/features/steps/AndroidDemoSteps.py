import sys
import time

from behave import *
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtlities
from Shell_FE_Appium_Core.Utilities.AssertUtilities import AssertUtilities

AppiumBase.read_config()
AppiumBase.read_values()
driver = AppiumBase.launch_app()
wait_utilities = WaitUtilities(driver)
android_utilities = AndroidUtlities(driver)
assert_utilities = AssertUtilities(driver)


@given('I have launched the apidemos app')
def open_views(context):
    wait_utilities.wait_for_element('accessibility_id', 'Views')
    android_utilities.take_Screenshot("screenshot1")
    text = android_utilities.get_text('Views')
    newList = ['test', 'game','Views']
    assert_utilities.assertEquals(text,'Views')
    assert_utilities.assertValueInList(text,newList)
    android_utilities.click('accessibility_id', 'Views')
    #wait_utilities.wait_for_element('text', 'Controls')


@when('I test views')
def open_views(context):
    android_utilities.isDisplayed('text', 'Controls')
    android_utilities.click('accessibility_id', 'Controls')
    wait_utilities.implicit_wait(10)


@then('I verify checkbox and radio buttons')
def verify_check_box(context):
    android_utilities.click('accessibility_id', '1. Light Theme')
    wait_utilities.wait_for_element('text', 'Checkbox 1')
    android_utilities.click('accessibility_id', 'Checkbox 1')


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
