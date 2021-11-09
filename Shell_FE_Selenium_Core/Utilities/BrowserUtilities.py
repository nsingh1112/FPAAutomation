import os

from selenium.webdriver.common.alert import Alert
from datetime import datetime

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase


class BrowserUtilities:
    """BrowserUtilities class contains reusable methods for common browser related actions"""
    current_working_directory = os.path.dirname(os.getcwd())
    screenshots = current_working_directory + "\\Shell_FE_Behave_Tests\\TestResults\\Screenshots\\"

    @staticmethod
    def navigate_to_url(url):
        """Navigates to the url specified.

        :Args:
            - url - The url to be navigated to.
        """
        if url is None:
            raise Exception("Invalid or empty URL!!")
        SeleniumBase.driver.get(url)

    @staticmethod
    def navigate_back():
        """Navigates back by one page."""
        SeleniumBase.driver.back()

    @staticmethod
    def navigate_forward():
        """Navigates forward by one page."""
        SeleniumBase.driver.forward()

    @staticmethod
    def refresh_page():
        """Refreshes the web page."""
        SeleniumBase.driver.refresh()

    @staticmethod
    def get_current_url():
        """Returns the current url."""
        return SeleniumBase.driver.current_url()

    @staticmethod
    def get_title():
        """Returns the current title."""
        return SeleniumBase.driver.title

    @staticmethod
    def switch_to_child_window():
        """Switches to the immediate child window."""
        child_window = SeleniumBase.driver.window_handles[1]
        SeleniumBase.driver.switch_to.window(child_window)

    @staticmethod
    def close_window():
        """Closes the driver instance (i.e.) the current browser tab / window."""
        SeleniumBase.driver.close()

    @staticmethod
    def switch_to_parent_window():
        """Switches to the parent window."""
        parent_window = SeleniumBase.driver.window_handles[0]
        SeleniumBase.driver.switch_to.window(parent_window)

    @staticmethod
    def switch_to_window_by_title(expected_title):
        """Navigates through available windows and switches focus to window by the title.

        :Args:
            - expected_title - The title of the window to be matched.
        """
        if expected_title is None:
            raise TypeError("Empty argument passed!!")
        if isinstance(expected_title, str) is False:
            raise ValueError("Title should be a string value!!")
        parent_window = SeleniumBase.driver.current_window_handle
        window_handles = SeleniumBase.driver.window_handles
        flag = False
        for window_handle in window_handles:
            SeleniumBase.driver.switch_to.window(window_handle)
            if SeleniumBase.driver.title == expected_title:
                flag = True
                break
        if not flag:
            SeleniumBase.driver.switch_to.window(parent_window)

    @staticmethod
    def switch_to_iframe(frame_value):
        """Switches to the frame.

        :Args:
            - frame_value - The value of frame (i.e.) frame name / index / locator.
        """
        if frame_value is None:
            raise TypeError("Empty or invalid argument passed!!")
        SeleniumBase.driver.switch_to.frame(frame_value)

    @staticmethod
    def accept_alert():
        """Accepts the alert."""
        alert = Alert(SeleniumBase.driver)
        alert.accept()

    @staticmethod
    def dismiss_alert():
        """Dismisses the alert."""
        alert = Alert(SeleniumBase.driver)
        alert.dismiss()

    @staticmethod
    def send_text_alert(text):
        """Sends text value to alert window.

        :Args:
            - text - The text to be sent to the alert window.
        """
        if text is None:
            raise TypeError("Empty argument passed!!")
        alert = Alert(SeleniumBase.driver)
        alert.send_keys(str(text))

    @staticmethod
    def get_alert_text():
        """Returns the text contained in alert"""
        alert = Alert(SeleniumBase.driver)
        return alert.text

    @staticmethod
    def take_screenshot_of_element(web_element):
        """Takes screenshot of the web element and saves it in the Screenshots folder under TestResults."""
        if web_element is None:
            raise TypeError("Empty or invalid argument passed!!")
        filename = web_element + str(datetime.timestamp(datetime.now())) + ".png"
        web_element.screenshot(BrowserUtilities.screenshots + filename)

    @staticmethod
    def take_screenshot():
        """Takes screenshot of the web page and saves it in the Screenshots folder under TestResults."""
        filename = str(datetime.timestamp(datetime.now())) + ".png"
        SeleniumBase.driver.save_screenshot(BrowserUtilities.screenshots + filename)

    @staticmethod
    def take_screenshot_base64():
        """Takes screenshot of the web page as base 64."""
        SeleniumBase.driver.get_screenshot_as_base64()

    @staticmethod
    def resize_browser(width, height):
        """Resize the browser based on the passed values.

        :Args:
            - width - The width of the browser to be set.
            - height - The height of the browser to be set.
        """
        if isinstance(width, int) is False or isinstance(height, int) is False:
            raise ValueError("Width and Height should be a number!!")
        SeleniumBase.driver.set_window_size(width, height)
