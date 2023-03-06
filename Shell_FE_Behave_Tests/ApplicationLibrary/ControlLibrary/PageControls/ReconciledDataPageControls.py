from selenium.webdriver.common.by import By


class ReconciledDataPageControls:

    def __init__(self, driver):
        self.driver = driver

    reconciledDataPageTitle = (By.XPATH, "//div/span[text()='Reconciled Data']")
    reconciledDataRowHeader = (By.XPATH, "//div[@class='shell-table-header']/table/thead/tr/th")
    receivedDateLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Received Date']")
    startDateInputBox = (By.XPATH, "//input[@placeholder='Start date']")
    finishDateInputBox = (By.XPATH, "//input[@placeholder='Finish date']")
    statusLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Status']")
    searchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Search By Text']")
    searchByTextCriteriaLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::span[text()='Order Id, Ref Id, Tank Id and License Plate']")
    searchByText= (By.XPATH, "//input[@placeholder='Search By Text']")
    searchButton = (By.XPATH, "//button[@class='sc-papXJ gDMjLE shell-button']/span[text()='Search']")
    clearSearchButton = (By.XPATH, "//a[@class='sc-jqUVSM hLItTL shell-button']")
    receivedDate = (By.XPATH, "//tbody[@class='shell-table-tbody']/tr[@class='shell-table-row shell-table-row-level-0']/td[2]")


    def get_reconciledDataPageTitle(self):
        return self.driver.find_element(*ReconciledDataPageControls.reconciledDataPageTitle)

    def get_reconciledDataRowHeader(self):
        return self.driver.find_elements(*ReconciledDataPageControls.reconciledDataRowHeader)

    def get_receivedDateLabel(self):
        return self.driver.find_element(*ReconciledDataPageControls.receivedDateLabel)

    def get_startDateInputBox(self):
        return self.driver.find_element(*ReconciledDataPageControls.startDateInputBox)

    def get_statusLabel(self):
        return self.driver.find_element(*ReconciledDataPageControls.statusLabel)

    def get_searchByTextLabel(self):
        return self.driver.find_element(*ReconciledDataPageControls.searchByTextLabel)

    def get_searchByTextCriteriaLabel(self):
        return self.driver.find_element(*ReconciledDataPageControls.searchByTextCriteriaLabel)

    def get_searchButton(self):
        return self.driver.find_element(*ReconciledDataPageControls.searchButton)

    def get_clearSearchButton(self):
        return self.driver.find_element(*ReconciledDataPageControls.clearSearchButton)

    def get_receivedDate(self):
        return self.driver.find_elements(*ReconciledDataPageControls.receivedDate)

    