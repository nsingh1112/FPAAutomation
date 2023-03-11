import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.EnteredInDEXPageControls import \
    EnteredInDEXPageControls
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.FailedReconciliationPageControls import \
    FailedReconciliationPageControls
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.FailedToEnteredInDEXPageControls import \
    FailedToEnteredInDEXPageControls
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


class FailedToEnteredInDEXPageFunctions:
    FOB_DES_TestData = None

    def __init__(self, driver):
        self.driver = driver
        self.failedToEnteredInDEXPageControls = FailedToEnteredInDEXPageControls(SeleniumBase.driver)
        self.calendarPageFunctions = CalendarPageFunctions(SeleniumBase.driver)
        self.commonPageFunctions = CommonPageFunctions(SeleniumBase.driver)
        self.FOB_DES_TestData = FileUtilities.read_json_file_as_dictionary("FSPTestData.json")

    def validate_FailedToEnterInDExPageTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.failedToEnteredInDEXPageControls.get_failedToEnteredInDEXPageTitle())
        if FPASeleniumHelper.check_element_exists_by_xpath( self.failedToEnteredInDEXPageControls.get_failedToEnteredInDEXPageTitle()):
            SeleniumUtilities.log.info("Failed To Enter In DEX Page title is correct")

        else:
            SeleniumUtilities.log.error("Failed To Enter In DEX Page title is not correct")

    def get_failedToEnterInDEXDataRowHeaders(self):
        WaitUtilities.wait_for_element_to_be_visible(self.failedToEnteredInDEXPageControls.get_failedToEnteredInDEXRowHeader())
        options1 = self.failedToEnteredInDEXPageControls.get_failedToEnteredInDEXRowHeader()
        CommonRowPageFunctions.validate_rowHeader(self, options1)

    def verify_failedToEnterInDEXDataFields(self):
        WaitUtilities.wait_for_element_to_be_visible(self.failedToEnteredInDEXPageControls.get_failedToEnteredInDEXRowHeader())
        isbolDateLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.failedToEnteredInDEXPageControls.get_errorLogsDateRangeLabel())
        isfinishDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.failedToEnteredInDEXPageControls.get_finishDateInputBox())
        isstartDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.failedToEnteredInDEXPageControls.get_startDateInputBox())
        isstatus = FPASeleniumHelper.check_element_exists_by_xpath(self.failedToEnteredInDEXPageControls.get_status())
        issearchByTextLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.failedToEnteredInDEXPageControls.get_searchByTextLabel())
        issearchByTextCriteriaLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.failedToEnteredInDEXPageControls.get_searchByTextCriteriaLabel())
        if(isbolDateLabel and isstartDateInputBox and isfinishDateInputBox and isstatus
                and issearchByTextLabel and issearchByTextCriteriaLabel):
            SeleniumUtilities.log.info("Failed  To Enter In DEX Data Fields Verified")
        else:
            SeleniumUtilities.log.error("Failed To Enter In DEX Data Fields not Verified")

    def enter_receivedDate(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.failedToEnteredInDEXPageControls.get_startDateInputBox())
        time.sleep(2)
        FPASeleniumHelper.click_element(self.failedToEnteredInDEXPageControls.get_startDateInputBox())
        startDate = self.FOB_DES_TestData['FailedReconciliationStartDate']
        finishDate = self.FOB_DES_TestData['FailedReconciliationFinishDate']
        time.sleep(2)
        self.calendarPageFunctions.click_calendarDate(startDate, finishDate)


    def get_validateContractID(self,expcontractID):
        time.sleep(2)
        WaitUtilities.wait_for_element_to_be_visible(self.failedToEnteredInDEXPageControls.get_contractID())
        actcontractID = self.failedToEnteredInDEXPageControls.get_contractID().text
        if(expcontractID in actcontractID):
            SeleniumUtilities.log.info("Contract ID Verified")
        else:
            SeleniumUtilities.log.error("Contract ID not Verified")

    def get_enterContractID(self):
        WaitUtilities.wait_for_element_to_be_visible(self.failedToEnteredInDEXPageControls.get_contractID())
        actcontractID = self.failedToEnteredInDEXPageControls.get_contractID().text
        FPASeleniumHelper.click_element(self.failedToEnteredInDEXPageControls.get_searchInputText())
        FPASeleniumHelper.send_text_by_actions(self.failedToEnteredInDEXPageControls.get_searchInputText(),actcontractID)
        time.sleep(2)
        return actcontractID