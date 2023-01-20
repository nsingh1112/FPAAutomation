from selenium.webdriver.common.by import By


class FPAHomePageControls:

    def __init__(self, driver):
        self.driver = driver

    invoices = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Invoices']")
    pdfLink = (By.XPATH, "//span[contains(text(),'.pdf')]")


    def get_invoices(self):
        return self.driver.find_element(*FPAHomePageControls.invoices)


    def get_pdfLink(self):
        return self.driver.find_element(*FPAHomePageControls.pdfLink)
