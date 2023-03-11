from selenium.webdriver.common.by import By


class ReconciliationPageControls:

    def __init__(self, driver):
        self.driver = driver

    unprocessedRecordPageTitle = (By.XPATH, "//span[text()='Reconciliation']/following::span[text()='Unprocessed Records']")
    reconciledDataPageTitle = (By.XPATH, "//span[text()='Reconciliation']/following::span[text()='Reconciled Data']")
    rowHeader = (By.XPATH, "//div[@class='shell-table-header']/table/thead/tr/th")
    receivedDateLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Received Date']")
    startDateInputBox = (By.XPATH, "//input[@placeholder='Start date']")
    finishDateInputBox = (By.XPATH, "//input[@placeholder='Finish date']")
    searchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Search By Text']")
    searchByTextCriteriaLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::span[text()='Order Id, Ref Id, Tank Id and License Plate']")
    searchInputText = (By.XPATH, "//input[@placeholder='Search By Text']")
    receivedDate = (By.XPATH, "//tbody[@class='shell-table-tbody']/tr[@class='shell-table-row shell-table-row-level-0']/td[2]")
    reconcileUnprocessedRecordsButton = (By.XPATH, "//span[@class='sc-ksZaOG kwPwYx' and text()='Reconcile Unprocessed Records']")
    reconcileUnprocessedRecordsPopUpTitle = (By.XPATH, "//strong[text()='Reconcile New Records']")
    reconcileUnprocessedRecordPopUpBody = (By.XPATH, "//div[text()='Are you sure you want to reconcile unprocessed records?']")
    reconcileUnprocessedRecordsPopUpCancelBtn = (By.XPATH, "//button[@class='sc-papXJ iFkojq shell-button']/span[text()='Cancel']")
    reconcileUnprocessedRecordPopUpSubmitBtn = ( By.XPATH, "//button[@class='sc-papXJ gfyoCe shell-button']/span[text()='Submit']")
    unprocessedRecordOrderID = (By.XPATH, "(//tr[@class='shell-table-row shell-table-row-level-0']/td)[2]")
    unprocessedRecordEditButton = (By.XPATH, "//td[@class='shell-table-cell']/button[@class='sc-papXJ fgKufr shell-button']")
    updateUnprocessedRecordPopupLoadQty = (By.XPATH, "//div[@id='loadedQty']/../following-sibling::div/input")
    updateUnprocessedRecordPopupUnloadQty = (By.XPATH, "//div[@id='unloadedQty']/../following-sibling::div/input")
    updateUnprocessedRecordPopupTerminalRefID = (By.XPATH, "//div[@id='terminalReferenceId']/../following-sibling::div/input")
    updateUnprocessedRecordPopupTitle = (By.XPATH, "//strong[text()='Update Quantity and Terminal Ref Id']")

    unprocessedRecordTerminalRefID = (By.XPATH, "(//tr[@class='shell-table-row shell-table-row-level-0']/td)[4]")
    unprocessedRecordloadQty = (By.XPATH, "(//tr[@class='shell-table-row shell-table-row-level-0']/td)[5]")
    unprocessedRecordUnloadQty = (By.XPATH, "(//tr[@class='shell-table-row shell-table-row-level-0']/td)[6]")

    updateReconciledDataPopupTitle = (By.XPATH, "//strong[text()='Update Loaded Quantity']")

    def get_unprocessedRecordPageTitle(self):
        return self.driver.find_element(*ReconciliationPageControls.unprocessedRecordPageTitle)

    def get_reconciledDataPageTitle(self):
        return self.driver.find_element(*ReconciliationPageControls.reconciledDataPageTitle)

    def get_rowHeader(self):
        return self.driver.find_elements(*ReconciliationPageControls.rowHeader)

    def get_receivedDateLabel(self):
        return self.driver.find_element(*ReconciliationPageControls.receivedDateLabel)

    def get_startDateInputBox(self):
        return self.driver.find_element(*ReconciliationPageControls.startDateInputBox)

    def get_finishDateInputBox(self):
        return self.driver.find_element(*ReconciliationPageControls.finishDateInputBox)

    def get_searchByTextLabel(self):
        return self.driver.find_element(*ReconciliationPageControls.searchByTextLabel)

    def get_searchByTextCriteriaLabel(self):
        return self.driver.find_element(*ReconciliationPageControls.searchByTextCriteriaLabel)

    def get_searchInputText(self):
        return self.driver.find_element(*ReconciliationPageControls.searchInputText)

    def get_receivedDate(self):
        return self.driver.find_elements(*ReconciliationPageControls.receivedDate)

    def get_reconcileUnprocessedRecordsButton(self):
        return self.driver.find_element(*ReconciliationPageControls.reconcileUnprocessedRecordsButton)

    def get_reconcileUnprocessedRecordsPopUpTitle(self):
        return self.driver.find_element(*ReconciliationPageControls.reconcileUnprocessedRecordsPopUpTitle)

    def get_reconcileUnprocessedRecordPopUpBody(self):
        return self.driver.find_element(*ReconciliationPageControls.reconcileUnprocessedRecordPopUpBody)

    def get_reconcileUnprocessedRecordsPopUpCancelBtn(self):
        return self.driver.find_element(*ReconciliationPageControls.reconcileUnprocessedRecordsPopUpCancelBtn)

    def get_reconcileUnprocessedRecordPopUpSubmitBtn(self):
        return self.driver.find_element(*ReconciliationPageControls.reconcileUnprocessedRecordPopUpSubmitBtn)

    def get_unprocessedRecordOrderID(self):
        return self.driver.find_element(*ReconciliationPageControls.unprocessedRecordOrderID)

    def get_unprocessedRecordEditButton(self):
        return self.driver.find_element(*ReconciliationPageControls.unprocessedRecordEditButton)

    def get_updateUnprocessedRecordPopupLoadQty(self):
        return self.driver.find_element(*ReconciliationPageControls.updateUnprocessedRecordPopupLoadQty)

    def get_updateUnprocessedRecordPopupUnloadQty(self):
        return self.driver.find_element(*ReconciliationPageControls.updateUnprocessedRecordPopupUnloadQty)

    def get_updateUnprocessedRecordPopupTerminalRefID(self):
        return self.driver.find_element(*ReconciliationPageControls.updateUnprocessedRecordPopupTerminalRefID)

    def get_updateUnprocessedRecordPopupTitle(self):
        return self.driver.find_element(*ReconciliationPageControls.updateUnprocessedRecordPopupTitle)

    def get_unprocessedRecordTerminalRefID(self):
        return self.driver.find_element(*ReconciliationPageControls.unprocessedRecordTerminalRefID)

    def get_unprocessedRecordloadQty(self):
        return self.driver.find_element(*ReconciliationPageControls.unprocessedRecordloadQty)

    def get_unprocessedRecordUnloadQty(self):
        return self.driver.find_element(*ReconciliationPageControls.unprocessedRecordUnloadQty)

    def get_updateReconciledDataPopupTitle(self):
        return self.driver.find_element(*ReconciliationPageControls.updateReconciledDataPopupTitle)