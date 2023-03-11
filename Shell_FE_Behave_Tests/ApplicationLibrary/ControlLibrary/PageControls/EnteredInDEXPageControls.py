from selenium.webdriver.common.by import By


class EnteredInDEXPageControls:

    def __init__(self, driver):
        self.driver = driver

    enteredInDEXPageTitle = (By.XPATH, "//span[text()='Actuals Processing']/../..//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::li/div/span[text()='Manage Actuals']")
    enteredInDEXRowHeader = (By.XPATH, "//div[@class='shell-table-header']/table/thead/tr/th")
    bolDateLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='BOL Date']")
    startDateInputBox = (By.XPATH, "//input[@placeholder='Start date']")
    finishDateInputBox = (By.XPATH, "//input[@placeholder='Finish date']")
    searchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Search By Text']")
    searchByTextCriteriaLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::span[text()='Dex Parcel Id, Contract Id, BOL Date, Buyer, Seller']")
    searchInputText = (By.XPATH, "//input[@placeholder='Search By Text']")
    bolDate = (By.XPATH, "//tbody[@class='shell-table-tbody']/tr[@class='shell-table-row shell-table-row-level-0']/td[8]")

    def get_enteredInDEXPageTitle(self):
        return self.driver.find_element(*EnteredInDEXPageControls.enteredInDEXPageTitle)

    def get_enteredInDEXRowHeader(self):
        return self.driver.find_elements(*EnteredInDEXPageControls.enteredInDEXRowHeader)

    def get_bolDateLabel(self):
        return self.driver.find_element(*EnteredInDEXPageControls.bolDateLabel)

    def get_startDateInputBox(self):
        return self.driver.find_element(*EnteredInDEXPageControls.startDateInputBox)

    def get_finishDateInputBox(self):
        return self.driver.find_element(*EnteredInDEXPageControls.finishDateInputBox)

    def get_searchByTextLabel(self):
        return self.driver.find_element(*EnteredInDEXPageControls.searchByTextLabel)

    def get_searchByTextCriteriaLabel(self):
        return self.driver.find_element(*EnteredInDEXPageControls.searchByTextCriteriaLabel)

    def get_searchInputText(self):
        return self.driver.find_element(*EnteredInDEXPageControls.searchInputText)

    def get_bolDate(self):
        return self.driver.find_elements(*EnteredInDEXPageControls.bolDate)

