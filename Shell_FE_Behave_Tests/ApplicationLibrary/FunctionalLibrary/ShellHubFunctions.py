from Shell_FE_Selenium_Core.Utilities.AccessibilityUtilities import AccessibilityUtilities

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.ShellHubControls import ShellHubControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.AccessibilityUtilities import AccessibilityUtilities
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities


class ShellHubFunctions:

    def __init__(self):
        self.shellHubControls = ShellHubControls(SeleniumBase.driver)

    def access_shell_hub(self):
        BrowserUtilities.navigate_to_url(SeleniumBase.url)

    def navigate_to_url(self, url):
        BrowserUtilities.navigate_to_url(url)

    def validate_url_equality(self, url):
        BrowserUtilities.refresh_page()
        WaitUtilities.wait_for_url_to_match_value(url)
        return BrowserUtilities.get_current_url()

    def search_value(self, value):
        BrowserUtilities.refresh_page()
        WaitUtilities.wait_for_element_to_be_visible(self.shellHubControls.search_box)
        WaitUtilities.wait_for_element_to_be_clickable(self.shellHubControls.search_box)
        SeleniumUtilities.send_text(self.shellHubControls.get_search_box(), value)
        SeleniumUtilities.click_element_by_actions(self.shellHubControls.get_search())

    def validate_title_equality(self, title):
        WaitUtilities.wait_for_title_to_match_value(title)
        return BrowserUtilities.get_title()

    def navigate_back_to_shell_hub(self, url):
        BrowserUtilities.navigate_back()
        WaitUtilities.wait_for_url_to_match_value(url)

    def click_yammer(self):
        WaitUtilities.wait_for_element_to_be_visible(self.shellHubControls.yammer)
        WaitUtilities.wait_for_element_to_be_clickable(self.shellHubControls.yammer)
        SeleniumUtilities.click_element(self.shellHubControls.get_yammer())

    def get_window_count(self, value):
        WaitUtilities.wait_for_number_of_windows_to_match(int(value))
        return len(SeleniumBase.driver.window_handles)

    def switch_to_Yammer(self, title):
        BrowserUtilities.switch_to_window_by_title(title)

    def close_Yammer(self):
        BrowserUtilities.switch_to_child_window()
        BrowserUtilities.switch_to_parent_window()

    def log_out(self):
        SeleniumUtilities.click_element_using_javascript_executor(self.shellHubControls.get_user_name())
        SeleniumUtilities.click_element_by_actions(self.shellHubControls.get_log_out())

    def check_select_account(self):
        WaitUtilities.wait_for_element_to_be_visible(self.shellHubControls.pick_account, 30)
        is_displayed = SeleniumUtilities.is_element_displayed(self.shellHubControls.get_pick_account())
        return is_displayed

    def check_shell_hub_accessibility(self):
        return AccessibilityUtilities.analyze_page()
