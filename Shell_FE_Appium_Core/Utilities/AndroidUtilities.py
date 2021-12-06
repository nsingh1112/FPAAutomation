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
    def click_element(element):
        """Clicks the Element.
            :Args:
                - web_element - The web element to be clicked.
         """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: click_element(element)")
            raise TypeError("Empty or invalid  element passed!!")
        element.click()
        AndroidUtilities.log.info("Clicked on the element.")

    @staticmethod
    def send_text_to_element(element, text_to_be_added):
        """Passes the value to the text field
           :Args:
                - element - The element where value needs to be passed
                - text_to_be_add - The value to be passed to the text field. Value would be converted to string and passed
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: send_text_to_element(element)")
            raise TypeError("Empty or invalid element passed!!")
        element.send_keys(str(text_to_be_added))
        AndroidUtilities.log.info("Send text {0} to the element.".format(text_to_be_added))

    @staticmethod
    def clear_text(element):
        """Clears the text field
           :Args:
              -element - The element of the field to be cleared
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: clear_text(element)")
            raise TypeError("Empty or invalid element passed!!")
        element.clear()
        AndroidUtilities.log.info("Cleared the field")

    @staticmethod
    def is_element_displayed(element):
        """Checks for the element is displayed
           :Args:
                      -element - The element to be checked
           :Returns:
                      - True if the element is displayed
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: is_element_displayed(element)")
            raise TypeError("Empty or invalid element passed!!")
        if element.is_displayed():
            AndroidUtilities.log.info("Element displayed Successfully")
            return True
        else:
            AndroidUtilities.log.info("Element is not displayed")
            return False

    @staticmethod
    def is_element_enabled(element):
        """Checks for the element is Enabled
        :Args:
             -element - The element to be checked
        :Returns:
             - True if the element is displayed
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: is_element_enabled(element)")
            raise TypeError("Empty or invalid element passed!!")
        if element.is_enabled():
            AndroidUtilities.log.info("Element Enabled Successfully")
            return True
        else:
            AndroidUtilities.log.info("Element is not Enabled")
            return False

    @staticmethod
    def is_element_selected(element):
        """Checks for the element to select
        :Args:
             -element - The element to be selected
        :Returns:
             - True if the element is selected
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: is_element_selected(element)")
            raise TypeError("Empty or invalid element passed!!")
        if element.is_selected():
            AndroidUtilities.log.info("Element selected Successfully")
            return True
        else:
            AndroidUtilities.log.info("Element is not selected")
            return False

    @staticmethod
    def get_attribute(element, attribute):
        """Return the value of the attribute
           :Args:
                -element - The element to get the value
                -attribute - The attribute value to be retrieved from the element
        """
        if element is None or attribute is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: get_attribute(element,attribute)")
            raise TypeError("Empty or invalid element passed!!")
        if isinstance(attribute, str) is False:
            AndroidUtilities.log.error(
                "Attribute: {0} should be passed as a string value to the method: get_attribute(element, attribute)".format(
                    attribute))
            raise ValueError("Attribute should be a string value!!")
        return element.get_attribute(attribute)

    @staticmethod
    def get_text(element):
        """Return the value of the attribute
           :Args:
                -element - Value of the element to be retrieved
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: get_attribute(element,attribute)")
            raise TypeError("Empty or invalid element passed!!")
        return element.text

    @staticmethod
    def take_screenshot(screenshot_name):
        """Takes screenshot of the web page and saves it in the Screenshots folder under TestResults."""
        time_format = str(time.strftime("%d_%m_%H_%S")).replace("_", "")
        filename = screenshot_name + "_" + time_format + ".png"
        screenshot_path = AndroidUtilities.screenshots + filename
        AppiumBase.driver.save_screenshot(screenshot_path)
        AndroidUtilities.log.info("Took screenshot and saved as {0} in screenshots folder.".format(filename))

    @staticmethod
    def get_current_context():
        """It will get the current context of the App"""
        context = AppiumBase.driver.current_context
        AndroidUtilities.log.info("Current context of the is {0}.".format(context))
        return context

    @staticmethod
    def get_app_contexts():
        """It will get all the available contexts of the App"""
        contexts = AppiumBase.driver.contexts
        return contexts

    @staticmethod
    def press_keycode(key_value):
        """Press the mobil key for the corresponding value
           :args:
               -key_value - Pass the integer value to be pressed
        """
        element = AppiumBase.driver.press_keycode(key_value)
        AndroidUtilities.log.info("key has been pressed")
        return element

    @staticmethod
    def switch_context(switch_view):
        """Switches the view of the app
            :args:
                 - switch_view- value of the app to be switched
        """
        AppiumBase.driver.switch_to.context(switch_view)

    @staticmethod
    def switch_context_in_list(context_value):
        """Switches to the context in list"""
        contexts = AndroidUtilities.get_app_contexts()
        AppiumBase.driver.switch_to.context[context_value]
        # for context in contexts:
        #     AppiumBase.driver.switch_to.context[context]

