from selenium.webdriver.common.by import By


class FailedToEnteredInDEXPageControls:

    def __init__(self, driver):
        self.driver = driver

    failedToEnteredInDEXPageTitle = (By.XPATH, "//span[text()='Logs']/../..//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::li/div/span[text()='Actuals Errors']")
    failedToEnteredInDEXRowHeader = (By.XPATH, "//div[@class='shell-table-header']/table/thead/tr/th")
    errorLogsDateRangeLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Error Logs Date Range']")
    startDateInputBox = (By.XPATH, "//input[@placeholder='Start date']")
    finishDateInputBox = (By.XPATH, "//input[@placeholder='Finish date']")
    statusLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Status']")
    searchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Search By Text']")
    searchByTextCriteriaLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::span[text()='Error Message, Contract Id, BOL Date']")
    searchInputText = (By.XPATH, "//input[@placeholder='Search By Text']")
    contractID = (By.XPATH, "//tbody[@class='shell-table-tbody']/tr[@class='shell-table-row shell-table-row-level-0']/td[5]")

    def get_failedToEnteredInDEXPageTitle(self):
        return self.driver.find_element(*FailedToEnteredInDEXPageControls.failedToEnteredInDEXPageTitle)

    def get_failedToEnteredInDEXRowHeader(self):
        return self.driver.find_elements(*FailedToEnteredInDEXPageControls.failedToEnteredInDEXRowHeader)

    def get_errorLogsDateRangeLabel(self):
        return self.driver.find_element(*FailedToEnteredInDEXPageControls.errorLogsDateRangeLabel)

    def get_startDateInputBox(self):
        return self.driver.find_element(*FailedToEnteredInDEXPageControls.startDateInputBox)

    def get_finishDateInputBox(self):
        return self.driver.find_element(*FailedToEnteredInDEXPageControls.finishDateInputBox)

    def get_status(self):
        return self.driver.find_element(*FailedToEnteredInDEXPageControls.statusLabel)

    def get_searchByTextLabel(self):
        return self.driver.find_element(*FailedToEnteredInDEXPageControls.searchByTextLabel)

    def get_searchByTextCriteriaLabel(self):
        return self.driver.find_element(*FailedToEnteredInDEXPageControls.searchByTextCriteriaLabel)

    def get_searchInputText(self):
        return self.driver.find_element(*FailedToEnteredInDEXPageControls.searchInputText)

    def get_contractID(self):
        return self.driver.find_element(*FailedToEnteredInDEXPageControls.contractID)

