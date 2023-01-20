from selenium.webdriver.common.by import By


class HomePageControls:

    def __init__(self, driver):
        self.driver = driver

    documentsMenuItems = (By.XPATH, "//div[@class='shell-menu-item-group-title' and text()='Documents']/../ul/li/div")
    reconciliationMenuItems = (By.XPATH, "//div[@class='shell-menu-item-group-title' and text()='Reconciliation']/../ul/li/div")
    actualProcessingMenuItems = (By.XPATH, "//div[@class='shell-menu-item-group-title' and text()='Actuals Processing']/../ul/li/div")
    logsMenuItems = (By.XPATH, "//div[@class='shell-menu-item-group-title' and text()='Logs']/../ul/li/div")
    MenuItems = (By.XPATH, "//div[@class='shell-menu-item-group-title']")
    linkUnprocessedRecord = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Unprocessed Records']")


    def get_documentsMenuItems(self):
        return self.driver.find_elements(*HomePageControls.documentsMenuItems)


    def get_reconciliationMenuItems(self):
        return self.driver.find_elements(*HomePageControls.reconciliationMenuItems)


    def get_actualProcessingMenuItems(self):
        return self.driver.find_elements(*HomePageControls.actualProcessingMenuItems)

    def get_logsMenuItems(self):
        return self.driver.find_elements(*HomePageControls.logsMenuItems)

    def get_MenuItems(self):
        return self.driver.find_elements(*HomePageControls.MenuItems)

    def get_linkUnprocessedRecord(self):
        return self.driver.find_element(*HomePageControls.linkUnprocessedRecord)
    