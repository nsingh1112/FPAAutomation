from selenium.webdriver.common.by import By


class UnprocessedRecordsPageControls:

    def __init__(self, driver):
        self.driver = driver

    unprocessedRecordPageTitle = (By.XPATH, "//span[text()='Reconciliation']/../..//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::li/div/span[text()='Unprocessed Records']")
    unprocessedRecordRowHeader = (By.XPATH, "//div[@class='shell-table-header']/table/thead/tr/th")
    totalUnprocessedRecord = (By.XPATH, "//strong/..")


    def get_unprocessedRecordPageTitle(self):
        return self.driver.find_element(*UnprocessedRecordsPageControls.unprocessedRecordPageTitle)

    def get_unprocessedRecordRowHeader(self):
        return self.driver.find_elements(*UnprocessedRecordsPageControls.unprocessedRecordRowHeader)

    def get_totalUnprocessedRecord(self):
        return self.driver.find_element(*UnprocessedRecordsPageControls.totalUnprocessedRecord)
    