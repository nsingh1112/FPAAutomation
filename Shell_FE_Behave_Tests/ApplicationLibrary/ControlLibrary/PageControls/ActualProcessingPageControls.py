from selenium.webdriver.common.by import By


class ActualProcessingPageControls:

    def __init__(self, driver):
        self.driver = driver

    createPageTitle = (By.XPATH, "//span[text()='Actuals Processing']/following::span[text()='Create Actuals']")
    createPageAggregateLabel = (By.XPATH, "//span[text()='Aggregate']")
    createPageAggregateDataLabel = (By.XPATH, "//span[text()='Aggregated Data']")
    manageActualsPageTitle = (By.XPATH, "//span[text()='Actuals Processing']/following::span[text()='Manage Actuals']")
    manageVolumesPageTitle = (By.XPATH, "//span[text()='Actuals Processing']/following::span[text()='Actual Volumes']")
    rowHeader = (By.XPATH, "//div[@class='shell-table-header']/table/thead/tr/th")
    bolDateLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='BOL Date']")
    startDateInputBox = (By.XPATH, "//input[@placeholder='Start date']")
    finishDateInputBox = (By.XPATH, "//input[@placeholder='Finish date']")
    searchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::label[text()='Search By Text']")
    createSearchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::span[text()='Contract Id, Discharge Date']")
    manageActualsSearchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::span[text()='Dex Parcel Id, Contract Id, BOL Date, Buyer, Seller']")
    actualVolumeSearchByTextLabel = (By.XPATH, "//*[local-name()='svg' and @class='sc-gsnTZi hDCash shell-icon']/following::span[text()='Dex Parcel Id']")
    searchInputText = (By.XPATH, "//input[@placeholder='Search By Text']")
    createActualsButton = (By.XPATH, "//span[@class='sc-ksZaOG kwPwYx' and  text()='Create Actuals (All)']")
    createActualsPopUpTitle = (By.XPATH, "//strong[text()='Create Actuals']")
    createActualsPopUpBody = (By.XPATH, "//div[text()='Are you sure you want to create actuals for all aggregated data?']")
    createActualsPopUpCancelBtn = (By.XPATH, "//button[@class='sc-papXJ iFkojq shell-button']/span[text()='Cancel']")
    createActualsPopUpSubmitBtn = (By.XPATH, "//button[@class='sc-papXJ gfyoCe shell-button']/span[text()='Submit']")

    def get_createPageTitle(self):
        return self.driver.find_element(*ActualProcessingPageControls.createPageTitle)

    def get_createPageAggregateLabel(self):
        return self.driver.find_element(*ActualProcessingPageControls.createPageAggregateLabel)

    def get_createPageAggregateDataLabel(self):
        return self.driver.find_element(*ActualProcessingPageControls.createPageAggregateDataLabel)

    def get_manageActualsPageTitle(self):
        return self.driver.find_element(*ActualProcessingPageControls.manageActualsPageTitle)

    def get_manageVolumesPageTitle(self):
        return self.driver.find_element(*ActualProcessingPageControls.manageVolumesPageTitle)

    def get_rowHeader(self):
        return self.driver.find_elements(*ActualProcessingPageControls.rowHeader)

    def get_bolDateLabel(self):
        return self.driver.find_element(*ActualProcessingPageControls.bolDateLabel)

    def get_startDateInputBox(self):
        return self.driver.find_element(*ActualProcessingPageControls.startDateInputBox)

    def get_finishDateInputBox(self):
        return self.driver.find_element(*ActualProcessingPageControls.finishDateInputBox)

    def get_searchByTextLabel(self):
        return self.driver.find_element(*ActualProcessingPageControls.searchByTextLabel)

    def get_createSearchByTextLabel(self):
        return self.driver.find_element(*ActualProcessingPageControls.createSearchByTextLabel)

    def get_manageActualsSearchByTextLabel(self):
        return self.driver.find_element(*ActualProcessingPageControls.manageActualsSearchByTextLabel)

    def get_actualVolumeSearchByTextLabel(self):
        return self.driver.find_element(*ActualProcessingPageControls.actualVolumeSearchByTextLabel)

    def get_searchInputText(self):
        return self.driver.find_element(*ActualProcessingPageControls.searchInputText)

    def get_createActualsButton(self):
        return self.driver.find_element(*ActualProcessingPageControls.createActualsButton)

    def get_createActualsPopUpTitle(self):
        return self.driver.find_element(*ActualProcessingPageControls.createActualsPopUpTitle)

    def get_createActualsPopUpBody(self):
        return self.driver.find_element(*ActualProcessingPageControls.createActualsPopUpBody)

    def get_createActualsPopUpCancelBtn(self):
        return self.driver.find_element(*ActualProcessingPageControls.createActualsPopUpCancelBtn)

    def get_createActualsPopUpSubmitBtn(self):
        return self.driver.find_element(*ActualProcessingPageControls.createActualsPopUpSubmitBtn)




