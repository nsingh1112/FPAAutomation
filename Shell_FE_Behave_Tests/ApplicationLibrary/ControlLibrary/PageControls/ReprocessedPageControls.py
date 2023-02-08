from selenium.webdriver.common.by import By


class ReprocessedPageControls:

    def __init__(self, driver):
        self.driver = driver

    reprocessedLink = (By.XPATH, "//div[@class='sc-jIAOiI hHlWKS' and text()='Reprocessed']")
    reconciledDataRowHeader = (By.XPATH, "//div[@class='shell-table-header']/table/thead/tr/th")


    def get_reprocessedLink(self):
        return self.driver.find_element(*ReprocessedPageControls.reprocessedLink)

    def get_reconciledDataRowHeader(self):
        return self.driver.find_elements(*ReprocessedPageControls.reconciledDataRowHeader)

