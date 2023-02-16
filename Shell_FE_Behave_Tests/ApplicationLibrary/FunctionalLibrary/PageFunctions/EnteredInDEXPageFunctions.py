import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.EnteredInDEXPageControls import \
    EnteredInDEXPageControls
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


class EnteredInDEXPageFunctions:
    FOB_DES_TestData = None

    def __init__(self, driver):
        self.driver = driver
        self.enteredInDEXPageControls = EnteredInDEXPageControls(SeleniumBase.driver)
        self.calendarPageFunctions = CalendarPageFunctions(SeleniumBase.driver)
        self.commonPageFunctions = CommonPageFunctions(SeleniumBase.driver)
        self.FOB_DES_TestData = FileUtilities.read_json_file_as_dictionary("FSPTestData.json")

    def validate_pageTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.enteredInDEXPageControls.get_enteredInDEXPageTitle())
        if FPASeleniumHelper.check_element_exists_by_xpath( self.enteredInDEXPageControls.get_enteredInDEXPageTitle()):
            SeleniumUtilities.log.info("Entered In DEX Page title is correct")

        else:
            SeleniumUtilities.log.error("Entered In DEX Page title is not correct")

    def get_enteredInDEXDataRowHeaders(self):
        WaitUtilities.wait_for_element_to_be_visible(self.enteredInDEXPageControls.get_enteredInDEXRowHeader())
        options1 = self.enteredInDEXPageControls.get_enteredInDEXRowHeader()
        CommonRowPageFunctions.validate_rowHeader(self, options1)

    def verify_enteredInDEXDataFields(self):
        WaitUtilities.wait_for_element_to_be_visible(self.enteredInDEXPageControls.get_enteredInDEXRowHeader())
        isbolDateLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.enteredInDEXPageControls.get_bolDateLabel())
        isfinishDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.enteredInDEXPageControls.get_finishDateInputBox())
        isstartDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.enteredInDEXPageControls.get_startDateInputBox())
        issearchByTextLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.enteredInDEXPageControls.get_searchByTextLabel())
        issearchByTextCriteriaLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.enteredInDEXPageControls.get_searchByTextCriteriaLabel())
        if(isbolDateLabel and isstartDateInputBox and isfinishDateInputBox
                and issearchByTextLabel and issearchByTextCriteriaLabel):
            SeleniumUtilities.log.info("Entered In DEX Data Fields Verified")
        else:
            SeleniumUtilities.log.error("Entered In DEX Data Fields not Verified")

    def enter_receivedDate(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.enteredInDEXPageControls.get_startDateInputBox())
        time.sleep(2)
        FPASeleniumHelper.click_element(self.enteredInDEXPageControls.get_startDateInputBox())
        startDate = self.FOB_DES_TestData['FailedReconciliationStartDate']
        finishDate = self.FOB_DES_TestData['FailedReconciliationFinishDate']
        time.sleep(2)
        self.calendarPageFunctions.click_calendarDate(startDate, finishDate)