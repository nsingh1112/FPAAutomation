from selenium.webdriver.common.by import By


class DashboardPageControls:

    def __init__(self, driver):
        self.driver = driver

    dashboardItems = (By.XPATH, "//span[text()='Dashboard']/following::div[@class='sc-TRNrF dkAayx']")
    dashboardGraphicalRep = (By.XPATH, "//div[@class='sc-iAvgwm cCdqsl']//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/*[local-name()='path']")
    texDarkMode = (By.XPATH, "// button[ @ title = 'Dark Mode'] / following::span[text() = 'Dark Mode']")
    btnDarkMode = (By.XPATH, "//button[@title='Dark Mode']")

    def get_dashboardItems(self):
        return self.driver.find_elements(*DashboardPageControls.dashboardItems)

    def get_dashboardGraphicalRep(self):
        return self.driver.find_element(*DashboardPageControls.dashboardGraphicalRep)

    def get_texDarkMode(self):
        return self.driver.find_element(*DashboardPageControls.texDarkMode)

    def get_btnDarkMode(self):
        return self.driver.find_element(*DashboardPageControls.btnDarkMode)
    