from appium.webdriver import webelement
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class AndroidUtlities:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator_type, locator_value):
        locator_type = locator_type.lower()
        element = None
        if locator_type == 'accessibility_id':
            element = self.driver.find_element_by_accessibility_id(locator_value)
            element.click()

        return element
