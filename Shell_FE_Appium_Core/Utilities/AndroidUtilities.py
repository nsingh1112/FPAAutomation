import time

from appium.webdriver import webelement
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities


class AndroidUtlities():

    #def __init__(self, driver):
        #self.driver = driver
    @staticmethod
    def click(locator_type, locator_value):
        locator_type = locator_type.lower()
        element = None
        '''need to implement the text, xpath and fix the class method'''
        if locator_type == 'accessibility_id':
            element = AppiumBase.driver.find_element_by_accessibility_id(locator_value)
            element.click()

        elif locator_type == 'id':
            element = AppiumBase.driver.find_element_by_id(locator_value)
            element.click()

        elif locator_type == 'class':
            element = AppiumBase.driver.find_element_by_class_name(locator_value)
            element.click()

        elif locator_type == 'xpath':
            element = AppiumBase.driver.find_element_by_xpath(locator_value)
            element.click()

        return element

    @staticmethod
    def isDisplayed(locator_type, locator_value):
        element = None
        try:
            locator_type = locator_type.lower()
            element = WaitUtilities.wait_for_element(locator_type, locator_value)
            element.is_displayed()
            return True

        except:
            return False

    @staticmethod
    def isEnabled(locator_type, locator_value):
        try:
            locator_type = locator_type.lower()
            element = WaitUtilities.wait_for_element(locator_type, locator_value)
            element.is_enabled()
            return True
        except:
            return False

    @staticmethod
    def getAttribute(elementid, attributeValue):
        element = AppiumBase.driver.find_element_by_accessibility_id(elementid)
        get_value = element.get_attribute(attributeValue)
        return get_value

    @staticmethod
    def is_selected(locator_type, locator_value):
        try:
            locator_type = locator_type.lower()
            element = WaitUtilities.wait_for_element(locator_type, locator_value)
            element.is_selected()
            return True
        except:
            return False

    @staticmethod
    def get_text(locatorValue):
        element = AppiumBase.driver.find_element_by_accessibility_id(locatorValue)
        textValue = element.text
        print("Value of the text :" + textValue)
        return textValue

    @staticmethod
    def send_keys( locatorType, locatorValue, textToBeAdd):
        element = AppiumBase.click(locatorType,locatorValue)
        element = AppiumBase.driver.find_element_by_id(locatorValue)
        element.send_keys(textToBeAdd)

    @staticmethod
    def take_Screenshot(screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            AppiumBase.driver.save_screenshot(screenshotPath)
            print("screen shot saved to the path " + screenshotPath)
        except:
            print("screen shot failed")

    @staticmethod
    def get_AppContext():
        contexts = AppiumBase.driver.contexts
        return contexts

    @staticmethod
    def press_KeyCode(key_value):
        element = AppiumBase.driver.press_keycode(key_value)
        return element
    @staticmethod
    def switch_Context(view_value):
        AppiumBase.driver.switch_to.context(view_value)
    @staticmethod
    def switch_ContextInList():
        contexts = AndroidUtlities.get_AppContext()
        for context in contexts:
            AppiumBase.driver.switch_to.context(context)
