from Shell_FE_Appium_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Behave_Tests.MobileApplicationLibrary.ControlLibrary.ApiDemoAppControls import ApiDemoAppControls
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Appium_Core.Utilities.AssertUtilities import AssertUtilities
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtlities


class ShellApiDemos:
    log = LoggingUtilities()
    log_file=log.logger()

    def __init__(self):
        self.apiDemosControls = ApiDemoAppControls()


    def click_Views(self):
        WaitUtilities.wait_for_element(self.apiDemosControls.accessibility, self.apiDemosControls.views)
        text = AndroidUtlities.get_text(self.apiDemosControls.views)
        AssertUtilities.assertEquals(text, self.apiDemosControls.views)
        AndroidUtlities.click(self.apiDemosControls.accessibility, self.apiDemosControls.views)
        AndroidUtlities.take_Screenshot('Test')
        ShellApiDemos.log_file.info("Element clicked")


    def click_Controls(self):
        AndroidUtlities.isDisplayed(self.apiDemosControls.accessibility, self.apiDemosControls.controls)
        AndroidUtlities.click(self.apiDemosControls.accessibility, self.apiDemosControls.controls)

    def click_CheckBox(self):
        AndroidUtlities.click(self.apiDemosControls.accessibility,self.apiDemosControls.light_Theme)
        WaitUtilities.wait_for_element(self.apiDemosControls.accessibility,self.apiDemosControls.check_Box)
        AndroidUtlities.click(self.apiDemosControls.accessibility,self.apiDemosControls.check_Box)
