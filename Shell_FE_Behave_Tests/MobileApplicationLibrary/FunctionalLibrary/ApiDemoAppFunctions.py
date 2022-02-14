from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Behave_Tests.MobileApplicationLibrary.ControlLibrary.ApiDemoAppControls import ApiDemoAppControls
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Appium_Core.Utilities.AssertUtilities import AssertUtilities
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities


class ShellApiDemos:
    log = LoggingUtilities()
    log_file = log.logger()

    def __init__(self):
        self.apiDemosControls = ApiDemoAppControls(AppiumBase.driver)

    def click_views(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.apiDemosControls.view_tab)
        text = AndroidUtilities.get_text(self.apiDemosControls.get_view_tab())
        AssertUtilities.assert_equals(text, "Views")
        AndroidUtilities.click_element(self.apiDemosControls.get_view_tab())
        AndroidUtilities.take_screenshot('Test_confirm')
        ShellApiDemos.log_file.info("Element clicked")

    def click_controls(self):
        WaitUtilities.wait_for_element_using_scroll_view("Controls")
        WaitUtilities.wait_for_element_to_be_clickable(self.apiDemosControls.control_tab)
        AndroidUtilities.is_element_displayed(self.apiDemosControls.get_controls_view())
        AndroidUtilities.click_element(self.apiDemosControls.get_controls_view())

    def click_checkbox(self):
        WaitUtilities.wait_element_to_be_visible(self.apiDemosControls.light_theme_tab)
        AndroidUtilities.click_element(self.apiDemosControls.get_light_theme())
        WaitUtilities.wait_for_value_to_be_present(self.apiDemosControls.check_box, "Checkbox 1")
        AndroidUtilities.click_element(self.apiDemosControls.get_checkbox())

    def check_back_button(self):
        AndroidUtilities.click_back_button()
        WaitUtilities.wait_element_to_be_visible(self.apiDemosControls.light_theme_tab)
        AndroidUtilities.click_back_button()
        WaitUtilities.wait_element_to_be_visible(self.apiDemosControls.control_tab)

    def check_drag_and_drop(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.apiDemosControls.drag_and_drop)
        AndroidUtilities.click_element(self.apiDemosControls.get_drag_and_drop_tab())
        WaitUtilities.wait_element_to_be_visible(self.apiDemosControls.source_element)
        AndroidUtilities.drag_and_drop(self.apiDemosControls.get_source_element(),self.apiDemosControls.get_target_element())
        WaitUtilities.wait_element_to_be_visible(self.apiDemosControls.result_text)
        print("############Result Text #####", AndroidUtilities.get_text(self.apiDemosControls.get_result_text()))

    def check_scroll(self):
        WaitUtilities.wait_element_to_be_visible(self.apiDemosControls.drag_and_drop)
        AndroidUtilities.scroll_to_text("TextSwitcher")
        AndroidUtilities.click_element(self.apiDemosControls.get_text_switcher())

    def check_tap(self):
        WaitUtilities.wait_element_to_be_visible(self.apiDemosControls.next_btn)
        AndroidUtilities.tap_element(self.apiDemosControls.get_next_btn())
