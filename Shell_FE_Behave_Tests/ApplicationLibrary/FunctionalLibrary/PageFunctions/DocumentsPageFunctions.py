import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.DocumentsPageControls import \
    DocumentsPageControls
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonPageFunctions import \
    CommonPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonRowPageFunctions import \
    CommonRowPageFunctions
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper


class DocumentsPageFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.documentsPageControls = DocumentsPageControls(SeleniumBase.driver)
        self.commonPageFunctions = CommonPageFunctions(SeleniumBase.driver)

    def validate_terminalReportPageTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.documentsPageControls.get_terminalReportPageTitle(), 10000)
        if FPASeleniumHelper.check_element_exists_by_xpath( self.documentsPageControls.get_terminalReportPageTitle()):
            SeleniumUtilities.log.info("Terminal Report Page title is correct")

        else:
            SeleniumUtilities.log.error("Terminal Report Page title is not correct")

    def get_terminalReportDataRowHeaders(self):
        WaitUtilities.wait_for_element_to_be_visible(
            self.documentsPageControls.get_terminalReportRowHeader())
        options1 = self.documentsPageControls.get_terminalReportRowHeader()
        CommonRowPageFunctions.validate_rowHeader(self, options1)

    def verify_terminalreportDataFields(self):
        WaitUtilities.wait_for_element_to_be_visible(self.documentsPageControls.get_terminalReportRowHeader())
        isreceivedDateLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.documentsPageControls.get_receivedDateLabel())
        isfinishDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.documentsPageControls.get_finishDateInputBox())
        isstartDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.documentsPageControls.get_startDateInputBox())
        isdocumentTypeLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.documentsPageControls.get_documentType())
        issearchByTextLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.documentsPageControls.get_searchByTextLabel())
        issearchByTextCriteriaLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.documentsPageControls.get_searchByTextCriteriaLabel())
        issearchInputText = FPASeleniumHelper.check_element_exists_by_xpath(self.documentsPageControls.get_searchInputText())

        if(isreceivedDateLabel and isstartDateInputBox and isfinishDateInputBox and isdocumentTypeLabel and issearchByTextLabel and issearchByTextCriteriaLabel and issearchInputText):
            SeleniumUtilities.log.info("Terminal Report Data Fields Verified")
        else:
            SeleniumUtilities.log.error("Terminal Report Data Fields not Verified")

    def click_filename(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.documentsPageControls.get_fileNameLink())
        FPASeleniumHelper.click_element(self.documentsPageControls.get_fileNameLink())

    def click_validateAndSwitchWindow(self):
        windows = self.driver.window_handles
        noOfWindows = len(windows)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(4)
        WaitUtilities.wait_for_element_to_be_clickable(self.documentsPageControls.get_newWindowLoginInputBox())
        FPASeleniumHelper.send_text(self.documentsPageControls.get_newWindowLoginInputBox(), "nupur.singh@shell.com")
        time.sleep(2)
        WaitUtilities.wait_for_element_to_be_clickable(self.documentsPageControls.get_newWindowNextButton())
        FPASeleniumHelper.click_element(self.documentsPageControls.get_newWindowNextButton())
        time.sleep(2)

    def validate_invoicesTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.documentsPageControls.get_invoicesTitle())
        if FPASeleniumHelper.check_element_exists_by_xpath( self.documentsPageControls.get_invoicesTitle()):
            SeleniumUtilities.log.info("Invoices title is correct")

        else:
            SeleniumUtilities.log.error("Invoices title is not correct")


    def validate_data(self, datafromDB):
        dbData = ""
        for i in datafromDB:
            dbData += str(i) + " "
        dbFileName = (dbData.split(',')[0]).replace('(', '')[:-1]
        dbDocumentType = dbData.split(',')[1]
        dbEmailFrom = dbData.split(',')[2]
        dbEmailSubject = dbData.split(',')[3]
        self.enter_fileNameAndSearch(dbFileName[1:])
        UiFilename  =self.documentsPageControls.get_fileName().text
        UirowValues = self.get_rowData()
        uiEmailFrom = UirowValues[1]
        uiEmailSubject = UirowValues[2]
        uiDocumentType = (UirowValues)[3]
        if((UiFilename in dbFileName) and (uiEmailFrom in dbEmailFrom) and (uiEmailSubject in dbEmailSubject) and (uiDocumentType in dbDocumentType) ):
            SeleniumUtilities.log.info("Elements verified from DB")
        else:
            SeleniumUtilities.log.error("Elements not verified from DB")

    def get_rowData(self):
        WaitUtilities.wait_for_element_to_be_visible(self.documentsPageControls.get_rowData())
        time.sleep(2)
        rowData = self.documentsPageControls.get_rowData()
        row_header_list = [x.get_attribute('innerHTML') for x in rowData]
        current_row_header_list = []
        for row in row_header_list:
            current_row_header_list.append(row)
        return current_row_header_list

    def enter_fileNameAndSearch(self, filename):
        WaitUtilities.wait_for_element_to_be_clickable(self.documentsPageControls.get_searchInputText())
        FPASeleniumHelper.send_text(self.documentsPageControls.get_searchInputText(), filename)
        self.commonPageFunctions.click_search()
        time.sleep(2)
        WaitUtilities.wait_for_element_to_be_clickable(self.documentsPageControls.get_fileName())

    def enter_fileName(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.documentsPageControls.get_searchInputText())
        filename = self.documentsPageControls.get_fileName().text
        FPASeleniumHelper.send_text(self.documentsPageControls.get_searchInputText(), filename)
        time.sleep(2)
        WaitUtilities.wait_for_element_to_be_clickable(self.documentsPageControls.get_fileName())
        return filename

    def validate_fileName(self,expFileName):
        WaitUtilities.wait_for_element_to_be_visible(self.documentsPageControls.get_fileName())
        actFileName = self.documentsPageControls.get_fileName().text
        if(expFileName in actFileName):
            SeleniumUtilities.log.info("FileName Verified")
        else:
            SeleniumUtilities.log.error("FileName not Verified")

    def get_documentType(self):
        WaitUtilities.wait_for_element_to_be_visible(self.documentsPageControls.get_docType())
        documentType = self.documentsPageControls.get_docType().text
        return documentType



