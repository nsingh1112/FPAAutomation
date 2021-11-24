from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.TutorialsPointObjects import TutorialsPointObjects
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities


class TutorialsPointFunctions:

    def __init__(self):
        self.tutorialsPointObj = TutorialsPointObjects(SeleniumBase.driver)

    def access_tutorialspoint(self, url):
        BrowserUtilities.navigate_to_url(url)

    def enter_first_name(self, first_name):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.first_name)
        SeleniumUtilities.send_text(self.tutorialsPointObj.get_first_name(), first_name)

    def enter_last_name(self, last_name):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.last_name)
        SeleniumUtilities.clear_text(self.tutorialsPointObj.get_last_name())
        SeleniumUtilities.send_text(self.tutorialsPointObj.get_last_name(), last_name)

    def retrieve_first_name_label(self):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.first_name)
        first_name_label = SeleniumUtilities.get_text(self.tutorialsPointObj.get_first_name_label())
        return first_name_label

    def copy_value_from_first_name(self):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.first_name)
        SeleniumUtilities.copy_value_from_textbox(self.tutorialsPointObj.get_first_name())

    def paste_value_into_last_name(self):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.first_name)
        SeleniumUtilities.paste_value_into_textbox(self.tutorialsPointObj.get_last_name())

    def retrieve_value_from_last_name_js(self):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.last_name)
        last_name = SeleniumUtilities.get_value_using_javascript_executor(self.tutorialsPointObj.get_last_name())
        return last_name

    def clear_first_name_using_actions(self):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.first_name)
        SeleniumUtilities.clear_text_using_keys(self.tutorialsPointObj.get_first_name())

    def copy_paste_value(self):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.first_name)
        WaitUtilities.wait_for_element_to_be_clickable(self.tutorialsPointObj.first_name)
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.last_name)
        WaitUtilities.wait_for_element_to_be_clickable(self.tutorialsPointObj.last_name)
        SeleniumUtilities.copy_value_from_textbox_and_paste(self.tutorialsPointObj.get_last_name(),
                                                            self.tutorialsPointObj.get_first_name())

    def retrieve_value_from_last_name(self):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.first_name)
        last_name = SeleniumUtilities.get_attribute(self.tutorialsPointObj.get_last_name(), "value")
        return last_name

    def clear_last_name(self):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.last_name)
        SeleniumUtilities.clear_text(self.tutorialsPointObj.get_last_name())

    def enter_first_name_using_js(self, first_name):
        WaitUtilities.wait_for_element_to_be_present(self.tutorialsPointObj.first_name)
        SeleniumUtilities.send_text_using_javascript_executor(self.tutorialsPointObj.get_first_name(), first_name)

    def enter_last_name_using_actions(self, last_name):
        WaitUtilities.wait_for_element_to_be_present(self.tutorialsPointObj.last_name)
        SeleniumUtilities.send_text_by_actions(self.tutorialsPointObj.get_last_name(), last_name)

    def retrieve_yoe_label(self):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.yoe_label)
        yoe_label = SeleniumUtilities.get_text_using_javascript_executor(self.tutorialsPointObj.get_yoe_label())
        return yoe_label

    def select_male(self):
        WaitUtilities.wait_for_element_to_be_present(self.tutorialsPointObj.sex_male)
        WaitUtilities.wait_for_element_to_be_clickable(self.tutorialsPointObj.sex_male)
        SeleniumUtilities.select_radiobutton(self.tutorialsPointObj.get_sex_male())

    def validate_selection_male(self):
        WaitUtilities.wait_for_element_to_be_selected(self.tutorialsPointObj.get_sex_male())
        result = SeleniumUtilities.is_element_selected(self.tutorialsPointObj.get_sex_male())
        return result

    def validate_enabled_female(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.tutorialsPointObj.sex_female)
        result = SeleniumUtilities.is_element_enabled(self.tutorialsPointObj.get_sex_female())
        return result

    def validate_selection_female(self):
        WaitUtilities.wait_for_element_to_be_selected(self.tutorialsPointObj.get_sex_female())
        result = SeleniumUtilities.is_element_selected(self.tutorialsPointObj.get_sex_female())
        return result

    def select_manual_tester(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.tutorialsPointObj.manual_tester)
        SeleniumUtilities.select_checkbox(self.tutorialsPointObj.get_manual_tester())

    def select_automation_tester(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.tutorialsPointObj.automation_tester)
        SeleniumUtilities.click_element(self.tutorialsPointObj.get_automation_tester())

    def unselect_automation_tester(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.tutorialsPointObj.automation_tester)
        SeleniumUtilities.unselect_checkbox(self.tutorialsPointObj.get_automation_tester())

    def validate_automation_tester_selection(self):
        return SeleniumUtilities.is_element_selected(self.tutorialsPointObj.get_automation_tester())

    def select_yoe_five(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.tutorialsPointObj.yoe_five)
        SeleniumUtilities.click_element_by_actions(self.tutorialsPointObj.get_yoe_five())

    def select_yoe_seven(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.tutorialsPointObj.yoe_seven)
        SeleniumUtilities.click_element_using_javascript_executor(self.tutorialsPointObj.get_yoe_seven())

    def select_continent_text(self, continent_name):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.continents)
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.tutorialsPointObj.get_continents(),
                                                                  continent_name)

    def select_continent_value(self, continent_name):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.continents)
        SeleniumUtilities.select_from_dropdown_using_value(self.tutorialsPointObj.get_continents(), continent_name)

    def retrieve_selected_continent(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.tutorialsPointObj.continents)
        selected_value = SeleniumUtilities.get_selected_element_text_from_dropdown(
            self.tutorialsPointObj.get_continents())
        return selected_value

    def retrieve_attribute_male(self, attr):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.sex_male)
        attribute = SeleniumUtilities.get_attribute(self.tutorialsPointObj.get_sex_male(), attr)
        return attribute

    def retrieve_attribute_female(self, attr):
        WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.sex_female)
        attribute = SeleniumUtilities.get_attribute_using_javascript_executor(self.tutorialsPointObj.get_sex_female(),
                                                                              attr)
        return attribute

    def update_attribute_male(self, attr, new_value):
        # WaitUtilities.wait_for_element_to_be_visible(self.tutorialsPointObj.sex_male)
        SeleniumUtilities.update_attribute_using_javascript_executor(self.tutorialsPointObj.get_sex_male(), attr,
                                                                     new_value)

    def retrieve_color_male(self, attr):
        color = SeleniumUtilities.get_css(self.tutorialsPointObj.get_first_name_label(), attr)
        return color
