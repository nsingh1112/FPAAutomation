import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
"""This class file holds the multiple driver instances as it's need based on linking"""


class DriverHelper:
    currentDriverInstance = SeleniumBase.driver

    @staticmethod
    def navigate_to_url():
        BrowserUtilities.maximize_window()
        BrowserUtilities.navigate_to_url(SeleniumBase.url)


    @staticmethod
    def create_new_driver_instance():
        """Initializes driver to ChromeDriver. Based on value in behave.ini file WebDriver Manager or
        WebDriver binary would be used.

        Returns:
            ChromeDriver instance
        """
        SeleniumBase.__opts = webdriver.ChromeOptions()
        SeleniumBase.set_options(SeleniumBase.__opts)
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=SeleniumBase.__opts)
            return driver
        except Exception as err:
            raise Exception(err)




