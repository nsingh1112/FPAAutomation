from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, \
    StaleElementReferenceException, NoSuchFrameException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase


class WaitUtilities:

    @staticmethod
    def wait_for_element_to_be_visible(by_locator, timeout=10):
        """Waits for element to be present in DOM and visible.

        :Args:
            - by_locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An ElementNotVisibleException if element is not visible within the specified time.
        """
        if by_locator is None:
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(SeleniumBase.driver, timeout).until(ec.visibility_of_element_located(by_locator))
        except ElementNotVisibleException as err:
            print("Element {0} is not visible. Exception: {1}".format(by_locator, err))

    @staticmethod
    def wait_for_element_to_be_present(by_locator, timeout=10):
        """Waits for element to be present in DOM.

        :Args:
            - by_locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An Exception if element is not loaded in DOM within the specified time.
        """
        if by_locator is None:
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(SeleniumBase.driver, timeout).until(ec.presence_of_element_located(by_locator))
        except Exception as err:
            print("Element {0} is not present. Exception: {1}".format(by_locator, err))

    @staticmethod
    def wait_for_element_to_be_clickable(by_locator, timeout=10):
        """Waits for element to be enabled.

        :Args:
            - by_locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An Exception if element is not enabled within the specified time.
        """
        if by_locator is None:
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(SeleniumBase.driver, timeout).until(ec.element_to_be_clickable(by_locator))
        except Exception as err:
            print("Element {0} is not clickable. Exception: {1}".format(by_locator, err))

    @staticmethod
    def wait_for_element_to_be_selected(web_element, timeout=10):
        """Waits for element to be selected.

        :Args:
            - by_locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An ElementNotSelectableException if element is not selected within the specified time.
        """
        if web_element is None:
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(SeleniumBase.driver, timeout).until(ec.element_to_be_selected(web_element))
        except ElementNotSelectableException as err:
            print("Element {0} is not selectable. Exception: {1}".format(web_element, err))

    @staticmethod
    def wait_for_element_to_be_invisible(by_locator, timeout=10):
        """Waits for element to be not present in the DOM.

        :Args:
            - by_locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An Exception if element is not invisible within the specified time.
        """
        if by_locator is None:
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(SeleniumBase.driver, timeout).until(ec.invisibility_of_element_located(by_locator))
        except Exception as err:
            print("Element {0} is visible. Exception: {1}".format(by_locator, err))

    @staticmethod
    def wait_for_element_to_be_stale(web_element, timeout=10):
        """Waits for element to become stale.

        :Args:
            - web_element - The element to be checked for staleness.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An Exception if element is not stale within the specified time.
        """
        if web_element is None:
            raise TypeError("Empty or invalid locator passed!!")
        if WebDriverWait(SeleniumBase.driver, timeout).until(ec.staleness_of(web_element)):
            return True
        else:
            raise Exception("Element {0} is attached to DOM. Element is not stale!!".format(web_element))

    @staticmethod
    def wait_for_element_to_be_stale_and_handle_it(web_element, by_locator, timeout=10):
        """Waits for a stale element to be visible within the specified time.

        :Args:
            - web_element - The element to be checked for staleness.
            - by_locator - The locator of the element to be checked for visibility.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An StaleElementReferenceException if element is still stale invisible after the specified time.
        """
        if web_element is None or by_locator is None:
            raise TypeError("Empty or invalid locator passed!!")
        try:
            if WebDriverWait(SeleniumBase.driver, timeout).until(ec.staleness_of(web_element)):
                WebDriverWait(SeleniumBase.driver, timeout).until(ec.visibility_of_element_located(by_locator))
        except StaleElementReferenceException as err:
            print("Element {0} is not attached to DOM. Element is stale!! Exception: {1}".format(by_locator, err))

    @staticmethod
    def wait_for_title_to_contain_value_and_assert(expected_value, timeout=10):
        """Waits for the title to contain the expected value.

        :Args:
            - expected_value - Expected value to be contained in title.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An AssertionError if the title does not contain the expected value.
        """
        if expected_value is None:
            raise ValueError("Empty or invalid Title passed as argument!!")
        try:
            WebDriverWait(SeleniumBase.driver, timeout).until(ec.title_contains(expected_value))
        except AssertionError as err:
            print("Title does not contain the value: {0}. Assertion failed!! Exception:{1}".format(expected_value, err))

    @staticmethod
    def wait_for_title_to_match_value_and_assert(expected_value, timeout=10):
        """Waits for the title to match the expected value.

        :Args:
            - expected_value - Expected value to be matched against title.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An AssertionError if the title does not match the expected value.
        """
        if expected_value is None:
            raise ValueError("Empty or invalid Title passed as argument!!")
        try:
            WebDriverWait(SeleniumBase.driver, timeout).until(ec.title_is(expected_value))
        except AssertionError as err:
            print("Title does not match the value: {0}. Assertion failed!! Exception: {1}".format(expected_value, err))

    @staticmethod
    def wait_for_url_to_contain_value_and_assert(expected_value, timeout=10):
        """Waits for the url to contain the expected value.

        :Args:
            - expected_value - Expected value to be contained in url.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An AssertionError if the url does not contain the expected value.
        """
        if expected_value is None:
            raise ValueError("Empty or invalid Title passed as argument!!")
        try:
            WebDriverWait(SeleniumBase.driver, timeout).until(ec.url_contains(expected_value))
        except AssertionError as err:
            print("Url does not contain the value: {0}. Assertion failed!! Exception: {1}".format(expected_value, err))

    @staticmethod
    def wait_for_url_to_match_value_and_assert(expected_value, timeout=10):
        """Waits for the url to match the expected value.

        :Args:
            - expected_value - Expected value to be matched against url.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An AssertionError if the url does not match the expected value.
        """
        if expected_value is None:
            raise ValueError("Empty or invalid Title passed as argument!!")
        try:
            WebDriverWait(SeleniumBase.driver, timeout).until(ec.url_to_be(expected_value))
        except AssertionError as err:
            print("Url does not match the value: {0}. Assertion failed!! Exception: {1}".format(expected_value, err))

    @staticmethod
    def wait_for_text_to_be_present(by_locator, expected_text, timeout=10):
        """Waits for value to be present in the element's text.

        :Args:
            - by_locator - The locator of the element to be checked.
            - expected_text - Value to be matched in element's text.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An Exception if text is not present in element within the specified time.
        """
        if by_locator is None or expected_text is None:
            raise TypeError("Empty or invalid argument passed!!")
        try:
            WebDriverWait(SeleniumBase.driver, timeout).until(
                ec.text_to_be_present_in_element(by_locator, expected_text))
        except Exception as err:
            print("Text {0} not present in element {1}. Exception: {2}".format(expected_text, by_locator, err))

    @staticmethod
    def wait_for_value_to_be_present(by_locator, expected_text, timeout=10):
        """Waits for text to be present in the element's value attribute.

        :Args:
            - by_locator - The locator of the element to be checked.
            - expected_text - Value to be matched in element's value attribute.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An Exception if text is not present in element's value attribute within the specified time.
        """
        if by_locator is None or expected_text is None:
            raise TypeError("Empty or invalid argument passed!!")
        try:
            WebDriverWait(SeleniumBase.driver, timeout).until(
                ec.text_to_be_present_in_element_value(by_locator, expected_text))
        except Exception as err:
            print("Text {0} not present in element {1}. Exception: {2}".format(expected_text, by_locator, err))

    @staticmethod
    def wait_for_number_of_windows_to_match(expected_value, timeout=10):
        """Waits for the number of windows to match the expected value.

        :Args:
            - expected_value - Expected number of windows.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An AssertionError if the number of windows does not match the expected value.
        """
        if expected_value is None:
            raise TypeError("Empty or invalid value passed!!")
        if isinstance(expected_value, int) is False:
            raise ValueError("Number of windows value should be a number")
        try:
            WebDriverWait(SeleniumBase.driver, timeout).until(ec.number_of_windows_to_be(expected_value))
        except AssertionError as err:
            print("Number of windows available does not match the expected value: {0}".format(expected_value))

    @staticmethod
    def wait_for_alert_to_be_present(timeout=10):
        """Waits for alert to be present.

        :Args:
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An Exception if alert is not present within specified time.
        """
        if WebDriverWait(SeleniumBase.driver, timeout).until(ec.alert_is_present()):
            return True
        else:
            raise Exception("Alert is not displayed!!")

    @staticmethod
    def wait_for_frame_and_switch(by_locator, timeout=10):
        """Waits for frame to be available.

        :Args:
            - by_locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.

        :Raises:
            An NoSuchFrameException if frame is not available within the specified time.
        """
        if by_locator is None:
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(SeleniumBase.driver, timeout).until(ec.frame_to_be_available_and_switch_to_it(by_locator))
        except NoSuchFrameException as err:
            print("Frame {0} is not available".format(by_locator))
