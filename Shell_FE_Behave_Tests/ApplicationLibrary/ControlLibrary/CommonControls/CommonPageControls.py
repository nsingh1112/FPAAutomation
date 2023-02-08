from selenium.webdriver.common.by import By

class CommonPageControls:

    def __init__(self, driver):
        self.driver = driver

    homepage = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Home']")
    statusInputBox = (By.XPATH, "//input[@class='shell-select-container-selection-search-input']")
    status = (By.XPATH, "//div[@class='shell-select-container-item shell-select-container-item-option' and @title='Aggregation Completed']")


    def get_Homepage(self):
        return self.driver.find_element(*CommonPageControls.homepage)

    def get_statusInputBox(self):
        return self.driver.find_element(*CommonPageControls.statusInputBox)

    def get_status(self):
        return self.driver.find_element(*CommonPageControls.status)

