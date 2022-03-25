import json
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
    __remoteURL = None
    __browser_name = None
    __application_type = None
    __automation_name = None
    __remote_exe = None
    __remote_environment = None
    __implicitwait = None
    devicePlatform = None
    app = None
    udid = None
    bundle_id = None
    appPackage = None
    appActivity = None
    driver = None
    noReset = None
    appPathFlag = None
    bundleIdPath = None
    appPackageFlag = None
    __parallel = None
    current_working_directory = os.path.dirname(os.getcwd())
    configfile = current_working_directory + '/Shell_FE_Behave_Tests/behave.ini'
    app_browserstack_config = current_working_directory + '/Shell_FE_Behave_Tests/browserstack.json'
    TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0
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
        AppiumBase.__implicitwait = AppiumBase.__config['timeout']['implicit_wait']
        # BrowserStack value initialization
        AppiumBase.__remote_exe = AppiumBase.__config.getboolean('MobilityCloudIntegration', 'remote')
        AppiumBase.__remote_environment = AppiumBase.__config['MobilityCloudIntegration']['remote_environment']

        if AppiumBase.devicePlatform.lower() == "android":
            AppiumBase.__platformName = AppiumBase.__config['Android']['platformName']
            AppiumBase.__platformVersion = AppiumBase.__config['Android']['platformVersion']
            AppiumBase.__deviceName = AppiumBase.__config['Android']['deviceName']
            AppiumBase.app = AppiumBase.__config['Android']['appPath']
            AppiumBase.appPackage = AppiumBase.__config['Android']['appPackage']
            AppiumBase.appActivity = AppiumBase.__config['Android']['appActivity']
            AppiumBase.__remoteURL = AppiumBase.__config['Android']['remoteURL']
            AppiumBase.__application_type = AppiumBase.__config['Android']['applicationType']
            AppiumBase.__automation_name = AppiumBase.__config['Android']['automationName']
            AppiumBase.__browser_name = AppiumBase.__config['Android']['browserName']
            AppiumBase.appPathFlag = AppiumBase.__config.getboolean('Android', 'runAppWithPath')
            AppiumBase.appPackageFlag = AppiumBase.__config.getboolean('Android', 'runAppWithPackage')

        elif AppiumBase.devicePlatform.lower() == "ios":
            AppiumBase.__application_type = AppiumBase.__config['iOS']['applicationType']
            AppiumBase.__platformName = AppiumBase.__config['iOS']['platformName']
            AppiumBase.__platformVersion = AppiumBase.__config['iOS']['platformVersion']
            AppiumBase.__deviceName = AppiumBase.__config['iOS']['deviceName']
            AppiumBase.udid = AppiumBase.__config['iOS']['udid']
            AppiumBase.bundle_id = AppiumBase.__config['iOS']['bundleId']
            AppiumBase.app = AppiumBase.__config['iOS']['appPath']
            AppiumBase.__remoteURL = AppiumBase.__config['iOS']['remoteURL']
            AppiumBase.__automation_name = AppiumBase.__config['iOS']['automationName']
            AppiumBase.__browser_name = AppiumBase.__config['iOS']['browserName']
            AppiumBase.noRest = AppiumBase.__config.getboolean('iOS', 'noReset')
            AppiumBase.appPathFlag = AppiumBase.__config.getboolean('iOS', 'runAppWithPath')
            AppiumBase.bundleIdPath = AppiumBase.__config.getboolean('iOS', 'runAppWithBundleId')

    # endregion

    # region Launch Application
    @staticmethod
    def launch_application(device_type=None):
        """Launches the Application
           Returns the driver instance
        """
        if device_type is None:
            AppiumBase.__config = AppiumBase.read_config()
            AppiumBase.devicePlatform = AppiumBase.__config['automationplatform']['platformtype']
            AppiumBase.read_values()

        elif device_type.lower() == "android":
            AppiumBase.devicePlatform = "android"
            AppiumBase.read_values()
        elif device_type.lower() == "ios":
            AppiumBase.devicePlatform = "ios"
            AppiumBase.read_values()

        desired_caps = {'platformName': AppiumBase.__platformName,
                        'platformVersion': AppiumBase.__platformVersion,
                        'deviceName': AppiumBase.__deviceName,
                        'automationName': AppiumBase.__automation_name,
                        }

        if AppiumBase.__remote_exe is False:

            if AppiumBase.__application_type.lower() == "native" or AppiumBase.__application_type.lower() == "hybrid":
                if AppiumBase.devicePlatform.lower() == "android":
                    if AppiumBase.appPackageFlag is True:
                        desired_caps['appPackage'] = AppiumBase.appPackage
                        desired_caps['appActivity'] = AppiumBase.appActivity

                    if AppiumBase.appPathFlag is True:
                        desired_caps['app'] = AppiumBase.app

                elif AppiumBase.devicePlatform.lower() == "ios":
                    desired_caps['udid'] = AppiumBase.udid

                    if AppiumBase.bundleIdPath is True:
                        desired_caps['bundleId'] = AppiumBase.bundle_id
                    if AppiumBase.appPathFlag is True:
                        desired_caps['app'] = AppiumBase.app
                    if AppiumBase.noReset is True:
                        desired_caps['app'] = AppiumBase.app

            elif AppiumBase.__application_type.lower() == "webbrowser":
                desired_caps['browserName'] = AppiumBase.__browser_name

            AppiumBase.driver = webdriver.Remote(AppiumBase.__remoteURL, desired_capabilities=desired_caps)
        elif AppiumBase.__remote_exe is True:
            remote_environment = str(AppiumBase.__remote_environment).upper()
            if remote_environment == "BROWSERSTACK":
                AppiumBase.driver = AppiumBase.__app_browserstack_initialization()
        AppiumBase.driver.implicitly_wait(int(AppiumBase.__implicitwait))

    # endregion

    @staticmethod
    def install_app():
        """Install the App in the device"""
        AppiumBase.driver.install_app(AppiumBase.app)

    @staticmethod
    def is_App_installed():
        """Checks the app is installed in the device
            Return True- if the application is installed
        """
        app_installed = AppiumBase.driver.is_app_installed(AppiumBase.app)
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
        AppiumBase.driver.remove_app(AppiumBase.app)

    @staticmethod
    def close_driver():
        """Closes the current driver session"""
        if AppiumBase.driver is not None:
            AppiumBase.driver.quit()

    @staticmethod
    def __app_browserstack_initialization():
        with open(AppiumBase.app_browserstack_config) as config_file:
            config = json.load(config_file)

        username = config['user']
        accesskey = config['key']

        server = config['appServer']

        capabilities = config['appCapabilities']
        capabilities['device'] = config['appEnvironments'][AppiumBase.TASK_ID]['device']
        driver = webdriver.Remote(
            command_executor='http://{0}:{1}@{2}/wd/hub'.format(username, accesskey, server),
            desired_capabilities=dict(capabilities))
        return driver
