import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.ReconciliationPageControls import \
    ReconciliationPageControls
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonPageFunctions import \
    CommonPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonRowPageFunctions import \
    CommonRowPageFunctions
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper

class ReconcilationPageFunctions:

    FSP_TestData = None
    def __init__(self, driver):
        self.driver = driver
        self.reconciliationPageControls = ReconciliationPageControls(SeleniumBase.driver)
        self.commonPageFunctions = CommonPageFunctions(SeleniumBase.driver)
        self.FSP_TestData = FileUtilities.read_json_file_as_dictionary("FSPTestData.json")

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

    def verify_reconcileUnprocessedRecordsButton(self):
        WaitUtilities.wait_for_element_to_be_visible(self.reconciliationPageControls.get_reconcileUnprocessedRecordsButton())
        FPASeleniumHelper.click_element(self.reconciliationPageControls.get_reconcileUnprocessedRecordsButton())
        isTitle = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciliationPageControls.get_reconcileUnprocessedRecordsPopUpTitle())
        isBody = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciliationPageControls.get_reconcileUnprocessedRecordPopUpBody())
        isCancelBtn = FPASeleniumHelper.check_element_exists_by_xpath(self.reconciliationPageControls.get_reconcileUnprocessedRecordsPopUpCancelBtn())
        isSubmitBtn = FPASeleniumHelper.check_element_exists_by_xpath(
            self.reconciliationPageControls.get_reconcileUnprocessedRecordPopUpSubmitBtn())

        FPASeleniumHelper.click_element(self.reconciliationPageControls.get_reconcileUnprocessedRecordsPopUpCancelBtn())
        if (isTitle and isBody and isCancelBtn and isSubmitBtn):
            SeleniumUtilities.log.info("Reconcile Unprocessed Records Button Fields Verified")
        else:
            SeleniumUtilities.log.error("Reconcile Unprocessed Records Button Fields not Verified")

    def getAndEnter_unprocessedRecordOrderID(self):
        WaitUtilities.wait_for_element_to_be_visible(self.reconciliationPageControls.get_unprocessedRecordOrderID())
        orderID = self.reconciliationPageControls.get_unprocessedRecordOrderID().text
        self.enter_unprocessedRecordOrderID(orderID)
        return orderID

    def enter_unprocessedRecordOrderID(self,orderID):
        WaitUtilities.wait_for_element_to_be_visible(self.reconciliationPageControls.get_unprocessedRecordOrderID())
        FPASeleniumHelper.click_element(self.reconciliationPageControls.get_searchInputText())
        SeleniumUtilities.clear_text(self.reconciliationPageControls.get_searchInputText())
        FPASeleniumHelper.send_text_by_actions(self.reconciliationPageControls.get_searchInputText(), orderID)
        time.sleep(2)
        return orderID

    def click_editButton(self):
        WaitUtilities.wait_for_element_to_be_visible(self.reconciliationPageControls.get_unprocessedRecordEditButton(), 15000)
        FPASeleniumHelper.click_element(self.reconciliationPageControls.get_unprocessedRecordEditButton())

    def update_unprocessedRecord(self):
        WaitUtilities.wait_for_element_to_be_visible(self.reconciliationPageControls.get_unprocessedRecordEditButton(), 15000)
        FPASeleniumHelper.click_element(self.reconciliationPageControls.get_unprocessedRecordEditButton())
        loadQty = self.FSP_TestData['UnprocessedRecordLoadQty']
        unloadQty = self.FSP_TestData['UnprocessedRecordUnloadQty']
        terminaltRefID = self.FSP_TestData['UnprocessedRecordTerminalRefID']

        FPASeleniumHelper.click_element(self.reconciliationPageControls.get_updateUnprocessedRecordPopupLoadQty())
        SeleniumUtilities.clear_text(self.reconciliationPageControls.get_updateUnprocessedRecordPopupLoadQty())
        FPASeleniumHelper.send_text(self.reconciliationPageControls.get_updateUnprocessedRecordPopupLoadQty(), loadQty)
        FPASeleniumHelper.click_element(self.reconciliationPageControls.get_updateUnprocessedRecordPopupUnloadQty())
        SeleniumUtilities.clear_text(self.reconciliationPageControls.get_updateUnprocessedRecordPopupUnloadQty())
        FPASeleniumHelper.send_text(self.reconciliationPageControls.get_updateUnprocessedRecordPopupUnloadQty(), unloadQty)
        #FPASeleniumHelper.click_element(self.reconciliationPageControls.get_updateUnprocessedRecordPopupTerminalRefID())
        #SeleniumUtilities.clear_text(self.reconciliationPageControls.get_updateUnprocessedRecordPopupTerminalRefID())
        #FPASeleniumHelper.send_text(self.reconciliationPageControls.get_updateUnprocessedRecordPopupTerminalRefID, terminaltRefID)
        WaitUtilities.wait_for_element_to_be_clickable(self.reconciliationPageControls.get_reconcileUnprocessedRecordPopUpSubmitBtn())
        FPASeleniumHelper.click_element(self.reconciliationPageControls.get_reconcileUnprocessedRecordPopUpSubmitBtn())


    def validate_updatedUnprocessedRecord(self):
        WaitUtilities.wait_for_element_to_be_visible(self.reconciliationPageControls.get_unprocessedRecordTerminalRefID())
        exploadQty = self.FSP_TestData['UnprocessedRecordLoadQty']
        expUnloadQty = self.FSP_TestData['UnprocessedRecordUnloadQty']
        expterminaltRefID = self.FSP_TestData['UnprocessedRecordTerminalRefID']
        actterminaltRefID = self.reconciliationPageControls.get_unprocessedRecordTerminalRefID().text
        actloadQty = self.reconciliationPageControls.get_unprocessedRecordloadQty().text
        actUnloadQty = self.reconciliationPageControls.get_unprocessedRecordUnloadQty().text

        if(exploadQty in actloadQty and expUnloadQty in actUnloadQty and expterminaltRefID in actterminaltRefID):
            SeleniumUtilities.log.info("Update Unprocessed Record is successfull")
        else:
            SeleniumUtilities.log.error("Update Unprocessed Record has failed")



    def select_statusToUpdate(self,status):
        self.commonPageFunctions.select_DocumentType(status)
        time.sleep(1)
        self.commonPageFunctions.click_search()


    def select_reconciledDataToUpdate(self):
        self.select_statusToUpdate("Reconciliation Failed")
        #self.driver.execute_script("arguments[0].scrollIntoView(true);", self.reconciliationPageControls.get_unprocessedRecordEditButton())
        SeleniumUtilities.scroll_to_element(self.reconciliationPageControls.get_unprocessedRecordEditButton())
        self.click_editButton()
        loadQty = self.FSP_TestData['UnprocessedRecordLoadQty']
        WaitUtilities.wait_for_element_to_be_visible(self.reconciliationPageControls.get_updateReconciledDataPopupTitle(), 15000)
        FPASeleniumHelper.click_element(self.reconciliationPageControls.get_updateUnprocessedRecordPopupLoadQty())
        SeleniumUtilities.clear_text(self.reconciliationPageControls.get_updateUnprocessedRecordPopupLoadQty())
        FPASeleniumHelper.send_text(self.reconciliationPageControls.get_updateUnprocessedRecordPopupLoadQty(), loadQty)
        WaitUtilities.wait_for_element_to_be_clickable(self.reconciliationPageControls.get_reconcileUnprocessedRecordPopUpSubmitBtn())
        FPASeleniumHelper.click_element(self.reconciliationPageControls.get_reconcileUnprocessedRecordPopUpSubmitBtn())











