import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.UnprocessedRecordsPageControls import \
    UnprocessedRecordsPageControls
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonRowPageFunctions import \
    CommonRowPageFunctions
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper


class UnprocessedRecordsPageFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.unprocessedRecordsPageControls = UnprocessedRecordsPageControls(SeleniumBase.driver)

    def validate_pageTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.unprocessedRecordsPageControls.get_unprocessedRecordPageTitle(), 6000)
        if FPASeleniumHelper.check_element_exists_by_xpath( self.unprocessedRecordsPageControls.get_unprocessedRecordPageTitle()):
            SeleniumUtilities.log.info("Unprocessed Record Page title is correct")

        else:
            SeleniumUtilities.log.error("Unprocessed Record Page title is not correct")

    def get_totalUnprocessedRecord(self):
        WaitUtilities.wait_for_element_to_be_visible(self.unprocessedRecordsPageControls.get_totalUnprocessedRecord())
        totalRecordText = self.unprocessedRecordsPageControls.get_totalUnprocessedRecord().text
        if(" Unprocessed records" in totalRecordText):
            totalRecordCount = int(((self.unprocessedRecordsPageControls.get_totalUnprocessedRecord().text).split(' '))[0])
            if (totalRecordCount >= 0):
                SeleniumUtilities.log.info("Total Record Count is greater than zero")
            else:
                SeleniumUtilities.log.info("Total Record Count is less than or equal to zero")
        else:
            SeleniumUtilities.log.error("Unprocessed Record Count is missing")

    def get_unprocessedRecordRowHeaders(self):
        WaitUtilities.wait_for_element_to_be_visible(
            self.unprocessedRecordsPageControls.get_unprocessedRecordRowHeader())
        options1 = self.unprocessedRecordsPageControls.get_unprocessedRecordRowHeader()
        CommonRowPageFunctions.validate_rowHeader(self, options1)