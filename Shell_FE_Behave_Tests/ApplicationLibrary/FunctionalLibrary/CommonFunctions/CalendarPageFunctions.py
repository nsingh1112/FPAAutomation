import time

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.CommonControls.CalendarPageControls import \
    CalendarPageControls
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.HomePageControls import HomePageControls
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper
from Shell_FE_Behave_Tests.Utilities.FPAWaitHelper import FPAWaitHelper
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

class CalendarPageFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.calendarPageControls = CalendarPageControls(SeleniumBase.driver)

    def select_startDateyear(self,yearToSelect, selYear):
        WaitUtilities.wait_for_element_to_be_visible(self.calendarPageControls.get_firstCalanderYear())
        x = self.calendarPageControls.get_firstCalanderYear().text
        yeardiff = int(yearToSelect) - int(x)
        self.select_calanderYear(yearToSelect, yeardiff, selYear)

    def select_finishDateyear(self,yearToSelect,selYear):
        WaitUtilities.wait_for_element_to_be_visible(self.calendarPageControls.get_secondCalanderYear())
        x = self.calendarPageControls.get_secondCalanderYear().text
        yeardiff = int(yearToSelect) - int(x)
        self.select_calanderYear(yearToSelect, yeardiff,selYear)

    def select_calanderYear(self, yearToSelect, yeardiff, selYear):
        if (yeardiff != 0):
            if(selYear == "startDate"):
               SeleniumUtilities.click_element(self.calendarPageControls.get_firstCalanderYear())
               WaitUtilities.wait_for_element_to_be_visible(self.calendarPageControls.get_yearSelections())
            else:
                SeleniumUtilities.click_element(self.calendarPageControls.get_secondCalanderYear())
                WaitUtilities.wait_for_element_to_be_visible(self.calendarPageControls.get_yearSelections())
            SelectionWindowStartingYear = self.calendarPageControls.get_yearSelectionWindowFirstYear().text
            SelectionWindowLastYear = self.calendarPageControls.get_yearSelectionWindowLastYear().text

            if (int(SelectionWindowStartingYear) > int(yearToSelect)):
                SeleniumUtilities.click_element(self.calendarPageControls.get_yearSelectionWindowPreviousButton())
                WaitUtilities.wait_for_element_to_be_visible(
                    self.calendarPageControls.get_yearSelectionWindowFirstYear())

            elif (int(SelectionWindowLastYear) < int(yearToSelect)):
                SeleniumUtilities.click_element(self.calendarPageControls.get_yearSelectionWindowNextButton())
                WaitUtilities.wait_for_element_to_be_visible(
                    self.calendarPageControls.get_yearSelectionWindowFirstYear())

            yearList = self.calendarPageControls.get_yearSelections()
            for year in yearList:
                divName = year.text
                if (divName == yearToSelect):
                    year.click()
                    break

    def select_month(self, monthToSelect):
        month = "May"
        if(monthToSelect == "startDateMonth"):
            SeleniumUtilities.click_element(self.calendarPageControls.get_firstCalanderMonth())
        #else:
           # SeleniumUtilities.click_element(self.calendarPageControls.get_secondCalanderMonth())
        month = self.driver.find_element_by_xpath(
            "//div[@class='shell-date-picker-cell-inner' and text()='" + month + "']")
        SeleniumUtilities.click_element(month)

    def select_date2(self):
        dateToSelect = "11"
        date = self.driver.find_element_by_xpath(
            "(//div[@class='shell-date-picker-cell-inner' and text()='" + dateToSelect + "'])[2]")
        SeleniumUtilities.click_element(date)

    def select_date(self):
        dateToSelect = "11"
        date = self.driver.find_element_by_xpath(
            "//div[@class='shell-date-picker-cell-inner' and text()='" + dateToSelect + "']")
        SeleniumUtilities.click_element(date)


    def click_calendarDate(self):
        startDateYear = "2022"
        monthToSelect = "May"
        self.select_startDateyear(startDateYear, "startDate")
        self.select_month("startDateMonth")
        self.select_date()

        finishDateYear = "2023"
        monthToSelect = "May"
        self.select_finishDateyear(finishDateYear, "finishDate")
        self.select_month("finishDateMonth")
        self.select_date2()




