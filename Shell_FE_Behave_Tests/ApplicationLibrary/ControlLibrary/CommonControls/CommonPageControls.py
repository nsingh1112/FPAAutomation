from selenium.webdriver.common.by import By

class CommonPageControls:

    def __init__(self, driver):
        self.driver = driver

    homepage = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Home']")
    statusInputBox = (By.XPATH, "//input[@class='shell-select-container-selection-search-input']")
    status = (By.XPATH, "//div[@class='shell-select-container-item shell-select-container-item-option' and @title='Aggregation Completed']")
    searchButton = (By.XPATH, "//button[@class='sc-papXJ gDMjLE shell-button']/span[text()='Search']")
    clearSearchButton = (By.XPATH, "//a[@class='sc-jqUVSM hLItTL shell-button']")
    documentInputBox = (By.XPATH, "//input[@class='shell-select-container-selection-search-input']")
    document = (By.XPATH, "//div[@class='shell-select-container-item-option-content' and text()='XLSX']")
    totalRecordsCount = (By.XPATH, "//p[@class='sc-bczRLJ hbSXPu shell-text-paragraph']/em")
    toastMsg = (By.XPATH, "//div[@class ='Toastify']/div")

    def get_Homepage(self):
        return self.driver.find_element(*CommonPageControls.homepage)

    def get_statusInputBox(self):
        return self.driver.find_element(*CommonPageControls.statusInputBox)

    def get_status(self):
        return self.driver.find_element(*CommonPageControls.status)

    def get_searchButton(self):
        return self.driver.find_element(*CommonPageControls.searchButton)

    def get_clearSearchButton(self):
        return self.driver.find_element(*CommonPageControls.clearSearchButton)

    def get_getDocumentInputBox(self):
        return self.driver.find_element(*CommonPageControls.documentInputBox)

    def get_document(self):
        return self.driver.find_element(*CommonPageControls.document)

    def get_totalRecordsCount(self):
        return self.driver.find_element(*CommonPageControls.totalRecordsCount)

    def get_toastMessageDiv(self):
        return self.driver.find_element(*CommonPageControls.toastMsg)

