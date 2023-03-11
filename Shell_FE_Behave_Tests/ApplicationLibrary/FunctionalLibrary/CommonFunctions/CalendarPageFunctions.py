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
        WaitUtilities.wait_for_element_to_be_visible(self.calendarPageControls.get_firstCalanderYear())
        x = self.calendarPageControls.get_firstCalanderYear().text
        yeardiff = int(yearToSelect) - int(x)
        return yeardiff

    def get_finishYearDiff(self, yearToSelect):
        WaitUtilities.wait_for_element_to_be_visible(self.calendarPageControls.get_secondCalanderYear())
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
                WaitUtilities.wait_for_element_to_be_visible(self.calendarPageControls.get_yearSelectionWindowPreviousButtons())
                SeleniumUtilities.click_element(self.calendarPageControls.get_yearSelectionWindowPreviousButton())
                WaitUtilities.wait_for_element_to_be_visible(
                    self.calendarPageControls.get_yearSelectionWindowFirstYear())

            elif (int(SelectionWindowLastYear) < int(yearToSelect)):
                WaitUtilities.wait_for_element_to_be_clickable(self.calendarPageControls.get_yearSelectionWindowNextButton())
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
        l1 = len(self.calendarPageControls.get_firstCalanderMonthCount())
        if(l1 > 0):
            WaitUtilities.wait_for_element_to_be_clickable(self.calendarPageControls.get_firstCalanderMonth())
            SeleniumUtilities.click_element(self.calendarPageControls.get_firstCalanderMonth())
        month = self.driver.find_element_by_xpath(
            "//div[@class='shell-date-picker-cell-inner' and text()='" + startmonth + "']")
        SeleniumUtilities.click_element(month)

    def select_finishMonth(self, finishmonth, yeardiff):
        l2 = len(self.calendarPageControls.get_secondCalanderMonthCount())
        if(l2 >0):
            WaitUtilities.wait_for_element_to_be_clickable(self.calendarPageControls.get_secondCalanderMonth())
            SeleniumUtilities.click_element(self.calendarPageControls.get_secondCalanderMonth())

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
        startDate = (startDateWithYear).split('-')
        startdateMon = self.num_to_month(startDate[1])
        yeardiff = self.get_startyeardiff(startDate[0])
        self.select_calanderYear(startDate[0], yeardiff, "startDate")
        self.select_startMonth(startdateMon, yeardiff)
        self.select_startdate(startDate[2].lstrip('0'))

        finishDate = (finishDateWithYear).split('-')
        yeardiff = self.get_finishYearDiff(finishDate[0])
        finishdateMon = self.num_to_month(finishDate[1])
        self.select_calanderYear(finishDate[0], yeardiff, "finishDate")
        self.select_finishMonth(finishdateMon, yeardiff)
        self.select_startdate(finishDate[2].lstrip('0'))

    def num_to_month(self, num):
        if int(num) <= 12 and int(num) > 0:

            list_of_months = {'01': 'Jan', '02': 'Feb', '03': 'Mar',
                              '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul',
                              '08': 'Aug', '09': 'Sep', '10': 'Oct',
                              '11': 'Nov', '12': 'Dec'}

            return list_of_months[num]

        else:
            print('num_to_month function error: "num=' + str(num) + '"')





