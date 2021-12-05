import logging
import os
import time

from appium.webdriver.appium_service import AppiumService
from configparser import ConfigParser
from appium import webdriver


class AppiumBase:
    def __init__(self, driver):
        self.driver = driver
    # region Class Variable Declarations
    __config = None
    __platformName = None
    __platformVersion = None
    __deviceName = None
    __app = None
    __appPackage = None
    __appActivity = None
    __remoteURL = None
    driver = None
    current_working_directory = os.path.dirname(os.getcwd())
    configfile = current_working_directory + '\\Shell_FE_Behave_Tests\\config.ini'
    appium_Service = AppiumService()

    # endregion
    @staticmethod
    def read_config():
        configuration = ConfigParser()
        configuration.read(AppiumBase.configfile)
        return configuration

    @staticmethod
    def start_appium_server():
        AppiumBase.appium_Service.start()
        print("Status of APPIUM Server :", AppiumBase.appium_Service.is_running)

    @staticmethod
    def stop_appium_server():
        AppiumBase.appium_Service.stop()

    @staticmethod
    def read_values(section_value):
        AppiumBase.__config = AppiumBase.read_config()
        AppiumBase.__platformName = AppiumBase.__config[section_value]['platformName']
        AppiumBase.__platformVersion = AppiumBase.__config[section_value]['platformVersion']
        AppiumBase.__deviceName = AppiumBase.__config[section_value]['deviceName']
        AppiumBase.__app = AppiumBase.__config[section_value]['appPath']
        AppiumBase.__appPackage = AppiumBase.__config[section_value]['appPackage']
        AppiumBase.__appActivity = AppiumBase.__config[section_value]['appActivity']
        AppiumBase.__remoteURL = AppiumBase.__config[section_value]['remoteURL']

    @staticmethod
    def launch_app():
        desired_caps = {'platformName': AppiumBase.__platformName, 'platformVersion': AppiumBase.__platformVersion,
                        'deviceName': AppiumBase.__deviceName, 'app': AppiumBase.__app,
                        'appPackage': AppiumBase.__appPackage, 'appActivity': AppiumBase.__appActivity}

        AppiumBase.driver = webdriver.Remote(AppiumBase.__remoteURL, desired_caps)
        return AppiumBase.driver

    @staticmethod
    def is_App_installed():
        app_installed = AppiumBase.driver.is_app_installed(AppiumBase.__app)

    @staticmethod
    def click_by_accessibility_id(element_id):
        element = AppiumBase.driver.find_element_by_accessibility_id(element_id)
        element.click()

    @staticmethod
    def click_by_id(element_id):
        element = AppiumBase.driver.find_element_by_id(element_id)
        element.click()

    @staticmethod
    def close_driver():
        AppiumBase.driver.quit()
