import time

from selenium.webdriver.support.select import Select

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.CommonControls.CommonPageControls import CommonPageControls
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper
from Shell_FE_Behave_Tests.Utilities.FPAWaitHelper import FPAWaitHelper
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

class CommonPageFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.commonPageControls = CommonPageControls(SeleniumBase.driver)

    def click_Homepage(self):
        FPAWaitHelper.wait_for_element_to_be_clickable(self.commonPageControls.get_Homepage(), 600)
        FPASeleniumHelper.click_element(self.commonPageControls.get_Homepage())
        time.sleep(7)

    def select_Status(self):
        FPAWaitHelper.wait_for_element_to_be_clickable(self.commonPageControls.get_statusInputBox(), 600)
        FPASeleniumHelper.click_element(self.commonPageControls.get_statusInputBox())
        FPAWaitHelper.wait_for_element_to_be_clickable(self.commonPageControls.get_status(), 1000)
        FPASeleniumHelper.click_element(self.commonPageControls.get_status())
        time.sleep(1000)


