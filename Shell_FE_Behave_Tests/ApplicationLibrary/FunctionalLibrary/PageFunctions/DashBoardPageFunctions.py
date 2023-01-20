import time

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.DashboardPageControls import \
    DashboardPageControls
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.HomePageControls import HomePageControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper


class DashBoardPageFunctions:

    def __init__(self, driver):
        self.dashboardPageControls = DashboardPageControls(SeleniumBase.driver)


    def get_dashboardItems(self):
        actualDashBoarditems= []
        expectedDashBoarditems = ['Unprocessed', 'Reconciled', 'Reprocessed', 'Failed Reconciliation', 'Entered in DEX', 'Failed to enter in DEX']
        WaitUtilities.wait_for_element_to_be_visible(self.dashboardPageControls.get_dashboardItems())
        dashboardItems = self.dashboardPageControls.get_dashboardItems()
        for dashboardItem in dashboardItems:
            dashbrditemwithCount = (dashboardItem.text).split('\n')
            dashbrditem=(dashbrditemwithCount)[0]
            self.validate_dashboardItems(dashbrditem, expectedDashBoarditems)


    def validate_dashboardItems(self, dashbrditem, subelementList):
        if(dashbrditem in subelementList):
            SeleniumUtilities.log.info("Elements verified for Dashboard")

        else:
            SeleniumUtilities.log.error(
                "Elements verified for Dashboard Expected Element is" +subelementList+ "Actual Element is" +dashbrditem)
            raise TypeError("Element not matched for Dashboard")

    def validate_dashboardGraphicalRepresentation(self):
        if FPASeleniumHelper.check_element_exists_by_xpath( self.dashboardPageControls.get_dashboardGraphicalRep()):
            SeleniumUtilities.log.info("Dashboard Graphical representation is Present")

        else:
            SeleniumUtilities.log.error("Dashboard Graphical representation is not Present")

    def validate_darkMode(self):
        if FPASeleniumHelper.check_element_exists_by_xpath(self.dashboardPageControls.get_texDarkMode()):
            SeleniumUtilities.log.info("Dark Mode Text is Present")
            fontColor = self.dashboardPageControls.get_texDarkMode().value_of_css_property('color')
            FPASeleniumHelper.click_element(self.dashboardPageControls.get_btnDarkMode())
            darkModeFontColor = self.dashboardPageControls.get_texDarkMode().value_of_css_property('color')
            if(darkModeFontColor != fontColor):
                SeleniumUtilities.log.info("Dark Mode is displayed")
            else:
                SeleniumUtilities.log.error("Dark Mode is not Present")

        else:
            SeleniumUtilities.log.error("Dark Mode Text is not Present")