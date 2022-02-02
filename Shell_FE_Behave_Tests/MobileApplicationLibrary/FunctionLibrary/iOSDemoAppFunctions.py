from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Behave_Tests.MobileApplicationLibrary.ControlLibrary.iOSDemoAppControls import IOSDemoControls
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Appium_Core.Utilities.iOSUtilities import IOSUtilities


class IOSDemoFunction:
    log = LoggingUtilities()
    log_file = log.logger()

    def __init__(self):
        self.iOSFunctions = IOSDemoControls(AppiumBase.driver)

    def open_alert(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.iOSFunctions.alert_view)
        IOSUtilities.click_element(self.iOSFunctions.get_alert_view())

    def simple_alert(self):
        WaitUtilities.wait_element_to_be_visible(self.iOSFunctions.simple_alert)
        IOSUtilities.click_element(self.iOSFunctions.get_simple_alert())
        WaitUtilities.wait_element_to_be_visible(self.iOSFunctions.okay_button)
        IOSUtilities.click_element(self.iOSFunctions.get_okay_btn())

    def okay_cancel_alert(self):
        WaitUtilities.wait_element_to_be_visible(self.iOSFunctions.okay_cancel_btn)
        IOSUtilities.click_element(self.iOSFunctions.get_okay_cancel_btn())
        WaitUtilities.wait_for_element_to_be_clickable(self.iOSFunctions.okay_button)
        IOSUtilities.click_element(self.iOSFunctions.get_okay_btn())

    def multiple_choice_alert(self):
        WaitUtilities.wait_element_to_be_visible(self.iOSFunctions.multiple_choice)
        IOSUtilities.tap_element(self.iOSFunctions.get_other_alert())
        WaitUtilities.wait_for_element_to_be_clickable(self.iOSFunctions.choice_btn)
        IOSUtilities.tap_element(self.iOSFunctions.get_choice_btn())

    def text_entry_alert(self):
        WaitUtilities.wait_element_to_be_visible(self.iOSFunctions.text_entry_alert)
        IOSUtilities.click_element(self.iOSFunctions.get_text_entry())
        WaitUtilities.wait_element_to_be_visible(self.iOSFunctions.text_field)
        IOSUtilities.send_text_to_element(self.iOSFunctions.get_text_field(),"FE Automation Team")
        IOSUtilities.clear_text(self.iOSFunctions.get_text_field())
        IOSUtilities.tap_element(self.iOSFunctions.get_okay_btn())

    def confirm_cancel_alert(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.iOSFunctions.confirm_cancel_btn)
        IOSUtilities.tap_element(self.iOSFunctions.get_confirm_cancel_btn())
        WaitUtilities.wait_element_to_be_visible(self.iOSFunctions.confirm_btn)
        IOSUtilities.click_element(self.iOSFunctions.get_confirm_btn())

    def home_page(self):
        IOSUtilities.click_back_button()
        WaitUtilities.wait_element_to_be_visible(self.iOSFunctions.alert_view)



