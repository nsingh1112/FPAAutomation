import time

from behave import *
import SharedVariables
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.TutorialsPointFunctions import TutorialsPointFunctions
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities


@Given('user navigates to the TutorialsPoint site')
def step_impl(context):
    print("TITLE BEFORE ASSIGNING: " + SharedVariables.expected_title)
    print("URL BEFORE ASSIGNING: " + SharedVariables.expected_url)
    context.tutorialFunctions = TutorialsPointFunctions()
    context.tutorialFunctions.access_tutorialspoint(SeleniumBase.url)
    time.sleep(5)
    SharedVariables.expected_title = BrowserUtilities.get_title()
    SharedVariables.expected_url = BrowserUtilities.get_current_url()
    print("TITLE AFTER ASSIGNING: " + SharedVariables.expected_title)
    print("URL AFTER ASSIGNING: " + SharedVariables.expected_url)


@When('user enters "{text}" in First name')
def step_impl(context, text):
    context.tutorialFunctions.enter_first_name(text)


@When('user enters "{text}" in Last name')
def step_impl(context, text):
    context.tutorialFunctions.enter_last_name(text)
    time.sleep(10)

@Then('user validates the "{text}" label in First name textbox')
def step_impl(context, text):
    expected_label = context.tutorialFunctions.retrieve_first_name_label()
    AssertionUtilities.assert_contains(text, expected_label)


@When('user copies the value from Firstname textbox')
def step_impl(context):
    context.tutorialFunctions.copy_value_from_first_name()


@When('user pastes the value into Lastname textbox')
def step_impl(context):
    context.tutorialFunctions.paste_value_into_last_name()


@Then('user validates if the value "{text}" is present in Lastname textbox using JSExecutor')
def step_impl(context, text):
    expected_value = context.tutorialFunctions.retrieve_value_from_last_name_js()
    print("LAST NAME EXTRACTED FROM JS: " + expected_value)
    AssertionUtilities.assert_equals(expected_value, text)


@When('user clears the Firstname textbox using actions')
def step_impl(context):
    context.tutorialFunctions.clear_first_name_using_actions()


@When('user copies the value from Lastname textbox into Firstname textbox')
def step_impl(context):
    context.tutorialFunctions.copy_paste_value()


@Then('user validates the value "{text}" in Last name textbox')
def step_impl(context, text):
    expected_value = context.tutorialFunctions.retrieve_value_from_last_name()
    AssertionUtilities.assert_equals(expected_value, text)


@When('user clears the Last name textbox')
def step_impl(context):
    context.tutorialFunctions.clear_last_name()


@When('user enters "{text}" in first name using JSExecutor')
def step_impl(context, text):
    context.tutorialFunctions.enter_first_name_using_js(text)


@When('user enters "{text}" in Last name using actions')
def step_impl(context, text):
    context.tutorialFunctions.enter_last_name_using_actions(text)


@Then('user validates the "{text}" label using JSExecutor')
def step_impl(context, text):
    expected_label = context.tutorialFunctions.retrieve_yoe_label()
    AssertionUtilities.assert_contains(text, expected_label)


@When('user selects the Male radiobutton')
def step_impl(context):
    context.tutorialFunctions.select_male()


@Then('user validates if the Male radiobutton is selected')
def step_impl(context):
    result = context.tutorialFunctions.validate_selection_male()
    AssertionUtilities.assert_if_true(result)


@Then('user validates if Female radiobutton is enabled')
def step_impl(context):
    result = context.tutorialFunctions.validate_enabled_female()
    AssertionUtilities.assert_if_true(result)


@Then('user validates if Female radiobutton is not selected')
def step_impl(context):
    result = context.tutorialFunctions.validate_selection_female()
    AssertionUtilities.assert_if_false(result)


@When('user selects the Manual Tester checkbox using checkbox method')
def step_impl(context):
    context.tutorialFunctions.select_manual_tester()


@When('user selects the Automation Tester checkbox using click method')
def step_impl(context):
    context.tutorialFunctions.select_automation_tester()


@When('user unselects the Automation Tester checkbox')
def step_impl(context):
    context.tutorialFunctions.unselect_automation_tester()


@Then('user asserts if the Automation Tester checkbox has been unselected')
def step_impl(context):
    result = context.tutorialFunctions.validate_automation_tester_selection()
    AssertionUtilities.assert_if_false(result)


@When('user selects YoE as 7 using JSExecutor click')
def step_impl(context):
    context.tutorialFunctions.select_yoe_seven()


@When('user changes the YoE selection as 5 using actions click')
def step_impl(context):
    context.tutorialFunctions.select_yoe_five()


@When('user selects continent as "{text}" using visible text')
def step_impl(context, text):
    context.tutorialFunctions.select_continent_text(text)


@Then('user validates the selected value "{text}" from dropdown')
def step_impl(context, text):
    selected_value = context.tutorialFunctions.retrieve_selected_continent()
    print("SELECTED VALUE FROM DROPDOWN: " + selected_value)
    AssertionUtilities.assert_equals(selected_value, text)


@When('user selects continent as "{text}" using value')
def step_impl(context, text):
    context.tutorialFunctions.select_continent_value(text)


@When('user retrieves the attributes of Male radiobutton')
def step_impl(context):
    attr_name = context.tutorialFunctions.retrieve_attribute_male("name")
    attr_type = context.tutorialFunctions.retrieve_attribute_male("type")
    attr_value = context.tutorialFunctions.retrieve_attribute_male("value")
    attr_style = context.tutorialFunctions.retrieve_attribute_male("style")
    print("NAME: {0}, TYPE: {1}, VALUE: {2}, STYLE: {3}".format(attr_name, attr_type, attr_value, attr_style))


@When('user retrieves the attributes of Female radiobutton via JSExecutor')
def step_impl(context):
    attr_name = context.tutorialFunctions.retrieve_attribute_female("name")
    attr_type = context.tutorialFunctions.retrieve_attribute_female("type")
    attr_value = context.tutorialFunctions.retrieve_attribute_female("value")
    attr_style = context.tutorialFunctions.retrieve_attribute_female("style")
    print("NAME: {0}, TYPE: {1}, VALUE: {2}, STYLE: {3}".format(attr_name, attr_type, attr_value, attr_style))


@Then('user updates the "{attr}" attribute to "{value}" and validates the change')
def step_impl(context, attr, value):
    context.tutorialFunctions.update_attribute_male(attr, value)
    attr_value = context.tutorialFunctions.retrieve_attribute_male(attr)
    print("UPDATED VALUE: " + attr_value)
    # time.sleep(10)
    AssertionUtilities.assert_equals(value, attr_value)


@When('user prints the color of the Firstname label')
def step_impl(context):
    color = context.tutorialFunctions.retrieve_color_male("color")
    print("THE COLOR OF FIRST NAME IS: " + color)
