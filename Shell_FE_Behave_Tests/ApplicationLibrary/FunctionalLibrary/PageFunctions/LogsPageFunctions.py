import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.LogsPageControls import LogsPageControls
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonRowPageFunctions import \
    CommonRowPageFunctions
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper

class LogsPageFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.logsPageControls = LogsPageControls(SeleniumBase.driver)


    def validate_reconciliationPageTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.logsPageControls.get_reconciliationPageTitle())
        if (FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_reconciliationPageTitle())):
            SeleniumUtilities.log.info("Reconciliation Page title is correct")
        else:
            SeleniumUtilities.log.error("Reconciliation Page title is not correct")


    def validate_reconciliationErrorPageTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.logsPageControls.get_reconciliationErrorsPageTitle())
        if (FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_reconciliationErrorsPageTitle())):
            SeleniumUtilities.log.info("Reconciliation Error Page title is correct")
        else:
            SeleniumUtilities.log.error("Reconciliation Error Page title is not correct")

    def validate_actualsErrorsPageTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.logsPageControls.get_actualsErrorsPageTitle())
        if (FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_actualsErrorsPageTitle())):
            SeleniumUtilities.log.info("Actuals Errors Page title is correct")
        else:
            SeleniumUtilities.log.error("Actuals Errors Page title is not correct")


    def validate_dataRowHeaders(self):
        WaitUtilities.wait_for_element_to_be_visible(self.logsPageControls.get_rowHeader())
        options1 = self.logsPageControls.get_rowHeader()
        CommonRowPageFunctions.validate_rowHeader(self, options1)

    def verify_dataFields(self):
        WaitUtilities.wait_for_element_to_be_visible(self.logsPageControls.get_rowHeader())
        #isBOLDateLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_bolDateLabel())
        isfinishDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_finishDateInputBox())
        isstartDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_startDateInputBox())
        issearchByTextLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_searchByTextLabel())
        #issearchByTextCriteriaLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_searchByTextCriteriaLabel())
        issearchInputText = FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_searchInputText())

        if(isstartDateInputBox and isfinishDateInputBox and issearchByTextLabel and issearchInputText):
            SeleniumUtilities.log.info("Data Fields Verified")
        else:
            SeleniumUtilities.log.error("Data Fields not Verified")

    def verify_searchByTextCriteria(self, actualProcessingItems):
        WaitUtilities.wait_for_element_to_be_visible(self.logsPageControls.get_rowHeader())
        if (actualProcessingItems == "Reconciliation"):
            isReceivedDateLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_receivedDateLabel())
            isSearchByTextLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_reconciliationSearchByTextLabel())
            if (isReceivedDateLabel and isSearchByTextLabel):
               SeleniumUtilities.log.info("Reconciliation Search Criteria Verified")
            else:
                SeleniumUtilities.log.error("Reconciliation Search Criteria not Verified")
        elif (actualProcessingItems == "Reconciliation Errors"):
            isErrorLogsDateRangeLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_errorLogDateRangeLabel())
            isSearchByTextLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_reconciliationErrorsSearchByTextLabel())
            if (isErrorLogsDateRangeLabel and isSearchByTextLabel):
               SeleniumUtilities.log.info("Reconciliation Errors Search Criteria Verified")
            else:
               SeleniumUtilities.log.error("Reconciliation Errors Search Criteria not Verified")
        else:
            isErrorLogsDateRangeLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_errorLogDateRangeLabel())
            isSearchByTextLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.logsPageControls.get_actualErrorsSearchByTextLabel())
            if (isErrorLogsDateRangeLabel and isSearchByTextLabel):
                SeleniumUtilities.log.info("Actuals Errors Search Criteria Verified")
            else:
                SeleniumUtilities.log.error("Actuals Errors Search Criteria not Verified")






