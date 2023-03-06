import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.ReconciliationPageControls import \
    ReconciliationPageControls
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonRowPageFunctions import \
    CommonRowPageFunctions
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper

class ReconcilationPageFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.reconciliationPageControls = ReconciliationPageControls(SeleniumBase.driver)


    def validate_unprocessedRecordPageTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.reconciliationPageControls.get_unprocessedRecordPageTitle())
        if FPASeleniumHelper.check_element_exists_by_xpath( self.reconciliationPageControls.get_unprocessedRecordPageTitle()):
            SeleniumUtilities.log.info("Unprocessed Record Page title is correct")

        else:
            SeleniumUtilities.log.error("Unprocessed Record Page title is not correct")

    def validate_reconciledDataPageTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.reconciliationPageControls.get_reconciledDataPageTitle())
        if FPASeleniumHelper.check_element_exists_by_xpath(self.reconciliationPageControls.get_reconciledDataPageTitle()):
            SeleniumUtilities.log.info("Reconciled Data Page title is correct")

        else:
            SeleniumUtilities.log.error("Reconciled Data Page title is not correct")


    def validate_dataRowHeaders(self):
        WaitUtilities.wait_for_element_to_be_visible(self.reconciliationPageControls.get_rowHeader())
        options1 = self.reconciliationPageControls.get_rowHeader()
        CommonRowPageFunctions.validate_rowHeader(self, options1)

    def verify_dataFields(self):
        WaitUtilities.wait_for_element_to_be_visible(self.reconciliationPageControls.get_rowHeader())
        isreceivedDateLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciliationPageControls.get_receivedDateLabel())
        isfinishDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciliationPageControls.get_finishDateInputBox())
        isstartDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciliationPageControls.get_startDateInputBox())
        issearchByTextLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciliationPageControls.get_searchByTextLabel())
        issearchByTextCriteriaLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciliationPageControls.get_searchByTextCriteriaLabel())
        issearchInputText = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciliationPageControls.get_searchInputText())

        if(isreceivedDateLabel and isstartDateInputBox and isfinishDateInputBox and issearchByTextLabel and issearchByTextCriteriaLabel and issearchInputText):
            SeleniumUtilities.log.info("Data Fields Verified")
        else:
            SeleniumUtilities.log.error("Data Fields not Verified")








