from selenium.webdriver.common.by import By


class ReconciliationPageControls:

    def __init__(self, driver):
        self.driver = driver

    unprocessedRecordPageTitle = (By.XPATH, "//span[text()='Reconciliation']/following::span[text()='Unprocessed Records']")
    reconciledDataPageTitle = (By.XPATH, "//span[text()='Reconciliation']/following::span[text()='Reconciled Data']")
    rowHeader = (By.XPATH, "//div[@class='shell-table-header']/table/thead/tr/th")
    receivedDateLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Received Date']")
    startDateInputBox = (By.XPATH, "//input[@placeholder='Start date']")
    finishDateInputBox = (By.XPATH, "//input[@placeholder='Finish date']")
    searchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Search By Text']")
    searchByTextCriteriaLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::span[text()='Order Id, Ref Id, Tank Id and License Plate']")
    searchInputText = (By.XPATH, "//input[@placeholder='Search By Text']")
    receivedDate = (By.XPATH, "//tbody[@class='shell-table-tbody']/tr[@class='shell-table-row shell-table-row-level-0']/td[2]")

    def get_unprocessedRecordPageTitle(self):
        return self.driver.find_element(*ReconciliationPageControls.unprocessedRecordPageTitle)

    def get_reconciledDataPageTitle(self):
        return self.driver.find_element(*ReconciliationPageControls.reconciledDataPageTitle)

    def get_rowHeader(self):
        return self.driver.find_elements(*ReconciliationPageControls.rowHeader)

    def get_receivedDateLabel(self):
        return self.driver.find_element(*ReconciliationPageControls.receivedDateLabel)

    def get_startDateInputBox(self):
        return self.driver.find_element(*ReconciliationPageControls.startDateInputBox)

    def get_finishDateInputBox(self):
        return self.driver.find_element(*ReconciliationPageControls.finishDateInputBox)

    def get_searchByTextLabel(self):
        return self.driver.find_element(*ReconciliationPageControls.searchByTextLabel)

    def get_searchByTextCriteriaLabel(self):
        return self.driver.find_element(*ReconciliationPageControls.searchByTextCriteriaLabel)

    def get_searchInputText(self):
        return self.driver.find_element(*ReconciliationPageControls.searchInputText)

    def get_receivedDate(self):
        return self.driver.find_elements(*ReconciliationPageControls.receivedDate)




