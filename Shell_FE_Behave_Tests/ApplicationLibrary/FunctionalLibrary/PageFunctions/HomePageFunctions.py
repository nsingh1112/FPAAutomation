import time

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.HomePageControls import HomePageControls
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

class HomePageFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.homePageControls = HomePageControls(SeleniumBase.driver)

    def validate_applicationTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.homePageControls.get_applicationTitle())
        if FPASeleniumHelper.check_element_exists_by_xpath(
                self.homePageControls.get_applicationTitle()):
            SeleniumUtilities.log.info("Home Page title is correct")

        else:
            SeleniumUtilities.log.error("Home Page title is not correct")

    def validate_leftListItems(self):
        WaitUtilities.wait_for_element_to_be_visible(self.homePageControls.get_MenuItems())
        menuItems = self.homePageControls.get_MenuItems()
        for menu in menuItems:
            divName = menu.text
            self.get_subList(divName)

    def get_leftSubListItems(self,sublistItems):
        elementList = []
        x1 = len(sublistItems)
        for option in sublistItems:
            x2 = option.text
            elementList.append(x2)

        return elementList

    def get_subList(self, divName):
        """ Navigates to the desired page from any page
          :Args:
            - pageName - name of the page to be selected
        """
        elementList1 = []
        subelementList = []

        if divName == "DOCUMENTS":
            WaitUtilities.wait_for_element_to_be_visible(self.homePageControls.get_documentsMenuItems())
            options1 = self.homePageControls.get_documentsMenuItems()
            elementList1 =  self.get_leftSubListItems(options1)
            subelementList = ['Terminal Report','Invoices']

        elif divName == "RECONCILIATION":
            WaitUtilities.wait_for_element_to_be_visible(self.homePageControls.get_reconciliationMenuItems())
            options1 = self.homePageControls.get_reconciliationMenuItems()
            elementList1 = self.get_leftSubListItems(options1)
            subelementList = ['Unprocessed Records','Reconciled Data']

        elif divName == "ACTUALS PROCESSING":
            WaitUtilities.wait_for_element_to_be_visible(self.homePageControls.get_documentsMenuItems())
            options1 = self.homePageControls.get_actualProcessingMenuItems()
            elementList1 = self.get_leftSubListItems(options1)
            subelementList = ['Create', 'Manage Actuals', 'Actual Volumes']

        elif divName == "LOGS":
            WaitUtilities.wait_for_element_to_be_visible(self.homePageControls.get_logsMenuItems())
            options1 = self.homePageControls.get_logsMenuItems()
            elementList1 = self.get_leftSubListItems(options1)
            subelementList = ['Reconciliation', 'Reconciliation Errors', 'Actual\'s Errors']

        self.validate_subList(divName, elementList1, subelementList )

    def validate_subList(self, divName, elementList1, subelementList):
        if(elementList1 == subelementList):
            SeleniumUtilities.log.info("Elements verified for " +divName)

        else:
            SeleniumUtilities.log.error(
                "Elements verified for" +divName+ "Expected Element is" +subelementList+ "Actual Element is" +elementList1)
            raise TypeError("Element not matched for " +divName)

    def click_unprocessedRecord(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_linkUnprocessedRecord())
        FPASeleniumHelper.click_element(self.homePageControls.get_linkUnprocessedRecord())

    def click_unprocessed(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_unprocessed())
        FPASeleniumHelper.click_element(self.homePageControls.get_unprocessed())

    def click_reconciled(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_reconciled())
        FPASeleniumHelper.click_element(self.homePageControls.get_reconciled())

    def click_reprocessed(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_reprocessed())
        FPASeleniumHelper.click_element(self.homePageControls.get_reprocessed())

    def click_failedReconciliation(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_failedReconciliation())
        FPASeleniumHelper.click_element(self.homePageControls.get_failedReconciliation())

    def click_enteredInDEX(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_enteredInDEX())
        FPASeleniumHelper.click_element(self.homePageControls.get_enteredInDEX())

    def click_failedToEnterInDEX(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_failedToEnterInDEX())
        FPASeleniumHelper.click_element(self.homePageControls.get_failedToEnterInDEX())

    def click_terminalReport(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_terminalReport())
        FPASeleniumHelper.click_element(self.homePageControls.get_terminalReport())
        time.sleep(4)

    def click_invoices(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_invoices())
        FPASeleniumHelper.click_element(self.homePageControls.get_invoices())

    def click_unprocessedRecord(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_unprocessedRecord())
        FPASeleniumHelper.click_element(self.homePageControls.get_unprocessedRecord())

    def click_reconciledData(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_reconciledData())
        FPASeleniumHelper.click_element(self.homePageControls.get_reconciledData())

    def click_create(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_create())
        FPASeleniumHelper.click_element(self.homePageControls.get_create())


    def click_manageActuals(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_manageActuals())
        FPASeleniumHelper.click_element(self.homePageControls.get_manageActuals())

    def click_actualVolumes(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_actualVolumes())
        FPASeleniumHelper.click_element(self.homePageControls.get_actualVolumes())


    def click_reconcilation(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_reconciliation())
        FPASeleniumHelper.click_element(self.homePageControls.get_reconciliation())


    def click_reconciliationErrors(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_reconciliationErrors())
        FPASeleniumHelper.click_element(self.homePageControls.get_reconciliationErrors())

    def click_actualErrors(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.homePageControls.get_actualErrors())
        FPASeleniumHelper.click_element(self.homePageControls.get_actualErrors())



