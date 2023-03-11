from selenium.webdriver.common.by import By


class DocumentsPageControls:

    def __init__(self, driver):
        self.driver = driver

    terminalReportPageTitle = (By.XPATH, "//span[text()='Documents']/following::span[text()='Terminal Reports']")
    terminalReportRowHeader = (By.XPATH, "//div[@class='shell-table-header']/table/thead/tr/th")
    receivedDateLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Received Date']")
    startDateInputBox = (By.XPATH, "//input[@placeholder='Start date']")
    finishDateInputBox = (By.XPATH, "//input[@placeholder='Finish date']")
    documentType = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Document Type']")
    searchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Search By Text']")
    searchByTextCriteriaLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::span[text()='Filename, Email From, Email Subject']")
    searchInputText = (By.XPATH, "//input[@placeholder='Search By Text']")
    fileNameLink = (By.XPATH, "//td[@class='shell-table-cell']/a")
    newWindowLoginInputBox = (By.XPATH, "//input[@name='loginfmt']")
    newWindowNextButton = (By.XPATH, "//input[@type='submit']")
    invoicesTitle = (By.XPATH, "//span[text()='Documents']/following::span[text()='Invoices']")
    totalRecordsCount = (By.XPATH, "//p[@class='sc-bczRLJ hbSXPu shell-text-paragraph']/em")
    rowData = (By.XPATH, "//tr[@class='shell-table-row shell-table-row-level-0']/td[@class='shell-table-cell']")
    fileName = (By.XPATH, "//tr/td[@class='shell-table-cell']/a/span[@class='sc-ksZaOG kwPwYx']")
    receivedDate = (By.XPATH, "//tr/td[@class='shell-table-cell']/span[@class='sc-fctJkW buDZzM shell-text-label']")
    docType = (By.XPATH, "(//tr[@class='shell-table-row shell-table-row-level-0']/td)[4]")

    def get_terminalReportPageTitle(self):
        return self.driver.find_element(*DocumentsPageControls.terminalReportPageTitle)

    def get_terminalReportRowHeader(self):
        return self.driver.find_elements(*DocumentsPageControls.terminalReportRowHeader)

    def get_receivedDateLabel(self):
        return self.driver.find_element(*DocumentsPageControls.receivedDateLabel)

    def get_startDateInputBox(self):
        return self.driver.find_element(*DocumentsPageControls.startDateInputBox)

    def get_finishDateInputBox(self):
        return self.driver.find_element(*DocumentsPageControls.finishDateInputBox)

    def get_documentType(self):
        return self.driver.find_element(*DocumentsPageControls.documentType)

    def get_searchByTextLabel(self):
        return self.driver.find_element(*DocumentsPageControls.searchByTextLabel)

    def get_searchByTextCriteriaLabel(self):
        return self.driver.find_element(*DocumentsPageControls.searchByTextCriteriaLabel)

    def get_searchInputText(self):
        return self.driver.find_element(*DocumentsPageControls.searchInputText)

    def get_fileNameLink(self):
        return self.driver.find_element(*DocumentsPageControls.fileNameLink)

    def get_newWindowLoginInputBox(self):
        return self.driver.find_element(*DocumentsPageControls.newWindowLoginInputBox)

    def get_newWindowNextButton(self):
        return self.driver.find_element(*DocumentsPageControls.newWindowNextButton)

    def get_invoicesTitle(self):
        return self.driver.find_element(*DocumentsPageControls.invoicesTitle)

    def get_totalRecordsCount(self):
        return self.driver.find_element(*DocumentsPageControls.totalRecordsCount)

    def get_rowData(self):
        return self.driver.find_elements(*DocumentsPageControls.rowData)

    def get_fileName(self):
        return self.driver.find_element(*DocumentsPageControls.fileName)

    def get_receivedDate(self):
        return self.driver.find_element(*DocumentsPageControls.receivedDate)

    def get_docType(self):
        return self.driver.find_element(*DocumentsPageControls.docType)



