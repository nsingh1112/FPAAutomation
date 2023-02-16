import time

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.HomePageControls import HomePageControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities


class LoginFunctions:

    def __init__(self, driver):
        self.homePageControls = HomePageControls(SeleniumBase.driver)

    def press_enter_button(self):
        config = SeleniumBase.read_config()
        browser_name = config['browser']['browser_name']
        if browser_name == 'edge':
            for i in range(3):
                SeleniumUtilities.press_keyboard_key('tab')
        while True:
            time.sleep(3)
            SeleniumUtilities.press_keyboard_key('enter')
            break

    def access_shell_hub(self):
        BrowserUtilities.maximize_window()
        BrowserUtilities.navigate_to_url(SeleniumBase.url)
        time.sleep(10)

        browurl = BrowserUtilities.get_current_url()
        BrowserUtilities.log.info("Navigated to the URL: {0}. after login" +browurl)
        SeleniumUtilities.press_keyboard_key('enter')


    def navigate_to_url(self, url):
        BrowserUtilities.navigate_to_url(url)



