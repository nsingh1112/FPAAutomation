import os
import time

from appium.webdriver import webelement
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities


class AndroidUtilities:
    current_working_directory = os.path.dirname(os.getcwd())
    screenshots = current_working_directory + "\\Shell_FE_Behave_Tests\\TestResults\\Screenshots\\"
    logobj = LoggingUtilities()
    log = logobj.logger()

    @staticmethod
    def click_by_mobileBy(element):
        """Clicks the Element.

                :Args:
                    - web_element - The web element to be clicked.
                """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: click_element(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        element.click()
        AndroidUtilities.log.info("Clicked on the element.")

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
    def clear_text(locator_type, locator_value):
        locator_type = locator_type.lower()
        element = None
        '''need to implement the text, xpath and fix the class method'''
        if locator_type == 'accessibility_id':
            element = AppiumBase.driver.find_element_by_accessibility_id(locator_value)
            element.clear()

        elif locator_type == 'id':
            element = AppiumBase.driver.find_element_by_id(locator_value)
            element.clear()

        elif locator_type == 'class':
            element = AppiumBase.driver.find_element_by_class_name(locator_value)
            element.clear()

        elif locator_type == 'xpath':
            element = AppiumBase.driver.find_element_by_xpath(locator_value)
            element.clear()

        elif locator_type == 'name':
            element = AppiumBase.driver.find_element_by_name(locator_value)
            element.clear()

        return element

    @staticmethod
    def is_element_displayed(locator_type, locator_value):
        element = None
        try:
            locator_type = locator_type.lower()
            element = WaitUtilities.wait_for_element(locator_type, locator_value)
            element.is_displayed()
            return True

        except:
            return False

    @staticmethod
    def is_element_enabled(locator_type, locator_value):
        try:
            locator_type = locator_type.lower()
            element = WaitUtilities.wait_for_element(locator_type, locator_value)
            element.is_enabled()
            return True
        except:
            return False

    @staticmethod
    def get_attribute(element_id, attribute_value):
        element = AppiumBase.driver.find_element_by_accessibility_id(element_id)
        get_value = element.get_attribute(attribute_value)
        return get_value

    @staticmethod
    def is_element_selected(locator_type, locator_value):
        try:
            locator_type = locator_type.lower()
            element = WaitUtilities.wait_for_element(locator_type, locator_value)
            element.is_selected()
            return True
        except:
            return False

    @staticmethod
    def get_text(locator_value):
        element = AppiumBase.driver.find_element_by_accessibility_id(locator_value)
        text_value = element.text
        print("Value of the text :" + text_value)
        return text_value

    @staticmethod
    def send_keys_by_xpath(locator_value, text_to_Add):
        element = AppiumBase.driver.find_element_by_xpath(locator_value)
        element.send_keys(text_to_Add)

    @staticmethod
    def send_keys(locator_value, text_to_add):
        # element = AppiumBase.click(locatorType,locatorValue)
        element = AppiumBase.driver.find_element_by_id(locator_value)
        element.send_keys(text_to_add)

    @staticmethod
    def take_screenshot(screenshot_name):
        time_format = str(time.strftime("%d_%m_%H_%S")).replace("_", "")
        filename = screenshot_name + "_" + time_format + ".png"
        screenshot_path = AndroidUtilities.screenshots + filename
        try:
            AppiumBase.driver.save_screenshot(screenshot_path)
            print("screen shot saved to the path " + screenshot_path)
        except:
            print("screen shot failed")

    @staticmethod
    def get_current_context():
        context = AppiumBase.driver.current_context
        return context

    @staticmethod
    def get_app_contexts():
        contexts = AppiumBase.driver.contexts
        return contexts

    @staticmethod
    def press_keycode(key_value):
        element = AppiumBase.driver.press_keycode(key_value)
        return element

    @staticmethod
    def switch_context(view_value):
        AppiumBase.driver.switch_to.context(view_value)

    @staticmethod
    def switch_context_in_list():
        contexts = AndroidUtilities.get_app_contexts()
        for context in contexts:
            AppiumBase.driver.switch_to.context(context)
