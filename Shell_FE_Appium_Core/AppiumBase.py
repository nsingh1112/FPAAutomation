import os
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
    __application_type = None
    __automation_name = None
    __udid = None
    __bundle_id = None
    __devicePlatform = None
    driver = None
    current_working_directory = os.path.dirname(os.getcwd())
    configfile = current_working_directory + '/Shell_FE_Behave_Tests/behave.ini'
    appium_Service = AppiumService()

    # endregion

    # region Appium server instance
    @staticmethod
    def start_appium_server():
        """Starts the Appium Server"""
        AppiumBase.appium_Service.start()

    @staticmethod
    def stop_appium_server():
        """Stops the current Appium server"""
        AppiumBase.appium_Service.stop()

    @staticmethod
    def appium_server_status():
        """Checks the appium server status
           :returns:
                   True - if the appium server instance is running
        """
        return AppiumBase.appium_Service.is_running

    # endregion

    # region Reading values from configuration file
    @staticmethod
    def read_config():
        """Reads behave.INI file present in Shell_FE_Behave_Tests folder.
           Returns:
                An instance of ConfigParser.
        """
        configuration = ConfigParser()
        configuration.read(AppiumBase.configfile)
        return configuration

    @staticmethod
    def read_values():
        """"Read and Assigns respective values to class variables from behave.INI file.
            :args:
            -section_value - chooses the section from which value to be fetched
        """
        AppiumBase.__config = AppiumBase.read_config()
        AppiumBase.__devicePlatform = AppiumBase.__config['automationplatform']['platformtype']
        if AppiumBase.__devicePlatform.lower() == "android":
            AppiumBase.__platformName = AppiumBase.__config['Android']['platformName']
            AppiumBase.__platformVersion = AppiumBase.__config['Android']['platformVersion']
            AppiumBase.__deviceName = AppiumBase.__config['Android']['deviceName']
            AppiumBase.__app = AppiumBase.__config['Android']['appPath']
            AppiumBase.__appPackage = AppiumBase.__config['Android']['appPackage']
            AppiumBase.__appActivity = AppiumBase.__config['Android']['appActivity']
            AppiumBase.__remoteURL = AppiumBase.__config['Android']['remoteURL']
            AppiumBase.__application_type = AppiumBase.__config['Android']['applicationType']
            AppiumBase.__automation_name = AppiumBase.__config['Android']['automationName']
            AppiumBase.__browser_name = AppiumBase.__config['Android']['browserName']

        elif AppiumBase.__devicePlatform.lower() == "ios":
            AppiumBase.__application_type = AppiumBase.__config['iOS']['applicationType']
            AppiumBase.__platformName = AppiumBase.__config['iOS']['platformName']
            AppiumBase.__platformVersion = AppiumBase.__config['iOS']['platformVersion']
            AppiumBase.__deviceName = AppiumBase.__config['iOS']['deviceName']
            AppiumBase.__udid = AppiumBase.__config['iOS']['udid']
            AppiumBase.__bundle_id = AppiumBase.__config['iOS']['bundleId']
            AppiumBase.__app = AppiumBase.__config['iOS']['appPath']
            AppiumBase.__remoteURL = AppiumBase.__config['iOS']['remoteURL']
            AppiumBase.__automation_name = AppiumBase.__config['iOS']['automationName']
            print(AppiumBase.__platformName)
            print(AppiumBase.__platformVersion)
            print(AppiumBase.__deviceName)
            print(AppiumBase.__udid)
            print(AppiumBase.__bundle_id)

    # endregion

    # region Launch Application
    @staticmethod
    def launch_application():
        """Launches the Application
           Returns the driver instance
        """

        if AppiumBase.__application_type.lower() == "native" and AppiumBase.__devicePlatform.lower() == "android":
            desired_caps = {'platformName': AppiumBase.__platformName, 'platformVersion': AppiumBase.__platformVersion,
                            'deviceName': AppiumBase.__deviceName, 'automationName': AppiumBase.__automation_name,
                            'app': AppiumBase.__app, 'appPackage': AppiumBase.__appPackage,
                            'appActivity': AppiumBase.__appActivity,
                            }
            AppiumBase.driver = webdriver.Remote(AppiumBase.__remoteURL, desired_capabilities=desired_caps)

        elif AppiumBase.__application_type.lower() == "hybrid" and AppiumBase.__devicePlatform.lower() == "android":
            desired_caps = {'platformName': AppiumBase.__platformName, 'platformVersion': AppiumBase.__platformVersion,
                            'deviceName': AppiumBase.__deviceName, 'automationName': AppiumBase.__automation_name,
                            'app': AppiumBase.__app, 'appPackage': AppiumBase.__appPackage,
                            'appActivity': AppiumBase.__appActivity,
                            }
            AppiumBase.driver = webdriver.Remote(AppiumBase.__remoteURL, desired_capabilities=desired_caps)

        elif AppiumBase.__application_type.lower() == "webbrowser" and AppiumBase.__devicePlatform.lower() == "android":
            desired_caps = {'platformName': AppiumBase.__platformName, 'platformVersion': AppiumBase.__platformVersion,
                            'deviceName': AppiumBase.__deviceName, 'automationName': AppiumBase.__automation_name,
                            'browserName': AppiumBase.__browser_name
                            }
            AppiumBase.driver = webdriver.Remote(AppiumBase.__remoteURL, desired_capabilities=desired_caps)

        elif AppiumBase.__application_type.lower() == "native" and AppiumBase.__devicePlatform.lower() == "ios":
            desired_caps = {'platformName': AppiumBase.__platformName, 'platformVersion': AppiumBase.__platformVersion,
                            'deviceName': AppiumBase.__deviceName, 'udid': AppiumBase.__udid, 'automationName' : AppiumBase.__automation_name,
                             'app':AppiumBase.__app
                            # 'bundleID': AppiumBase.__bundle_id
                            }
            AppiumBase.driver = webdriver.Remote(AppiumBase.__remoteURL, desired_capabilities=desired_caps)

    # endregion

    @staticmethod
    def install_app():
        """Install the App in the device"""
        AppiumBase.driver.install_app(AppiumBase.__app)

    @staticmethod
    def is_App_installed():
        """Checks the app is installed in the device
            Return True- if the application is installed
        """
        app_installed = AppiumBase.driver.is_app_installed(AppiumBase.__app)
        return app_installed

    @staticmethod
    def reset_app():
        """Reset the currently running app for this session"""
        AppiumBase.driver.reset()

    @staticmethod
    def close_app():
        """It closes the app on the device"""
        AppiumBase.driver.close_app()

    @staticmethod
    def remove_app():
        """Remove an app from the device"""
        AppiumBase.driver.remove_app(AppiumBase.__app)

    @staticmethod
    def close_driver():
        """Closes the current driver session"""
        if AppiumBase.driver is not None:
            AppiumBase.driver.quit()
