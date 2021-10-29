import logging
import os
import time

from configparser import ConfigParser
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


class AppiumBase:
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
    appiumService = AppiumService()
    current_working_directory = os.path.dirname(os.getcwd())
    configfile = current_working_directory + '\\Shell_FE_Behave_Tests\\config.ini'

    # endregion
    @staticmethod
    def read_config():
        configuration = ConfigParser()
        configuration.read(AppiumBase.configfile)
        return configuration

    @staticmethod
    def read_values():
        AppiumBase.__config = AppiumBase.read_config()
        AppiumBase.__platformName = AppiumBase.__config['nativeApp']['platformName']
        AppiumBase.__platformVersion = AppiumBase.__config['nativeApp']['platformVersion']
        AppiumBase.__deviceName = AppiumBase.__config['nativeApp']['deviceName']
        AppiumBase.__app = AppiumBase.__config['nativeApp']['appPath']
        AppiumBase.__appPackage = AppiumBase.__config['nativeApp']['appPackage']
        AppiumBase.__appActivity = AppiumBase.__config['nativeApp']['appActivity']
        AppiumBase.__remoteURL = AppiumBase.__config['nativeApp']['remoteURL']

    @staticmethod
    def launch_app():
        desired_caps = {}
        desired_caps['platformName'] = AppiumBase.__platformName
        desired_caps['platformVersion'] = AppiumBase.__platformVersion
        desired_caps['deviceName'] = AppiumBase.__deviceName
        desired_caps['app'] = AppiumBase.__app
        desired_caps['appPackage'] = AppiumBase.__appPackage
        desired_caps['appActivity'] = AppiumBase.__appActivity

        AppiumBase.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return AppiumBase.driver

    @staticmethod
    def is_App_installed():
        app_installed = AppiumBase.driver.is_app_installed(AppiumBase.__app)
        print(app_installed)

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
