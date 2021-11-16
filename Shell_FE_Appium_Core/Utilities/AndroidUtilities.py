import time

from appium.webdriver import webelement
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities


class AndroidUtlities:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator_type, locator_value):
        locator_type = locator_type.lower()
        element = None
        '''need to implement the text, xpath and fix the class method'''
        if locator_type == 'accessibility_id':
            element = self.driver.find_element_by_accessibility_id(locator_value)
            element.click()

        elif locator_type == 'id':
            element = self.driver.find_element_by_id(locator_value)
            element.click()

        elif locator_type == 'class':
            element = self.driver.find_element_by_class_name(locator_value)
            element.click()

    def isDisplayed(self, locator_type, locator_value):
        element = None
        try:
            locator_type = locator_type.lower()
            element = WaitUtilities.wait_for_element(locator_type, locator_value)
            element.is_displayed()
            return True

        except:
            return False

    def isEnabled(self,locator_type, locator_value):
        try:
            locator_type = locator_type.lower()
            element = WaitUtilities.wait_for_element(locator_type, locator_value)
            element.is_enabled()
            return True
        except:
            return False

    def getAttribute(self,elementid,attributeValue):
        element = self.driver.find_element_by_accessibility_id(elementid)
        get_value = element.get_attribute(attributeValue)
        return get_value

    def is_selected(self,locator_type,locator_value):
        try:
            locator_type = locator_type.lower()
            element = WaitUtilities.wait_for_element(locator_type, locator_value)
            element.is_selected()
            return True
        except:
            return False

    def get_text(self,locatorValue):
         element = self.driver.find_element_by_accessibility_id(locatorValue)
         textValue = element.text
         print("Value of the text :" + textValue)
         return textValue

    def send_keys(self,element_id,element_value):
        element = self.driver.find_element_by_accessibility_id(element_id)
        element.click()
        element.clear()
        element.send_keys(element_id,element_value)

    def take_Screenshot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            print("screen shot saved to the path " + screenshotPath)
        except:
            print("screen shot failed")
