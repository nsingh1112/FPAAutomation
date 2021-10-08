import os
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver import *
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager


class SeleniumBase:
    # region Class Variable Declarations
    __config = None
    __browser = None
    __environment = None
    __url = None
    __headless = None
    __webdrivermanager = None
    driver = None
    current_working_directory = os.path.dirname(os.getcwd())
    configfile = current_working_directory + '\\Shell_FE_Behave_Tests\\config.ini'
    __webdriver_executables = current_working_directory + '\\Shell_FE_Behave_Tests\\WebDriverExecutables\\'

    # endregion

    # def __init__(self):
    #     print("Constructor")

    # region Reading data from Configuration files and initializing values to Class variables
    @staticmethod
    def read_config():
        configuration = ConfigParser()
        configuration.read(SeleniumBase.configfile)
        return configuration

    @staticmethod
    def initialize_values():
        SeleniumBase.__config = SeleniumBase.read_config()
        SeleniumBase.__browser = SeleniumBase.__config['browser']['browser_name']
        SeleniumBase.__webdrivermanager = SeleniumBase.__config.getboolean('browser', 'webdriver_manager')
        SeleniumBase.__url = SeleniumBase.__config['application']['qa_url']

    # endregion

    # region Browser Initialization methods
    @staticmethod
    def browser_initialization():
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
            # Throw an exception
            # Include logging
        SeleniumBase.driver.maximize_window()
        return SeleniumBase.driver

    @staticmethod
    def __chrome_initialization():
        if SeleniumBase.__webdrivermanager:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            return driver
        else:
            chromedrivername = "chromedriver.exe"
            driver = webdriver.Chrome(executable_path=SeleniumBase.__webdriver_executables + chromedrivername)
            return driver

    @staticmethod
    def __firefox_initialization():
        driver = webdriver.Firefox(executable_path=GeckoDriverManager.install())
        return driver

    @staticmethod
    def __ie_initialization():
        driver = webdriver.ie(IEDriverManager.install())
        return driver

    @staticmethod
    def __edge_initialization():
        driver = webdriver.Edge(EdgeChromiumDriverManager.install())
        return driver
    # endregion

