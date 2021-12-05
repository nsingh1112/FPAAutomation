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
        WaitUtilities.wait_for_element(self.apiDemosControls.accessibility, self.apiDemosControls.views)
        text = AndroidUtilities.get_text(self.apiDemosControls.views)
        AssertUtilities.assert_equals(text, self.apiDemosControls.views)
        AndroidUtilities.click_by_mobileBy(self.apiDemosControls.open_view_tab())
        #AndroidUtilities.click(self.apiDemosControls.accessibility, self.apiDemosControls.views)
        AndroidUtilities.take_screenshot('Test')
        ShellApiDemos.log_file.info("Element clicked")

    def click_controls(self):
        AndroidUtilities.is_element_displayed(self.apiDemosControls.accessibility, self.apiDemosControls.controls)
        AndroidUtilities.click(self.apiDemosControls.accessibility, self.apiDemosControls.controls)

    def click_checkbox(self):
        AndroidUtilities.click(self.apiDemosControls.accessibility, self.apiDemosControls.light_Theme)
        WaitUtilities.wait_for_element(self.apiDemosControls.accessibility, self.apiDemosControls.check_Box)
        AndroidUtilities.click(self.apiDemosControls.accessibility, self.apiDemosControls.check_Box)
