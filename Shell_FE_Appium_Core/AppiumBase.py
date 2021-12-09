import logging
import os
import time

from appium.webdriver.appium_service import AppiumService
from configparser import ConfigParser
from appium import webdriver
from selenium.webdriver import DesiredCapabilities


class AppiumBase:
    """AppiumBase class contains functions for reading config file, app initiation"""
    # region Class Variable Declarations
    __config = None
    __platformName = None
    __platformVersion = None
    __deviceName = None
    __app = None
    __appPackage = None
    __appActivity = None
    __remoteURL = None
    __browser_name = None
    driver = None
    current_working_directory = os.path.dirname(os.getcwd())
    configfile = current_working_directory + '\\Shell_FE_Behave_Tests\\config.ini'
    appium_Service = AppiumService()

    # endregion
    @staticmethod
    def read_config():
        """Reads Config.INI file present in Shell_FE_Behave_Tests folder.
           Returns:
                An instance of ConfigParser.
        """
        configuration = ConfigParser()
        configuration.read(AppiumBase.configfile)
        return configuration

    @staticmethod
    def start_appium_server():
        """Starts the Appium Server"""
        AppiumBase.appium_Service.start()
        print("Status of APPIUM Server :", AppiumBase.appium_Service.is_running)

    @staticmethod
    def stop_appium_server():
        """Stops the current Appium server"""
        AppiumBase.appium_Service.stop()

    @staticmethod
    def read_values(section_value):
        """"Read and Assigns respective values to class variables from Config.INI file.
            :args:
            -section_value - chooses the section from which value to be fetched
        """
        AppiumBase.__config = AppiumBase.read_config()
        AppiumBase.__platformName = AppiumBase.__config[section_value]['platformName']
        AppiumBase.__platformVersion = AppiumBase.__config[section_value]['platformVersion']
        AppiumBase.__deviceName = AppiumBase.__config[section_value]['deviceName']
        AppiumBase.__app = AppiumBase.__config[section_value]['appPath']
        AppiumBase.__appPackage = AppiumBase.__config[section_value]['appPackage']
        AppiumBase.__appActivity = AppiumBase.__config[section_value]['appActivity']
        AppiumBase.__remoteURL = AppiumBase.__config[section_value]['remoteURL']
        #AppiumBase.__browser_name = AppiumBase.__config[section_value]['browsername']

    @staticmethod
    def launch_app():
        """Launch the Application
           Returns the driver instance
        """
        # caps = DesiredCapabilities()
        # caps.ANDROID.copy()
        # caps['plat']
        desired_caps = {'platformName': AppiumBase.__platformName, 'platformVersion': AppiumBase.__platformVersion,
                        'deviceName': AppiumBase.__deviceName, 'app': AppiumBase.__app,
                        'appPackage': AppiumBase.__appPackage, 'appActivity': AppiumBase.__appActivity,
                        }

        AppiumBase.driver = webdriver.Remote(AppiumBase.__remoteURL, desired_caps)
        return AppiumBase.driver

    @staticmethod
    def is_App_installed():
        """Checks the app is installed in the device
            Return True- if the application is installed
        """
        app_installed = AppiumBase.driver.is_app_installed(AppiumBase.__app)
        return app_installed

    @staticmethod
    def close_driver():
        """Closes the driver instance"""
        if AppiumBase.driver is not None:
            AppiumBase.driver.quit()
