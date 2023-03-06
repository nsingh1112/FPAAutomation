from selenium.webdriver.common.by import By


class LogsPageControls:

    def __init__(self, driver):
        self.driver = driver

    reconciliationPageTitle = (By.XPATH, "//span[text()='Logs']/following::span[text()='Reconciliation']")
    reconciliationErrorsPageTitle = (By.XPATH, "//span[text()='Logs']/following::span[text()='Reconciliation Errors']")
    actualsErrorsPageTitle = (By.XPATH, "//span[text()='Logs']/following::span[text()='Actuals Errors']")

    rowHeader = (By.XPATH, "//div[@class='shell-table-header']/table/thead/tr/th")
    receivedDateLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Received Date']")
    errorLogDateRangeLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Error Logs Date Range']")
    startDateInputBox = (By.XPATH, "//input[@placeholder='Start date']")
    finishDateInputBox = (By.XPATH, "//input[@placeholder='Finish date']")
    statusLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Status']")
    searchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Search By Text']")
    reconciliationSearchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::span[text()='Ref Id, Dex Parcel Id']")
    reconciliationErrorsSearchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::span[text()='Error Message, Ref Id, Contract Id']")
    actualErrorsSearchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::span[text()='Error Message, Contract Id, BOL Date']")
    searchInputText = (By.XPATH, "//input[@placeholder='Search By Text']")

    def get_reconciliationPageTitle(self):
        return self.driver.find_element(*LogsPageControls.reconciliationPageTitle)

    def get_reconciliationErrorsPageTitle(self):
        return self.driver.find_element(*LogsPageControls.reconciliationErrorsPageTitle)

    def get_actualsErrorsPageTitle(self):
        return self.driver.find_element(*LogsPageControls.actualsErrorsPageTitle)

    def get_rowHeader(self):
        return self.driver.find_elements(*LogsPageControls.rowHeader)

    def get_receivedDateLabel(self):
        return self.driver.find_element(*LogsPageControls.receivedDateLabel)

    def get_errorLogDateRangeLabel(self):
        return self.driver.find_element(*LogsPageControls.errorLogDateRangeLabel)

    def get_startDateInputBox(self):
        return self.driver.find_element(*LogsPageControls.startDateInputBox)

    def get_finishDateInputBox(self):
        return self.driver.find_element(*LogsPageControls.finishDateInputBox)

    def get_statusLabel(self):
        return self.driver.find_element(*LogsPageControls.statusLabel)

    def get_searchByTextLabel(self):
        return self.driver.find_element(*LogsPageControls.searchByTextLabel)

    def get_reconciliationSearchByTextLabel(self):
        return self.driver.find_element(*LogsPageControls.reconciliationSearchByTextLabel)

    def get_reconciliationErrorsSearchByTextLabel(self):
        return self.driver.find_element(*LogsPageControls.reconciliationErrorsSearchByTextLabel)

    def get_actualErrorsSearchByTextLabel(self):
        return self.driver.find_element(*LogsPageControls.actualErrorsSearchByTextLabel)

    def get_searchInputText(self):
        return self.driver.find_element(*LogsPageControls.searchInputText)




