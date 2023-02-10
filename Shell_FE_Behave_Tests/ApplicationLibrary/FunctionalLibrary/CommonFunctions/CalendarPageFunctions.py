import time

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.CommonControls.CalendarPageControls import \
    CalendarPageControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities


class CalendarPageFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.calendarPageControls = CalendarPageControls(SeleniumBase.driver)

    def get_startyeardiff(self, yearToSelect):
        WaitUtilities.wait_for_element_to_be_visible(self.calendarPageControls.get_firstCalanderYear(),6000)
        x = self.calendarPageControls.get_firstCalanderYear().text
        yeardiff = int(yearToSelect) - int(x)
        return yeardiff

    def get_finishYearDiff(self, yearToSelect):
        WaitUtilities.wait_for_element_to_be_visible(self.calendarPageControls.get_secondCalanderYear(),6000)
        x = self.calendarPageControls.get_secondCalanderYear().text
        yeardiff = int(yearToSelect) - int(x)
        return yeardiff

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


    def select_startMonth(self, startmonth, yeardiff):
        SeleniumUtilities.click_element(self.calendarPageControls.get_firstCalanderMonth())
        month = self.driver.find_element_by_xpath(
            "//div[@class='shell-date-picker-cell-inner' and text()='" + startmonth + "']")
        SeleniumUtilities.click_element(month)

    def select_finishMonth(self, finishmonth, yeardiff):
        month = self.driver.find_element_by_xpath(
            "//div[@class='shell-date-picker-cell-inner' and text()='" + finishmonth + "']")
        SeleniumUtilities.click_element(month)

    def select_finishdate(self, finishdate):
        date = self.driver.find_element_by_xpath(
            "(//div[@class='shell-date-picker-cell-inner' and text()='" + finishdate + "'])[2]")
        SeleniumUtilities.click_element(date)

    def select_startdate(self, startdate):
        date = self.driver.find_element_by_xpath(
            "//div[@class='shell-date-picker-cell-inner' and text()='" + startdate + "']")
        SeleniumUtilities.click_element(date)


    def click_calendarDate(self, startDateWithYear, finishDateWithYear):
        startDate = (startDateWithYear).split(' ')
        yeardiff = self.get_startyeardiff(startDate[2])
        self.select_calanderYear(startDate[2], yeardiff, "startDate")
        self.select_startMonth(startDate[1], yeardiff)
        self.select_startdate(startDate[0])

        finishDate = (finishDateWithYear).split(' ')
        yeardiff = self.get_finishYearDiff(finishDate[2])
        self.select_calanderYear(finishDate[2], yeardiff, "finishDate")
        self.select_finishMonth(finishDate[1], yeardiff)
        self.select_startdate(finishDate[0])





