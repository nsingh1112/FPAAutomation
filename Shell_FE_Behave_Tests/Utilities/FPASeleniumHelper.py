import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from selenium.common.exceptions import NoSuchElementException
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from selenium.webdriver.common.action_chains import ActionChains
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Behave_Tests.Utilities.DriverHelper import DriverHelper


class FPASeleniumHelper:

    @staticmethod
    def check_element_exists_by_xpath(element):
        """
            Checks whether element exists or not
        @rtype: Returns True if element exists or false if element doesn't exists
        """

        try:
            SeleniumUtilities.is_element_displayed(element)
        except NoSuchElementException:  # spelling error making this code not work as expected
            return False

        return True

    @staticmethod
    def scroll_to_element(web_element):
        """Scrolls the webpage until the element is displayed.

        :Args:
            - web_element - The web element up to which the web page needs to be scrolled..
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        SeleniumBase.driver.execute_script("arguments[0].scrollIntoView(true);", web_element)
        """Adding sleep of a second for DOM refresh after scroll"""
        time.sleep(2)

    @staticmethod
    def scroll_window(scroll_value):
        """Scrolls the window up or down based on coordinate passed.

        :Args:
            - scroll_value - The coordinate value up to which the window need to be scrolled
        """
        if scroll_value is None:
            raise TypeError("Empty or invalid argument passed!!")
        SeleniumBase.driver.execute_script("window.scrollBy(0," + scroll_value + ")")
        time.sleep(1)

    @staticmethod
    def move_focus_to_element(web_element):
        """Moves the focus to element using Actions.

        :Args:
            - web_element - The web element to be interacted.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: move_focus_to_element(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(web_element).perform()
        SeleniumUtilities.log.info("Moved focus to element using Action chains.")

    @staticmethod
    def send_text_using_javascript_executor(web_element, text):
        """Sends text value to the element using Javascript executor after converting text value to string.

        :Args:
            - web_element - The web element to be interacted with.
            - text - The text value to be passed
        """
        if web_element is None or text is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: send_text_using_javascript_executor(web_element, text)")
            raise TypeError("Empty or invalid argument passed!!")
        text_input = str(text)
        SeleniumBase.driver.execute_script("arguments[0].value=arguments[1];", web_element, text_input)
        # SeleniumBase.driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", web_element, text_input)
        SeleniumUtilities.log.info("Sent values: {0} to the field using Javascript executor.".format(text))

    # region Reusable methods for actions performed using Javascript executor
    @staticmethod
    def click_element_using_javascript_executor(web_element):
        """Clicks the element using Javascript executor.

        :Args:
            - web_element - The web element to be clicked.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: click_element_using_javascript_executor(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        SeleniumBase.driver.execute_script("arguments[0].click();", web_element)
        SeleniumUtilities.log.info("Clicked on the element using Javascript executor.")

    @staticmethod
    def send_text_by_actions(web_element, text):
        """Sends text to the element using Actions.

        :Args:
            - web_element - The web element to be interacted with.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: send_text_by_actions(web_element, text)")
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(web_element).click(web_element).send_keys(str(text)).perform()
        SeleniumUtilities.log.info("Sent text {0} to the element using Action Chains.".format(text))

    @staticmethod
    def click_element(web_element):
        """Clicks the Element.

        :Args:
            - web_element - The web element to be clicked.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: click_element(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        web_element.click()
        SeleniumUtilities.log.info("Clicked on the element.")

    @staticmethod
    def take_screenshot(file_name="Screenshot"):
        """Takes screenshot of the web page and saves it in the Screenshots folder under TestResults."""
        filename = file_name + str(time.strftime("%d_%m_%H_%S")).replace("_", "") + ".png"
        SeleniumBase.driver.save_screenshot(BrowserUtilities.screenshots + filename)
        BrowserUtilities.log.info("Took screenshot and saved as {0} in Screenshots folder.".format(filename))

    @staticmethod
    def page_is_loading():
        while True:
            x = SeleniumBase.driver.execute_script("return document.readyState")
            if x == "complete":
                return True
            else:
                return False

    @staticmethod
    def send_text(web_element, text):
        """Passes the value to the text field.

            Args:
                - web_element - The web element where value needs to be passed.
                - text - The value to be passed to text field. Value would be converted to string and passed.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: send_text(web_element, text)")
            raise TypeError("Empty or invalid Web element passed!!")
        web_element.send_keys(str(text))
        SeleniumUtilities.log.info("Sent text {0} to the element.".format(text))
