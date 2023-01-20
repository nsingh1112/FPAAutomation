import time

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.FPAHomePageControls import FPAHomePageControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities


class FPAHomePageFunctions:

    def __init__(self):
        self.fpaHomePageControls = FPAHomePageControls(SeleniumBase.driver)

    def click_invoices(self):
        WaitUtilities.wait_for_element_to_be_visible(self.fpaHomePageControls.get_invoices())
        WaitUtilities.wait_for_element_to_be_clickable(self.fpaHomePageControls.get_invoices())
        SeleniumUtilities.click_element(self.fpaHomePageControls.get_invoices())
        time.sleep(15)

    def navigate_to_url(self, url):
        BrowserUtilities.navigate_to_url(url)

    def click_pdfLink(self):
        time.sleep(15)
        WaitUtilities.wait_for_element_to_be_visible(self.fpaHomePageControls.get_pdfLink())
        WaitUtilities.wait_for_element_to_be_clickable(self.fpaHomePageControls.get_pdfLink())
        SeleniumUtilities.click_element(self.fpaHomePageControls.get_pdfLink())
        time.sleep(15)

