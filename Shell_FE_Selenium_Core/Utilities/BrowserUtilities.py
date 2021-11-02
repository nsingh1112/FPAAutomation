import os

from selenium.webdriver.common.alert import Alert
from datetime import datetime

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase


class BrowserUtilities:
    """BrowserUtilities class contains reusable methods for common browser related actions"""
    current_working_directory = os.path.dirname(os.getcwd())
    screenshots = current_working_directory + "\\Shell_FE_Behave_Tests\\TestResults\\Screenshots\\"

    def __init__(self):
        print("Constructor")

    @staticmethod
    def navigate_to_url(url):
        if url is None:
            raise Exception("Invalid or empty URL!!")
        SeleniumBase.driver.get(url)

    @staticmethod
    def navigate_back():
        SeleniumBase.driver.back()

    @staticmethod
    def navigate_forward():
        SeleniumBase.driver.forward()

    @staticmethod
    def refresh_page():
        SeleniumBase.driver.refresh()

    @staticmethod
    def get_current_url():
        return SeleniumBase.driver.current_url()

    @staticmethod
    def get_title():
        return SeleniumBase.driver.title

    @staticmethod
    def switch_to_child_window():
        child_window = SeleniumBase.driver.window_handles[1]
        SeleniumBase.driver.switch_to.window(child_window)

    @staticmethod
    def close_window():
        SeleniumBase.driver.close()

    @staticmethod
    def switch_to_parent_window():
        parent_window = SeleniumBase.driver.window_handles[0]
        SeleniumBase.driver.switch_to.window(parent_window)

    @staticmethod
    def switch_to_window_by_title(expected_title):
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
        if frame_value is None:
            raise TypeError("Empty or invalid argument passed!!")
        SeleniumBase.driver.switch_to.frame(frame_value)

    @staticmethod
    def accept_alert():
        alert = Alert(SeleniumBase.driver)
        alert.accept()

    @staticmethod
    def dismiss_alert():
        alert = Alert(SeleniumBase.driver)
        alert.dismiss()

    @staticmethod
    def send_text_alert(text):
        if text is None:
            raise TypeError("Empty argument passed!!")
        if isinstance(text, str) is False:
            raise ValueError("Value to be sent should be a string!!")
        alert = Alert(SeleniumBase.driver)
        alert.send_keys(text)

    @staticmethod
    def get_alert_text():
        alert = Alert(SeleniumBase.driver)
        return alert.text

    @staticmethod
    def take_screenshot_of_element(web_element):
        if web_element is None:
            raise TypeError("Empty or invalid argument passed!!")
        filename = web_element + str(datetime.timestamp(datetime.now())) + ".png"
        web_element.screenshot(BrowserUtilities.screenshots + filename)

    @staticmethod
    def take_screenshot():
        filename = str(datetime.timestamp(datetime.now())) + ".png"
        SeleniumBase.driver.save_screenshot(BrowserUtilities.screenshots + filename)

    @staticmethod
    def take_screenshot_base64():
        SeleniumBase.driver.get_screenshot_as_base64()

    @staticmethod
    def resize_browser(width, height):
        if isinstance(width, int) is False or isinstance(height, int) is False:
            raise ValueError("Width and Height should be a number!!")
        SeleniumBase.driver.set_window_size(width, height)
