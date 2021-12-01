from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from Shell_FE_Appium_Core.AppiumBase import AppiumBase


class WaitUtilities():

    #def __init__(self, driver):
        #self.driver = driver

    @staticmethod
    def implicit_wait(self,timeout):
        AppiumBase.driver.implicitly_wait(timeout)

    def wait_for_element(locator_type, locator_value):

        locator_type = locator_type.lower()
        element = None

        wait = WebDriverWait(AppiumBase.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        if locator_type == "id":
            element = wait.until(lambda x: x.find_element_by_id(locator_value))
            return element

        elif locator_type == "accessibility_id":
            element = wait.until(lambda x: x.find_element_by_accessibility_id(locator_value))
            return element

        elif locator_type == "class":
            element = wait.until(lambda x: x.find_element_by_class_name(locator_value))
            return element

        elif locator_type == "des":
            element = wait.until(
               lambda x: x.find_element_by_android_uiautomator('UiSelector().description("%s")' % locator_value))
            return element

        elif locator_type == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator("UiSelector().index(%d)" % int(locator_value)))
            return element

        elif locator_type == "text":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('text("%s")' % locator_value))
            return element

        elif locator_type == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath('%s' % locator_value))
            return element

        return element
