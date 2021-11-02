import os
from configparser import ConfigParser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager


class SeleniumBase:
    """SeleniumBase class contains functions for reading config file, browser initiation"""
    # region Class Variable Declarations
    __config = None
    __browser = None
    __environment = None
    __headless = None
    __webdrivermanager = None
    driver = None
    url = None
    current_working_directory = os.path.dirname(os.getcwd())
    configfile = current_working_directory + '\\Shell_FE_Behave_Tests\\config.ini'
    __webdriver_executables = current_working_directory + '\\Shell_FE_Behave_Tests\\WebDriverExecutables\\'

    # endregion

    # region Reading data from Configuration files and initializing values to Class variables
    @staticmethod
    def read_config():
        """Reads Config.INI file present in Shell_FE_Behave_Tests folder.

        Returns:
                An instance of ConfigParser.
        """
        configuration = ConfigParser()
        configuration.read(SeleniumBase.configfile)
        return configuration

    @staticmethod
    def initialize_values():
        """Assigns respective values to class variables from Config.INI file.
        """
        SeleniumBase.__config = SeleniumBase.read_config()
        SeleniumBase.__browser = SeleniumBase.__config['browser']['browser_name']
        SeleniumBase.__webdrivermanager = SeleniumBase.__config.getboolean('browser', 'webdriver_manager')
        SeleniumBase.url = SeleniumBase.__config['application']['qa_url']

    # endregion

    # region WebDriver Initialization and dispose methods
    @staticmethod
    def browser_initialization():
        """Initializes browser based on the value passed in Config.INI file and assigns the respective driver to
        the class variable 'driver'.

        Raises:
            An exception if an invalid browser name is provided in Config.INI file

        Returns:
            Class variable 'driver' present in SeleniumBase
        """
        browsername = str(SeleniumBase.__browser).upper()

        if browsername == "CHROME":
            SeleniumBase.driver = SeleniumBase.__chrome_initialization()
        elif browsername == "FIREFOX":
            SeleniumBase.driver = SeleniumBase.__firefox_initialization()
        elif browsername == "IE":
            SeleniumBase.driver = SeleniumBase.__ie_initialization()
        elif browsername == "EDGE":
            SeleniumBase.driver = SeleniumBase.__edge_initialization()
        else:
            print("Invalid browser!!")
            raise Exception("Invalid Browser name passed. Aborting the UI tests!!")
            # Include logging
        SeleniumBase.driver.maximize_window()
        SeleniumBase.driver.delete_all_cookies()
        return SeleniumBase.driver

    @staticmethod
    def __chrome_initialization():
        """Initializes driver to ChromeDriver. Based on value in Config.INI file WebDriver Manager or
        WebDriver binary would be used.

        Returns:
            ChromeDriver instance
        """
        if SeleniumBase.__webdrivermanager:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            return driver
        else:
            chromedrivername = "chromedriver.exe"
            driver = webdriver.Chrome(executable_path=SeleniumBase.__webdriver_executables + chromedrivername)
            return driver

    @staticmethod
    def __firefox_initialization():
        """Initializes driver to FirefoxDriver. Based on value in Config.INI file WebDriver Manager or
        WebDriver binary would be used.

            Returns:
                FirefoxDriver instance
        """
        driver = webdriver.Firefox(executable_path=GeckoDriverManager.install())
        return driver

    @staticmethod
    def __ie_initialization():
        """Initializes driver to IEDriver. Based on value in Config.INI file IEDriver Manager or
        WebDriver binary would be used.

            Returns:
                IEDriver instance
        """
        driver = webdriver.ie(IEDriverManager.install())
        return driver

    @staticmethod
    def __edge_initialization():
        """Initializes driver to EdgeDriver. Based on value in Config.INI file WebDriver Manager or
        WebDriver binary would be used.

            Returns:
                Chromedriver instance
        """
        driver = webdriver.Edge(EdgeChromiumDriverManager.install())
        return driver

    @staticmethod
    def dispose():
        """Terminates all instances of WebDriver."""
        if SeleniumBase.driver is not None:
            SeleniumBase.driver.quit()
        # Enter code for closing the driver based on local or remote
    # endregion
