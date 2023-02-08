from selenium.webdriver.common.by import By

class CalendarPageControls:


    def __init__(self, driver):
        self.driver = driver

    firstCalanderYear = (By.XPATH, "(//button[@class='shell-date-picker-year-btn'])[1]")
    firstCalanderMonth = (By.XPATH, "(//button[@class='shell-date-picker-month-btn'])[1]")
    previousButton = (By.XPATH, "(//button[@class='shell-date-picker-header-prev-btn'])[1]")
    secondCalanderYear = (By.XPATH, "(//button[@class='shell-date-picker-year-btn'])[2]")
    secondCalanderMonth = (By.XPATH, "(//button[@class='shell-date-picker-month-btn'])[2]")
    nextButton = (By.XPATH, "(//button[@class='shell-date-picker-header-next-btn'])[2]")
    yearSelectionWindow = (By.XPATH, "//div[@class='shell-date-picker-cell-inner']")
    yearSelectionWindowFirstYear = (By.XPATH, "(//div[@class='shell-date-picker-cell-inner'])[1]")
    yearSelectionWindowLastYear = (By.XPATH, "(//div[@class='shell-date-picker-cell-inner'])[12]")
    yearSelectionWindowPrevious = (By.XPATH, "//button[@class='shell-date-picker-header-super-prev-btn']")
    yearSelectionWindowNext = (By.XPATH, "//button[@class='shell-date-picker-header-super-next-btn']")

    def get_firstCalanderYear(self):
        return self.driver.find_element(*CalendarPageControls.firstCalanderYear)

    def get_firstCalanderMonth(self):
        return self.driver.find_element(*CalendarPageControls.firstCalanderMonth)

    def get_secondCalanderYear(self):
        return self.driver.find_element(*CalendarPageControls.secondCalanderYear)

    def get_secondCalanderMonth(self):
        return self.driver.find_element(*CalendarPageControls.secondCalanderMonth)

    def get_previousButton(self):
        return self.driver.find_element(*CalendarPageControls.previousButton)

    def get_nextButton(self):
        return self.driver.find_element(*CalendarPageControls.nextButton)

    def get_yearSelections(self):
        return self.driver.find_elements(*CalendarPageControls.yearSelectionWindow)

    def get_yearSelectionWindowFirstYear(self):
        return self.driver.find_element(*CalendarPageControls.yearSelectionWindowFirstYear)

    def get_yearSelectionWindowLastYear(self):
        return self.driver.find_element(*CalendarPageControls.yearSelectionWindowLastYear)

    def get_yearSelectionWindowPreviousButton(self):
        return self.driver.find_element(*CalendarPageControls.yearSelectionWindowPrevious)

    def get_yearSelectionWindowNextButton(self):
        return self.driver.find_element(*CalendarPageControls.yearSelectionWindowNext)



