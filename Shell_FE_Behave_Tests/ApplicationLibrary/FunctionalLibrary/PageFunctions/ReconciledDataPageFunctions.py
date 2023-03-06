import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.ReconciledDataPageControls import \
    ReconciledDataPageControls
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CalendarPageFunctions import \
    CalendarPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonPageFunctions import \
    CommonPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonRowPageFunctions import \
    CommonRowPageFunctions
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper
from Shell_FE_Behave_Tests.Utilities.FPAWaitHelper import FPAWaitHelper


class ReconciledDataPageFunctions:
    FOB_DES_TestData = None

    def __init__(self, driver):
        self.driver = driver
        self.reconciledDataPageControls = ReconciledDataPageControls(SeleniumBase.driver)
        self.calendarPageFunctions = CalendarPageFunctions(SeleniumBase.driver)
        self.commonPageFunctions = CommonPageFunctions(SeleniumBase.driver)
        self.FOB_DES_TestData = FileUtilities.read_json_file_as_dictionary("FSPTestData.json")

    def validate_pageTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.reconciledDataPageControls.get_reconciledDataPageTitle())
        if FPASeleniumHelper.check_element_exists_by_xpath( self.reconciledDataPageControls.get_reconciledDataPageTitle()):
            SeleniumUtilities.log.info("Reconciled Data Page title is correct")

        else:
            SeleniumUtilities.log.error("Reconciled Data Page title is not correct")

    def enter_receivedDate(self, dashboardItems,startDate,endDate):
        WaitUtilities.wait_for_element_to_be_clickable(self.reconciledDataPageControls.get_startDateInputBox())
        FPASeleniumHelper.click_element(self.reconciledDataPageControls.get_startDateInputBox())
        time.sleep(2)
        self.calendarPageFunctions.click_calendarDate(startDate, endDate)

    def click_search(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.reconciledDataPageControls.get_searchButton())
        FPASeleniumHelper.click_element(self.reconciledDataPageControls.get_searchButton())

    def click_Clear(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.reconciledDataPageControls.get_clearSearchButton())
        #FPAWaitHelper.wait_for_element_to_be_clickable(self.reconciledDataPageControls.get_clearSearchButton(), 6000)
        FPASeleniumHelper.click_element(self.reconciledDataPageControls.get_clearSearchButton())

    def get_reconciledDataRowHeaders(self):
        WaitUtilities.wait_for_element_to_be_visible(
            self.reconciledDataPageControls.get_reconciledDataRowHeader())
        options1 = self.reconciledDataPageControls.get_reconciledDataRowHeader()
        CommonRowPageFunctions.validate_rowHeader(self, options1)

    def verify_reconciledDataFields(self):
        WaitUtilities.wait_for_element_to_be_visible(self.reconciledDataPageControls.get_reconciledDataRowHeader())
        isreceivedDateLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciledDataPageControls.get_receivedDateLabel())
        isstartDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciledDataPageControls.get_startDateInputBox())
        isstatusLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciledDataPageControls.get_statusLabel())
        issearchByTextLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciledDataPageControls.get_searchByTextLabel())
        issearchByTextCriteriaLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciledDataPageControls.get_searchByTextCriteriaLabel())
        issearchButton = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciledDataPageControls.get_searchButton())
        isclearSearchButton = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciledDataPageControls.get_clearSearchButton())
        if(isreceivedDateLabel and isstartDateInputBox and isstatusLabel and issearchByTextLabel and issearchByTextCriteriaLabel and issearchButton and isclearSearchButton):
            SeleniumUtilities.log.info("Reconciled Data Fields Verified")
        else:
            SeleniumUtilities.log.error("Reconciled Data Fields not Verified")


    def get_receivedStartEndDate(self):
        elementList = []
        WaitUtilities.wait_for_element_to_be_visible(
            self.reconciledDataPageControls.get_receivedDate())
        options1 = self.reconciledDataPageControls.get_receivedDate()
        for option in options1:
            x2 = option.text
            if ((len(elementList) <= 1) and (x2 not in elementList)):
                elementList.append(x2)

        earliest_date = min(elementList)
        lastest_date = max(elementList)

        return earliest_date, lastest_date
