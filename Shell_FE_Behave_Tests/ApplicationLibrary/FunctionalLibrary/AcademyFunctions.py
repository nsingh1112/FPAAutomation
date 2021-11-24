import time

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.AcademyObjects import AcademyObjects
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities


class AcademyFunctions:

    def __init__(self):
        self.academyObj = AcademyObjects(SeleniumBase.driver)

    def access_academy_site(self, url):
        BrowserUtilities.navigate_to_url(url)

    def get_title(self):
        self.title = BrowserUtilities.get_title()

    def navigate_back(self):
        BrowserUtilities.navigate_back()

    def navigate_forward(self):
        BrowserUtilities.navigate_forward()

    def validate_title_equality(self, title):
        WaitUtilities.wait_for_title_to_match_value(title)
        return BrowserUtilities.get_title()

    def validate_title_contains(self, title):
        WaitUtilities.wait_for_title_to_contain_value(title)
        return BrowserUtilities.get_title()

    def validate_url_equality(self, url):
        WaitUtilities.wait_for_url_to_match_value(url)
        return BrowserUtilities.get_current_url()

    def validate_url_contains(self, url):
        WaitUtilities.wait_for_url_to_contain_value(url)
        return BrowserUtilities.get_current_url()

    def validate_text_present(self, text):
        WaitUtilities.wait_for_text_to_be_present(self.academyObj.header, text)
        return SeleniumUtilities.get_text(self.academyObj.get_header())

    def validate_value_present(self, value):
        WaitUtilities.wait_for_value_to_be_present(self.academyObj.option_one, value)
        return SeleniumUtilities.get_attribute(self.academyObj.get_option_one(), "value")

    def click_open_window(self):
        SeleniumUtilities.click_element(self.academyObj.get_open_window())

    def validate_child_window_count(self, value):
        WaitUtilities.wait_for_number_of_windows_to_match(int(value))
        return len(SeleniumBase.driver.window_handles)

    def switch_to_child_window(self):
        BrowserUtilities.switch_to_child_window()

    def switch_to_parent_window(self):
        BrowserUtilities.switch_to_parent_window()

    def switch_to_child_window_and_close(self):
        BrowserUtilities.switch_to_child_window()
        BrowserUtilities.close_window()
        BrowserUtilities.switch_to_parent_window()

    def switch_to_child_by_title(self):
        BrowserUtilities.switch_to_window_by_title(
            "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy")
        return BrowserUtilities.get_title()

    def click_open_tab(self):
        SeleniumUtilities.click_element(self.academyObj.get_open_tab())

    def switch_to_child_tab_by_title(self):
        BrowserUtilities.switch_to_window_by_title("Rahul Shetty Academy")
        return BrowserUtilities.get_title()

    def click_alert_button(self):
        WaitUtilities.wait_for_alert_to_be_present()
        SeleniumUtilities.click_element(self.academyObj.get_open_alert())

    def click_confirm_alert(self):
        SeleniumUtilities.click_element(self.academyObj.get_confirm_alert())

    def wait_switch_to_frame(self):
        WaitUtilities.wait_for_frame_and_switch(self.academyObj.frame)
        # BrowserUtilities.switch_to_iframe(1)

    def click_blogs(self):
        SeleniumUtilities.click_element(self.academyObj.get_frame_blg())

    def scroll_down_frame(self):
        SeleniumUtilities.scroll_window("500")

    def move_mouse(self):
        SeleniumUtilities.scroll_to_element(self.academyObj.get_mouse_hover())
        SeleniumUtilities.move_focus_to_element(self.academyObj.get_mouse_hover())

    def move_mouse_options(self):
        WaitUtilities.wait_for_element_to_be_visible(self.academyObj.top)
        WaitUtilities.wait_for_element_to_be_visible(self.academyObj.reload)
        result_1 = SeleniumUtilities.is_element_displayed(self.academyObj.get_top())
        result_2 = SeleniumUtilities.is_element_displayed(self.academyObj.get_reload())
        result = result_1 and result_2
        return result

    def screenshot_validation(self):
        BrowserUtilities.take_screenshot_of_element(self.academyObj.get_open_window())
        BrowserUtilities.take_screenshot()

    def validate_dropdown(self):
        SeleniumUtilities.select_from_dropdown_using_value(self.academyObj.get_dropdown(), "option1")

    def click_hide(self):
        SeleniumUtilities.scroll_to_element(self.academyObj.get_hide_button())
        time.sleep(5)
        SeleniumUtilities.click_element(self.academyObj.get_hide_button())
        time.sleep(5)

    def click_show(self):
        SeleniumUtilities.scroll_to_element(self.academyObj.get_show_button())
        SeleniumUtilities.click_element(self.academyObj.get_show_button())

    def confirm_hidden(self):
        WaitUtilities.wait_for_element_to_be_invisible(self.academyObj.hidden_textbox)
        time.sleep(5)
        return SeleniumUtilities.is_element_displayed(self.academyObj.get_hidden_textbox())

    def confirm_shown(self):
        WaitUtilities.wait_for_element_to_be_visible(self.academyObj.hidden_textbox)
        time.sleep(5)
        return SeleniumUtilities.is_element_displayed(self.academyObj.get_hidden_textbox())

