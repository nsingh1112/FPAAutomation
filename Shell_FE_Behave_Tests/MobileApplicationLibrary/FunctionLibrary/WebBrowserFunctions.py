import time

from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Behave_Tests.MobileApplicationLibrary.ControlLibrary.WebBrowserControls import BrowserControls
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Appium_Core.Utilities.AssertUtilities import AssertUtilities


class BrowserFunctions:
    def __init__(self):
        self.BrowserControls = BrowserControls(AppiumBase.driver)

    def launch_web(self, url):
        AndroidUtilities.navigate_to_url(url)

    def get_context(self):
        app_context = AndroidUtilities.get_app_contexts()
        print("#########App context :", app_context)

    def switch_context(self, view_switch):
        AndroidUtilities.switch_context(view_switch)

    def verify_title(self):
        title = AndroidUtilities.get_title()
        print("############ Title of the page is :" + title)
        AssertUtilities.assert_equals(title, "Sign in to your account")

    def click_username(self):
        WaitUtilities.wait_element_to_be_visible(self.BrowserControls.user_name)
        AndroidUtilities.click_element(self.BrowserControls.get_username())

    def pass_value(self):
        AndroidUtilities.send_text_to_element(self.BrowserControls.get_username(), "saktivel.rajasekar@shell.com")
        WaitUtilities.wait_for_element_to_be_clickable(self.BrowserControls.next_btn)
        AndroidUtilities.click_element(self.BrowserControls.get_next_btn())

    def check_authentication(self):
        WaitUtilities.wait_element_to_be_visible(self.BrowserControls.authentication_text)
