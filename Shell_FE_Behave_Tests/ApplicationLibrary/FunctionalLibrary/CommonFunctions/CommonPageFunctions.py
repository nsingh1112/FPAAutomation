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
        WaitUtilities.wait_for_element_to_be_clickable(self.commonPageControls.get_Homepage(), 12000)
        FPASeleniumHelper.click_element(self.commonPageControls.get_Homepage())

    def select_Status(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.commonPageControls.get_statusInputBox())
        FPASeleniumHelper.click_element(self.commonPageControls.get_statusInputBox())
        WaitUtilities.wait_for_element_to_be_clickable(self.commonPageControls.get_status())
        FPASeleniumHelper.click_element(self.commonPageControls.get_status())

    def click_search(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.commonPageControls.get_searchButton())
        FPASeleniumHelper.click_element(self.commonPageControls.get_searchButton())

    def click_Clear(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.commonPageControls.get_clearSearchButton())
        FPASeleniumHelper.click_element(self.commonPageControls.get_clearSearchButton())

    def select_DocumentType(self, docType):
        WaitUtilities.wait_for_element_to_be_clickable(self.commonPageControls.get_getDocumentInputBox())
        FPASeleniumHelper.click_element(self.commonPageControls.get_getDocumentInputBox())
        #filetype = (fileName.split('.'))[1].upper()
        documentType = self.driver.find_element_by_xpath(
            "//div[@class='shell-select-container-item-option-content' and text()='" + str(docType) + "']")
        WaitUtilities.wait_for_element_to_be_clickable(documentType)
        FPASeleniumHelper.click_element(documentType)

    def get_totalNoOfRecords(self):
        time.sleep(2)
        WaitUtilities.wait_for_element_to_be_visible(self.commonPageControls.get_totalRecordsCount())
        totalRecordCount = int(((self.commonPageControls.get_totalRecordsCount().text).split(' '))[0])
        return totalRecordCount

    def get_receivedStartDateEndDate(self, options1):
        elementList = []
        for option in options1:
            x2 = option.text
            if ((len(elementList) <= 1) and (x2 not in elementList)):
                elementList.append(x2)

        earliest_date = min(elementList)
        lastest_date = max(elementList)

        return earliest_date, lastest_date

    def wait_forToastToDisable(self):
        WaitUtilities.wait_for_element_to_be_invisible(self.commonPageControls.get_toastMessageDiv(),20000)




