from selenium.webdriver.common.by import By


class UnprocessedRecordsPageControls:

    def __init__(self, driver):
        self.driver = driver

    unprocessedRecordPageTitle = (By.XPATH, "//span[text()='Reconciliation']/../../following-sibling::li/div/span[text()='Unprocessed Records']")
    unprocessedRecordRowHeader = (By.XPATH, "//div[@class='shell-table-header']/table/thead/tr/th")


    def get_unprocessedRecordPageTitle(self):
        return self.driver.find_element(*UnprocessedRecordsPageControls.unprocessedRecordPageTitle)

    def get_unprocessedRecordRowHeader(self):
        return self.driver.find_elements(*UnprocessedRecordsPageControls.unprocessedRecordRowHeader)
    