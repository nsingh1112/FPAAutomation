import time

from behave import Given, When, Then
import SharedVariables
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.AcademyFunctions import AcademyFunctions
from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities


@Given('user navigates to Academy site')
def step_impl(context):
    context.academyFunctions = AcademyFunctions()
    context.academyFunctions.access_academy_site("https://www.rahulshettyacademy.com/AutomationPractice/")


@When('user navigates back')
def step_impl(context):
    context.academyFunctions.navigate_back()
    print("TITLE FROM PREVIOUS FEATURE FILE: " + SharedVariables.expected_title)


@Then('user validates the title equality using Wait utilities')
def step_impl(context):
    actual_title = context.academyFunctions.validate_title_equality(SharedVariables.expected_title)
    AssertionUtilities.assert_equals(SharedVariables.expected_title, actual_title)


@When('user navigates forward')
def step_impl(context):
    context.academyFunctions.navigate_forward()


@Then('user validates if the title contains the expected value using Wait Utilities')
def step_impl(context):
    actual_title = context.academyFunctions.validate_title_contains(SharedVariables.expected_title)
    AssertionUtilities.assert_contains(SharedVariables.expected_title, actual_title)


@Then('user validates the url equality using Wait Utilities')
def step_impl(context):
    actual_url = context.academyFunctions.validate_url_equality(SharedVariables.expected_url)
    print("ACTUAL URL: " + actual_url)
    print("EXPECTED URL: " + SharedVariables.expected_url)
    AssertionUtilities.assert_equals(SharedVariables.expected_url, actual_url)


@Then('user validates if the url contains the expected value using Wait Utilities')
def step_impl(context):
    actual_url = context.academyFunctions.validate_url_contains(SharedVariables.expected_url)
    AssertionUtilities.assert_contains(SharedVariables.expected_url, actual_url)


@When('user refreshes the page')
def step_impl(context):
    BrowserUtilities.refresh_page()


@Then('user waits for the text "{text}" to be present in the page')
def step_impl(context, text):
    actual_text = context.academyFunctions.validate_text_present(text)
    AssertionUtilities.assert_equals(actual_text, text)
    AssertionUtilities.assert_not_none(actual_text)


@Then('user waits for the value "{text}" to be present in the page')
def step_impl(context, text):
    actual_value = context.academyFunctions.validate_value_present(text)
    print("EXTRACTED VALUE: " + actual_value)
    AssertionUtilities.assert_equals(actual_value, text)


@When('user clicks on Open window button')
def step_impl(context):
    context.academyFunctions.click_open_window()


@Then('user verifies the number of windows "{text}"')
def step_impl(context, text):
    window_count = context.academyFunctions.validate_child_window_count(text)
    AssertionUtilities.assert_equals(int(text), window_count)


@When('user switches to child window')
def step_impl(context):
    context.academyFunctions.switch_to_child_window()
    SharedVariables.child_window_title = BrowserUtilities.get_title()
    print("CHILD WINDOW TITLE: " + SharedVariables.child_window_title)


@When('user switches to parent window')
def step_impl(context):
    context.academyFunctions.switch_to_parent_window()


@When('user switches to child window and closes it')
def step_impl(context):
    context.academyFunctions.switch_to_child_window_and_close()


@Then('user switches to child window by title, asserts and closes it')
def step_impl(context):
    window_title = context.academyFunctions.switch_to_child_by_title()
    AssertionUtilities.assert_equals(window_title,
                                     "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy")
    BrowserUtilities.close_window()
    BrowserUtilities.switch_to_parent_window()


@When('user clicks on Open Tab button')
def step_impl(context):
    context.academyFunctions.click_open_tab()


@Then('user switches to child tab by title, asserts and closes it')
def step_impl(context):
    window_title = context.academyFunctions.switch_to_child_tab_by_title()
    AssertionUtilities.assert_equals(window_title, "Rahul Shetty Academy")
    BrowserUtilities.close_window()
    BrowserUtilities.switch_to_parent_window()


@When('user clicks on Alert button')
def step_impl(context):
    context.academyFunctions.click_alert_button()


@Then('user accepts Alert')
def step_impl(context):
    BrowserUtilities.accept_alert()


@When('user clicks on Confirm button')
def step_impl(context):
    context.academyFunctions.click_confirm_alert()


@Then('user accepts confirm alert')
def step_impl(context):
    BrowserUtilities.accept_alert()


@Then('user dismisses confirm alert')
def step_impl(context):
    BrowserUtilities.dismiss_alert()


@Then('user validates the Alert text')
def step_impl(context):
    alert_text = BrowserUtilities.get_alert_text()
    print("ALERT TEXT: " + alert_text)


@When('user switches to the frame')
def step_impl(context):
    context.academyFunctions.wait_switch_to_frame()


@When('user selects blog in frame')
def step_impl(context):
    context.academyFunctions.click_blogs()


@When('scrolls down in frame')
def step_impl(context):
    context.academyFunctions.scroll_down_frame()


@When('user hovers mouse')
def step_impl(context):
    context.academyFunctions.move_mouse()


@Then('validates if options are displayed')
def step_impl(context):
    result = context.academyFunctions.move_mouse_options()
    AssertionUtilities.assert_if_true(result)


@When('user selects value from dropdown')
def step_impl(context):
    context.academyFunctions.validate_dropdown()


@When('user scrolls down window')
def step_impl(context):
    SeleniumUtilities.scroll_window("2500")
    time.sleep(5)


@When('user scrolls the window up')
def step_impl(context):
    SeleniumUtilities.scroll_window("-2500")
    time.sleep(5)

@When('user takes screenshot')
def step_impl(context):
    context.academyFunctions.screenshot_validation()

@When('user resizes the browser')
def step_impl(context):
    BrowserUtilities.resize_browser(500, 500)
    time.sleep(5)

@When('user clicks on the Hide button')
def step_impl(context):
    context.academyFunctions.click_hide()

@When('user clicks on the Show button')
def step_impl(context):
    context.academyFunctions.click_show()

@Then('user verifies if the text box is hidden')
def step_impl(context):
    result = context.academyFunctions.confirm_hidden()
    AssertionUtilities.assert_if_true(result)

@Then('user verifies if the text box is shown')
def step_impl(context):
    result = context.academyFunctions.confirm_shown()
    AssertionUtilities.assert_if_true(result)