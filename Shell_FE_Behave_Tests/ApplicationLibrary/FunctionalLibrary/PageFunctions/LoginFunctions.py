import time

import requests

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.HomePageControls import HomePageControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.LoginControls import LoginControls


class LoginFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.homePageControls = HomePageControls(SeleniumBase.driver)
        self.loginControls = LoginControls(SeleniumBase.driver)


    def press_enter_button(self):

        config = SeleniumBase.read_config()
        browser_name = config['browser']['browser_name']
        if browser_name == 'edge':
            for i in range(3):
                SeleniumUtilities.press_keyboard_key('tab')
        while True:
            time.sleep(3)

            # Use this to click on cancel button in local
            #SeleniumUtilities.press_keyboard_key('tab')
            #SeleniumUtilities.press_keyboard_key('tab')
            #SeleniumUtilities.press_keyboard_key('tab')
            #SeleniumUtilities.press_keyboard_key('enter')
            time.sleep(3)
            break

    def access_shell_hub(self):
        BrowserUtilities.maximize_window()
        BrowserUtilities.navigate_to_url(SeleniumBase.url)
        time.sleep(5)

        browurl = BrowserUtilities.get_current_url()
        BrowserUtilities.log.info("Navigated to the URL: {0}. after login " +browurl)
        SeleniumUtilities.press_keyboard_key('enter')


    def navigate_to_url(self, url):
        BrowserUtilities.navigate_to_url(url)

    def access_shell_hub1(self):
        SeleniumUtilities.press_keyboard_key('enter')
        time.sleep(2)

    def click_pingIdMFA(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.loginControls.get_btnPingIdMFA())
        SeleniumUtilities.click_element(self.loginControls.get_btnPingIdMFA())
        WaitUtilities.wait_for_element_to_be_clickable(self.loginControls.get_pingIdMFAUserName())
        SeleniumUtilities.send_text(self.loginControls.get_pingIdMFAUserName(), "nupur.singh@shell.com")
        WaitUtilities.wait_for_element_to_be_clickable(self.loginControls.get_pingIdMFAPwd())
        SeleniumUtilities.send_text(self.loginControls.get_pingIdMFAPwd(), "Winter#11112")
        WaitUtilities.wait_for_element_to_be_clickable(self.loginControls.get_pingIdMFASignOn())
        SeleniumUtilities.click_element(self.loginControls.get_pingIdMFASignOn())
        WaitUtilities.wait_for_element_to_be_invisible(self.loginControls.get_pingIdMFAAppName(),15000)
        time.sleep(15)
        browserurl = BrowserUtilities.get_current_url()
        BrowserUtilities.log.info("Navigated to the URL: {0}. after Ping ID MFA " + browserurl)
        textbody = self.loginControls.get_bodyText().text
        BrowserUtilities.log.info("Body Text " + textbody)






