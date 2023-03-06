from selenium.webdriver.common.by import By


class HomePageControls:

    def __init__(self, driver):
        self.driver = driver

    applicationTitle = (By.XPATH, "//p[text()='FeedStock Procurement Automation']")
    documentsMenuItems = (By.XPATH, "//div[@class='shell-menu-item-group-title' and text()='Documents']/../ul/li/div")
    reconciliationMenuItems = (By.XPATH, "//div[@class='shell-menu-item-group-title' and text()='Reconciliation']/../ul/li/div")
    actualProcessingMenuItems = (By.XPATH, "//div[@class='shell-menu-item-group-title' and text()='Actuals Processing']/../ul/li/div")
    logsMenuItems = (By.XPATH, "//div[@class='shell-menu-item-group-title' and text()='Logs']/../ul/li/div")
    MenuItems = (By.XPATH, "//div[@class='shell-menu-item-group-title']")
    linkUnprocessedRecord = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Unprocessed Records']")
    reconciled = (By.XPATH, "//div[@class='sc-jIAOiI hHlWKS' and text()='Reconciled']")
    reprocessed = (By.XPATH, "//div[@class='sc-jIAOiI hHlWKS' and text()='Reprocessed']")
    failedReconciliation = (By.XPATH, "//div[@class='sc-jIAOiI hHlWKS' and text()='Failed Reconciliation']")
    enteredInDEX = (By.XPATH, "//div[@class='sc-jIAOiI hHlWKS' and text()='Entered in DEX']")
    failedToEnterInDEX = (By.XPATH, "//div[@class='sc-jIAOiI hHlWKS' and text()='Failed to enter in DEX']")
    terminalReport = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Terminal Report']")
    invoices = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Invoices']")
    unprocessedRecord = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Unprocessed Records']")
    reconciledData = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Reconciled Data']")
    create = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Create']")
    manageActuals = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Manage Actuals']")
    actualVolumes = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Actual Volumes']")

    reconciliation = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Reconciliation']")
    reconciliationErrors = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Reconciliation Errors']")
    actualErrors = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Reconciliation Errors']/../following-sibling::li/div")

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

    def get_reconciled(self):
        return self.driver.find_element(*HomePageControls.reconciled)

    def get_reprocessed(self):
        return self.driver.find_element(*HomePageControls.reprocessed)

    def get_failedReconciliation(self):
        return self.driver.find_element(*HomePageControls.failedReconciliation)

    def get_enteredInDEX(self):
        return self.driver.find_element(*HomePageControls.enteredInDEX)

    def get_failedToEnterInDEX(self):
        return self.driver.find_element(*HomePageControls.failedToEnterInDEX)

    def get_terminalReport(self):
        return self.driver.find_element(*HomePageControls.terminalReport)

    def get_invoices(self):
        return self.driver.find_element(*HomePageControls.invoices)

    def get_unprocessedRecord(self):
        return self.driver.find_element(*HomePageControls.unprocessedRecord)

    def get_applicationTitle(self):
        return self.driver.find_element(*HomePageControls.applicationTitle)

    def get_reconciledData(self):
        return self.driver.find_element(*HomePageControls.reconciledData)

    def get_create(self):
        return self.driver.find_element(*HomePageControls.create)

    def get_manageActuals(self):
        return self.driver.find_element(*HomePageControls.manageActuals)

    def get_actualVolumes(self):
        return self.driver.find_element(*HomePageControls.actualVolumes)

    def get_reconciliation(self):
        return self.driver.find_element(*HomePageControls.reconciliation)

    def get_reconciliationErrors(self):
        return self.driver.find_element(*HomePageControls.reconciliationErrors)

    def get_actualErrors(self):
        return self.driver.find_element(*HomePageControls.actualErrors)


    