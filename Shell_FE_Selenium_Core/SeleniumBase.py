import json
import os
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from msedge.selenium_tools import Edge, EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager


class SeleniumBase:
    """SeleniumBase class contains functions for reading config file, browser initiation"""
    # region Class Variable Declarations
    __config = None
    __browser = None
    __webdrivermanager = None
    __implicitwait = None
    __opts = None
    __environment = None
    __headless = None
    __incognito = None
    __acceptcerts = None
    __extensions = None
    __notifications = None
    __insecure_content = None
    __disable_popup = None
    __remote_exe = None
    __remote_environment = None
    driver = None
    url = None
    diff_app = None
    current_working_directory = os.path.dirname(os.getcwd())
    configfile = current_working_directory + '/Shell_FE_Behave_Tests/behave.ini'
    browserstack_config = current_working_directory + '/Shell_FE_Behave_Tests/browserstack.json'
    __webdriver_executables = current_working_directory + '/Shell_FE_Behave_Tests/WebDriverExecutables/'
    TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

    # endregion

    # region Reading data from Configuration files and initializing values to Class variables
    @staticmethod
    def read_config():
        """Reads behave.ini file present in Shell_FE_Behave_Tests folder.

        Returns:
                An instance of ConfigParser.
        """
        configuration = ConfigParser()
        configuration.read(SeleniumBase.configfile)
        return configuration

    @staticmethod
    def initialize_values():
        """Assigns respective values to class variables from behave.ini file.
        """
        SeleniumBase.__config = SeleniumBase.read_config()
        SeleniumBase.__browser = SeleniumBase.__config['browser']['browser_name']
        SeleniumBase.__webdrivermanager = SeleniumBase.__config.getboolean('browser', 'webdriver_manager')
        SeleniumBase.__implicitwait = SeleniumBase.__config['timeout']['implicit_wait']
        environment = SeleniumBase.__config['application']['environment']
        # region Application url initialization
        if environment == "dev":
            SeleniumBase.url = SeleniumBase.__config['application']['dev_url']
        elif environment == "qa":
            SeleniumBase.url = SeleniumBase.__config['application']['qa_url']
        elif environment == "stage":
            SeleniumBase.url = SeleniumBase.__config['application']['stage_url']
        elif environment == "prod":
            SeleniumBase.url = SeleniumBase.__config['application']['prod_url']
        else:
            print("Invalid environment name provided in INI file. Environment: {0}.".format(environment))
        # endregion
        # region Browser options initialization
        SeleniumBase.__headless = SeleniumBase.__config.getboolean('browser-options', 'headless')
        SeleniumBase.__incognito = SeleniumBase.__config.getboolean('browser-options', 'incognito')
        SeleniumBase.__acceptcerts = SeleniumBase.__config.getboolean('browser-options', 'accept_cert')
        SeleniumBase.__extensions = SeleniumBase.__config.getboolean('browser-options', 'disable_extensions')
        SeleniumBase.__notifications = SeleniumBase.__config.getboolean('browser-options', 'disable_notifications')
        SeleniumBase.__insecure_content = SeleniumBase.__config.getboolean('browser-options', 'allow_insecure_content')
        SeleniumBase.__disable_popup = SeleniumBase.__config.getboolean('browser-options', 'disable_popup')
        # endregion
        SeleniumBase.__remote_exe = SeleniumBase.__config.getboolean('browser', 'remote')
        SeleniumBase.__remote_environment = SeleniumBase.__config['browser']['remote_environment']

    # endregion

    # region WebDriver Initialization and dispose methods
    @staticmethod
    def browser_initialization():
        """Initializes browser based on the value passed in behave.ini file and assigns the respective driver to
        the class variable 'driver'.

        Raises:
            An exception if an invalid browser name is provided in behave.ini file

        Returns:
            Class variable 'driver' present in SeleniumBase
        """
        browsername = str(SeleniumBase.__browser).upper()
        if SeleniumBase.__remote_exe is False:
            if browsername == "CHROME":
                SeleniumBase.driver = SeleniumBase.__chrome_initialization()
            elif browsername == "FIREFOX":
                SeleniumBase.driver = SeleniumBase.__firefox_initialization()
            elif browsername == "IE":
                SeleniumBase.driver = SeleniumBase.__ie_initialization()
            elif browsername == "EDGE":
                SeleniumBase.driver = SeleniumBase.__edge_initialization()
            elif browsername == "SAFARI":
                SeleniumBase.driver = SeleniumBase.__safari_initialization()
            else:
                print("Invalid browser!!")
                raise Exception("Invalid Browser name passed. Aborting the UI tests!!")
        elif SeleniumBase.__remote_exe is True:
            remote_environment = str(SeleniumBase.__remote_environment).upper()
            if remote_environment == "BROWSERSTACK":
                SeleniumBase.driver = SeleniumBase.__browserstack_initialization()
        SeleniumBase.driver.implicitly_wait(int(SeleniumBase.__implicitwait))

    @staticmethod
    def __chrome_initialization():
        """Initializes driver to ChromeDriver. Based on value in behave.ini file WebDriver Manager or
        WebDriver binary would be used.

        Returns:
            ChromeDriver instance
        """
        SeleniumBase.__opts = webdriver.ChromeOptions()
        # capability = DesiredCapabilities.CHROME.copy()
        SeleniumBase.set_options(SeleniumBase.__opts)

        if SeleniumBase.__webdrivermanager:
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=SeleniumBase.__opts)
            return driver
        else:
            try:
                chromedrivername = "chromedriver"
                driver = webdriver.Chrome(executable_path=SeleniumBase.__webdriver_executables + chromedrivername,
                                          options=SeleniumBase.__opts)
                return driver
            except Exception as err:
                raise Exception(err)

    @staticmethod
    def __firefox_initialization():
        """Initializes driver to FirefoxDriver. Based on value in behave.ini file WebDriver Manager or
        WebDriver binary would be used.

            Returns:
                FirefoxDriver instance
        """
        SeleniumBase.__opts = webdriver.FirefoxOptions()
        SeleniumBase.set_options(SeleniumBase.__opts)

        if SeleniumBase.__webdrivermanager:
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=SeleniumBase.__opts)
            return driver
        else:
            try:
                geckodrivername = "geckodriver"
                driver = webdriver.Firefox(executable_path=SeleniumBase.__webdriver_executables + geckodrivername,
                                           options=SeleniumBase.__opts)
                return driver
            except Exception as err:
                raise Exception(err)

    @staticmethod
    def __edge_initialization():
        """Initializes driver to EdgeDriver. Based on value in behave.ini file WebDriver Manager or
        WebDriver binary would be used.

            Returns:
                Edgedriver instance
        """
        SeleniumBase.__opts = EdgeOptions()
        SeleniumBase.__opts.use_chromium = True
        SeleniumBase.set_options(SeleniumBase.__opts)

        if SeleniumBase.__webdrivermanager:
            driver = Edge(EdgeChromiumDriverManager().install(), options=SeleniumBase.__opts)
            return driver
        else:
            try:
                edgedrivername = "msedgedriver"
                # driver = webdriver.Edge(executable_path=SeleniumBase.__webdriver_executables + edgedrivername)
                driver = Edge(executable_path=SeleniumBase.__webdriver_executables + edgedrivername,
                              options=SeleniumBase.__opts)
                return driver
            except Exception as err:
                raise Exception(err)

    @staticmethod
    def __safari_initialization():
        """Initializes driver to Safari driver.
            Returns:
                  Safari driver instance
        """
        driver = webdriver.Safari()
        return driver

    @staticmethod
    def set_options(browser_options):
        opts = browser_options
        opts.headless = SeleniumBase.__headless
        opts.set_capability("acceptInsecureCerts", SeleniumBase.__acceptcerts)
        if SeleniumBase.__incognito:
            if str(SeleniumBase.__browser).upper() == "CHROME":
                opts.add_argument("--incognito")
            if str(SeleniumBase.__browser).upper() == "EDGE":
                opts.add_argument("-inprivate")
            if str(SeleniumBase.__browser).upper() == "FIREFOX":
                opts.add_argument("-private")
        if SeleniumBase.__extensions:
            opts.add_argument("--disable-extensions")
        if SeleniumBase.__notifications:
            opts.add_argument("--disable-notifications")
        if SeleniumBase.__insecure_content:
            opts.add_argument("--allow-running-insecure-content")
            opts.add_argument("--ignore-certificate-errors")
        if SeleniumBase.__disable_popup:
            opts.add_argument("--disable-popup-blocking")

    @staticmethod
    def __browserstack_initialization():
        """Initializes driver to remote webdriver with Browserstack based on the value provided in 'remote_environment'
         in Behave.INI file.

            Returns:
                Remote webdriver instance with Browserstack.
        """
        with open(SeleniumBase.browserstack_config) as config_file:
            config = json.load(config_file)

        username = config['user']
        accesskey = config['key']
        server = config['webServer']

        capabilities = config['webEnvironments'][SeleniumBase.TASK_ID]
        driver = webdriver.Remote(command_executor='https://{0}:{1}@{2}/wd/hub'.format(username, accesskey, server),
                                      desired_capabilities=capabilities)
        return driver

    @staticmethod
    def dispose():
        """Terminates all instances of WebDriver."""
        if SeleniumBase.driver is not None:
            SeleniumBase.driver.quit()
        # Enter code for closing the driver based on local or remote
    # endregion
