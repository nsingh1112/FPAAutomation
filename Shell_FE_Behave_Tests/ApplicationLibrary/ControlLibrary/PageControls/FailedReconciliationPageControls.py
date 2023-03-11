from selenium.webdriver.common.by import By


class FailedReconciliationPageControls:

    def __init__(self, driver):
        self.driver = driver

    failedReconciliationPageTitle = (By.XPATH, "//span[text()='Logs']/../..//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::li/div/span[text()='Reconciliation Errors']")
    failedReconciliationRowHeader = (By.XPATH, "//div[@class='shell-table-header']/table/thead/tr/th")
    errorLogDateRangeLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Error Logs Date Range']")
    startDateInputBox = (By.XPATH, "//input[@placeholder='Start date']")
    finishDateInputBox = (By.XPATH, "//input[@placeholder='Finish date']")
    statusLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Status']")
    searchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Search By Text']")
    searchByTextCriteriaLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::span[text()='Error Message, Ref Id, Contract Id']")
    searchInputText= (By.XPATH, "//input[@placeholder='Search By Text']")
    receivedDate = (By.XPATH, "//tbody[@class='shell-table-tbody']/tr[@class='shell-table-row shell-table-row-level-0']/td[7]")
    orderID = (By.XPATH, "//tbody[@class='shell-table-tbody']/tr[@class='shell-table-row shell-table-row-level-0']/td[5]")

    def get_failedReconciliationPageTitle(self):
        return self.driver.find_element(*FailedReconciliationPageControls.failedReconciliationPageTitle)

    def get_failedReconciliationRowHeader(self):
        return self.driver.find_elements(*FailedReconciliationPageControls.failedReconciliationRowHeader)

    def get_errorLogDateRangeLabel(self):
        return self.driver.find_element(*FailedReconciliationPageControls.errorLogDateRangeLabel)

    def get_startDateInputBox(self):
        return self.driver.find_element(*FailedReconciliationPageControls.startDateInputBox)

    def get_finishDateInputBox(self):
        return self.driver.find_element(*FailedReconciliationPageControls.finishDateInputBox)

    def get_statusLabel(self):
        return self.driver.find_element(*FailedReconciliationPageControls.statusLabel)

    def get_searchByTextLabel(self):
        return self.driver.find_element(*FailedReconciliationPageControls.searchByTextLabel)

    def get_searchByTextCriteriaLabel(self):
        return self.driver.find_element(*FailedReconciliationPageControls.searchByTextCriteriaLabel)

    def get_searchInputText(self):
        return self.driver.find_element(*FailedReconciliationPageControls.searchInputText)

    def get_receivedDate(self):
        return self.driver.find_elements(*FailedReconciliationPageControls.receivedDate)

    def get_orderID(self):
        return self.driver.find_element(*FailedReconciliationPageControls.orderID)

