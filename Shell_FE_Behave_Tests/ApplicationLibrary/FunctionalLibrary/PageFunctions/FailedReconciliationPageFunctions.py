import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.FailedReconciliationPageControls import \
    FailedReconciliationPageControls
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


class FailedReconciliationPageFunctions:
    FOB_DES_TestData = None

    def __init__(self, driver):
        self.driver = driver
        self.failedReconciliationPageControls = FailedReconciliationPageControls(SeleniumBase.driver)
        self.calendarPageFunctions = CalendarPageFunctions(SeleniumBase.driver)
        self.commonPageFunctions = CommonPageFunctions(SeleniumBase.driver)
        self.FOB_DES_TestData = FileUtilities.read_json_file_as_dictionary("FSPTestData.json")

    def validate_pageTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.failedReconciliationPageControls.get_failedReconciliationPageTitle())
        if FPASeleniumHelper.check_element_exists_by_xpath( self.failedReconciliationPageControls.get_failedReconciliationPageTitle()):
            SeleniumUtilities.log.info("Failed Reconciliation Page title is correct")

        else:
            SeleniumUtilities.log.error("Failed Reconciliation Page title is not correct")

    def get_failedReconciliationDataRowHeaders(self):
        WaitUtilities.wait_for_element_to_be_visible(
            self.failedReconciliationPageControls.get_failedReconciliationRowHeader())
        options1 = self.failedReconciliationPageControls.get_failedReconciliationRowHeader()
        CommonRowPageFunctions.validate_rowHeader(self, options1)

    def verify_failedReconciliationDataFields(self):
        WaitUtilities.wait_for_element_to_be_visible(self.failedReconciliationPageControls.get_failedReconciliationRowHeader())
        isget_errorLogDateRangeLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.failedReconciliationPageControls.get_errorLogDateRangeLabel())
        isfinishDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.failedReconciliationPageControls.get_finishDateInputBox())
        isstartDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.failedReconciliationPageControls.get_startDateInputBox())
        isstatusLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.failedReconciliationPageControls.get_statusLabel())
        issearchByTextLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.failedReconciliationPageControls.get_searchByTextLabel())
        issearchByTextCriteriaLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.failedReconciliationPageControls.get_searchByTextCriteriaLabel())
        if(isget_errorLogDateRangeLabel and isstartDateInputBox and isfinishDateInputBox and isstatusLabel and issearchByTextLabel and issearchByTextCriteriaLabel):
            SeleniumUtilities.log.info("Failed Reconciliation Data Fields Verified")
        else:
            SeleniumUtilities.log.error("Failed Reconciliation Data Fields not Verified")

    def enter_receivedDate(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.failedReconciliationPageControls.get_startDateInputBox())
        time.sleep(2)
        FPASeleniumHelper.click_element(self.failedReconciliationPageControls.get_startDateInputBox())
        startDate = self.FOB_DES_TestData['FailedReconciliationStartDate']
        finishDate = self.FOB_DES_TestData['FailedReconciliationFinishDate']
        time.sleep(2)
        self.calendarPageFunctions.click_calendarDate(startDate, finishDate)