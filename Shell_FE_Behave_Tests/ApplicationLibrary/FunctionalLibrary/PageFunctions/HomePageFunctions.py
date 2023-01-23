from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.HomePageControls import HomePageControls
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper
from Shell_FE_Behave_Tests.Utilities.FPAWaitHelper import FPAWaitHelper
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

class HomePageFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.homePageControls = HomePageControls(SeleniumBase.driver)

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
            subelementList = ['Create', 'Manage Actuals']

        elif divName == "LOGS":
            WaitUtilities.wait_for_element_to_be_visible(self.homePageControls.get_logsMenuItems())
            options1 = self.homePageControls.get_logsMenuItems()
            elementList1 = self.get_leftSubListItems(options1)
            subelementList = ['Reconciliation', 'Reconciliation Errors', 'Actual\'s Errors']

        self.validate_subList(divName, elementList1, subelementList )

    def validate_subList(self, divName, elementList1, subelementList):
        if(elementList1 == subelementList):
            SeleniumUtilities.log.info("Elements verified for" +divName)

        else:
            SeleniumUtilities.log.error(
                "Elements verified for" +divName+ "Expected Element is" +subelementList+ "Actual Element is" +elementList1)
            raise TypeError("Element not matched for" +divName)

    def click_unprocessedRecord(self):
        FPAWaitHelper.wait_for_element_to_be_clickable(self.homePageControls.get_linkUnprocessedRecord(), 600)
        FPASeleniumHelper.click_element(self.homePageControls.get_linkUnprocessedRecord())

