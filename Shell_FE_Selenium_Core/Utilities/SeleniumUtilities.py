from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase


class SeleniumUtilities:
    """SeleniumUtilities class contains reusable methods for common Selenium user actions"""

    def __init__(self):
        print("Constructor")

    # region Reusable methods for performing common user actions in Selenium
    @staticmethod
    def click_element(web_element):
        """Clicks the Element.

        :Args:
            - web_element - The web element to be clicked.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        web_element.click()

    @staticmethod
    def send_text(web_element, text):
        """Passes the value to the text field.

        :Args:
            - web_element - The web element where value needs to be passed.
            - text - The value to be passed to text field. Value would be converted to string and passed.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        web_element.send_keys(str(text))

    @staticmethod
    def clear_text(web_element):
        """Clears the text field.

        :Args:
            - web_element - The web element of the field to be cleared.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        web_element.clear()

    @staticmethod
    def is_element_selected(web_element):
        """Verifies if the element is selected.

        :Args:
            - web_element - The web element to be checked.

        :Returns:
            - True if element is selected.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        if web_element.is_selected():
            return True
        else:
            return False

    @staticmethod
    def is_element_displayed(web_element):
        """Verifies if the element is visible.

        :Args:
            - web_element - The web element to be checked.

        :Returns:
            - True if element is visible.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        if web_element.is_displayed():
            return True
        else:
            return False

    @staticmethod
    def is_element_enabled(web_element):
        """Verifies if the element is enabled.

        :Args:
            - web_element - The web element to be checked.

        :Returns:
            - True if element is enabled.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        if web_element.is_enabled():
            return True
        else:
            return False

    @staticmethod
    def select_from_dropdown_using_value(web_element, value):
        """Selects option from dropdown using value.

        :Args:
            - web_element - The web element of the dropdown to be clicked.
            - value - The value of the option to be selected.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        select = Select(web_element)
        select.select_by_value(value)

    @staticmethod
    def select_from_dropdown_using_visible_text(web_element, value):
        """Selects option from dropdown using visible text.

        :Args:
            - web_element - The web element of the dropdown to be clicked.
            - value - The visible text of the option to be selected.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        select = Select(web_element)
        select.select_by_visible_text(value)

    @staticmethod
    def get_selected_element_from_dropdown(web_element):
        """Retrieves the selected element from dropdown.

        :Args:
            - web_element - The web element of the dropdown to be interacted with.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        select = Select(web_element)
        return select.first_selected_option()

    @staticmethod
    def select_checkbox(web_element):
        """Selects the checkbox if it is already unchecked.

        :Args:
            - web_element - The web element of the checkbox to be selected.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        if not SeleniumUtilities.is_element_selected(web_element):
            SeleniumUtilities.click_element(web_element)

    @staticmethod
    def deselect_checkbox(web_element):
        """Unselects the checkbox if it is already checked.

        :Args:
            - web_element - The web element of the checkbox to be unselected.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        if SeleniumUtilities.is_element_selected(web_element):
            SeleniumUtilities.click_element(web_element)

    @staticmethod
    def select_radiobutton(web_element):
        """Selects the radio button if it is unselected.

        :Args:
            - web_element - The web element of the radio button to be selected.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        if not SeleniumUtilities.is_element_selected(web_element):
            SeleniumUtilities.click_element(web_element)

    @staticmethod
    def deselect_radiobutton(web_element):
        """Unselects the radio button if it is selected.

        :Args:
            - web_element - The web element of the radio button to be unselected.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        if SeleniumUtilities.is_element_selected(web_element):
            SeleniumUtilities.click_element(web_element)

    @staticmethod
    def get_text(web_element):
        """Retrieves the inner text of the text field.

        :Args:
            - web_element - The web element of the text field whose text needs to be retrieved.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        return web_element.text

    @staticmethod
    def get_attribute(web_element, attr):
        """Retrieves the required attribute's value of element.

        :Args:
            - web_element - The web element of the field whose attribute value needs to be retrieved.
        """
        if web_element is None or attr is None:
            raise TypeError("Empty or invalid argument passed!!")
        if isinstance(attr, str) is False:
            raise ValueError("Attribute should be a string value!!")
        return web_element.get_attribute(attr)

    # endregion

    # region Reusable methods for user actions performed using ActionChains
    @staticmethod
    def move_focus_to_element(web_element):
        """Moves the focus to element using Actions.

        :Args:
            - web_element - The web element to be interacted.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(web_element).perform()

    @staticmethod
    def click_element_by_actions(web_element):
        """Clicks the element using Actions.

        :Args:
            - web_element - The web element to be clicked.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(web_element).click(web_element).perform()

    @staticmethod
    def send_text_by_actions(web_element, text):
        """Sends text to the element using Actions.

        :Args:
            - web_element - The web element to be interacted with.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(web_element).click(web_element).send_keys(str(text)).perform()

    @staticmethod
    def drag_drop_element_by_coordinates(web_element, x_offset, y_offset):
        """Drags and drops an element via coordinates using Actions.

        :Args:
            - web_element - The web element to be moved.
            - x-offset - The x-axis value
            - y-offset - The y-axis value
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        if isinstance(x_offset, int) is False or isinstance(y_offset, int) is False:
            raise ValueError("Integer value should be passed as offset!!")
        action = ActionChains(SeleniumBase.driver)
        action.drag_and_drop_by_offset(web_element, x_offset, y_offset).perform()

    @staticmethod
    def drag_drop_element(source_web_element, target_web_element):
        """Drags and drops an element to new location using Actions.

        :Args:
            - source_web_element - The web element to be moved.
            - target_web_element - The web element of the target location
        """
        if source_web_element is None or target_web_element is None:
            raise TypeError("Empty or invalid argument passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.drag_and_drop(source_web_element, target_web_element).perform()

    @staticmethod
    def double_click(web_element):
        """Performs mouse double click on the element using Actions.

        :Args:
            - web_element - The web element to be clicked.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.double_click(web_element).perform()

    @staticmethod
    def right_click(web_element):
        """Performs mouse right click on the element using Actions.

        :Args:
            - web_element - The web element to be clicked.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.context_click(web_element).perform()

    @staticmethod
    def clear_text_using_keys(web_element):
        """Clears the contents of element.

        :Args:
            - web_element - The web element to be cleared.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(web_element).click(web_element).key_down(Keys.CONTROL).send_keys('A').key_up(
            Keys.CONTROL).key_down(Keys.DELETE).pause(1000).key_up(Keys.DELETE).perform()

    @staticmethod
    def copy_value_from_textbox(web_element):
        """Copy value from text field into clipboard using key actions.

        :Args:
            - web_element - The web element to be interacted with.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(web_element).click(web_element).key_down(Keys.CONTROL).send_keys('A').key_up(
            Keys.CONTROL).key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()

    @staticmethod
    def paste_value_into_textbox(web_element):
        """Paste value from clipboard into text field using key actions.

        :Args:
            - web_element - The web element to be interacted with.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(web_element).click(web_element).key_down(Keys.CONTROL).send_keys('A').key_up(
            Keys.CONTROL).key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform()

    @staticmethod
    def copy_value_from_textbox_and_paste(source_web_element, target_web_element):
        """Copy value from a text field and pastes copied value into another text field using key actions.

        :Args:
            - source_web_element - The web element of the text field whose contents need to be copied.
            - target_web_element - The web element of the text field into which the contents need to be pasted.
        """
        if source_web_element is None or target_web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(source_web_element).click(source_web_element).key_down(Keys.CONTROL).send_keys(
            'A').key_up(
            Keys.CONTROL).key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()
        action.move_to_element(target_web_element).click(target_web_element).key_down(Keys.CONTROL).send_keys(
            'A').key_up(Keys.CONTROL).key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform()

    # endregion

    # region Reusable methods for actions performed using Javascript executor
    @staticmethod
    def click_element_using_javascript_executor(web_element):
        """Clicks the element using Javascript executor.

        :Args:
            - web_element - The web element to be clicked.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        SeleniumBase.driver.execute_script("arguments[0].click();", web_element)

    @staticmethod
    def send_text_using_javascript_executor(web_element, text):
        """Sends text value to the element using Javascript executor after converting text value to string.

        :Args:
            - web_element - The web element to be interacted with.
            - text - The text value to be passed
        """
        if web_element is None or text is None:
            raise TypeError("Empty or invalid argument passed!!")
        text_input = str(text)
        SeleniumBase.driver.execute_script("arguments[0].value='text_input';", web_element)
        # SeleniumBase.driver.execute_script("arguments[0].value=arguments[1];", web_element, text_input)
        # SeleniumBase.driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", web_element, text_input)

    @staticmethod
    def get_text_using_javascript_executor(web_element):
        """Retrieves the inner text of the text field using Javascript executor.

        :Args:
            - web_element - The web element of the text field whose text needs to be retrieved.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        SeleniumBase.driver.execute_script("return arguments[0].innerText;", web_element)

    @staticmethod
    def get_value_using_javascript_executor(web_element):
        """Retrieves the value of element using Javascript executor.

        :Args:
            - web_element - The web element of the field whose value needs to be retrieved.
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        SeleniumBase.driver.execute_script("return arguments[0].value;", web_element)

    @staticmethod
    def get_attribute_using_javascript_executor(web_element, attr):
        """Retrieves the required attribute's value using Javascript executor.

        :Args:
            - web_element - The web element of the field whose attribute value needs to be retrieved.
            - attr - The attribute whose value needs to be retrieved
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        SeleniumBase.driver.execute_script("return arguments[0].getAttribute(arguments[1]);", web_element, attr)

    @staticmethod
    def update_attribute_using_javascript_executor(web_element, attribute, new_value):
        """Updates the value of required attribute of an element using Javascript executor.

        :Args:
            - web_element - The web element of the field whose attribute value needs to be retrieved.
            - attribute - The attribute whose value needs to be updated
            - new_value - The value that needs to be updated
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        # SeleniumBase.driver.execute_script("arguments[0].setAttribute(attribute, new_value);", web_element)
        SeleniumBase.driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", web_element)
        SeleniumBase.driver.execute_script("arguments[0]." + attribute + "=arguments[1];", web_element, new_value)

    @staticmethod
    def scroll_to_element(web_element):
        """Scrolls the webpage until the element is displayed.

        :Args:
            - web_element - The web element up to which the web page needs to be scrolled..
        """
        if web_element is None:
            raise TypeError("Empty or invalid Web element passed!!")
        SeleniumBase.driver.execute_script("arguments[0].scrollIntoView(true);", web_element)
        # SeleniumBase.driver.execute_script("return arguments[0].scrollIntoView(true);", web_element)

    @staticmethod
    def scroll_window(scroll_value):
        """Scrolls the window up or down based on coordinate passed.

        :Args:
            - scroll_value - The coordinate value up to which the window need to be scrolled
        """
        if scroll_value is None:
            raise TypeError("Empty or invalid Web element passed!!")
        SeleniumBase.driver.execute_script("window.scrollBy(0," + scroll_value + ")")

    # endregion
