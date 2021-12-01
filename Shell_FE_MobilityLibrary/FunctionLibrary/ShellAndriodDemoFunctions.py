from Shell_FE_Appium_Core import AppiumBase
from Shell_FE_MobilityLibrary.ControlLibrary.ShellAndriodDemoControls import ApiDemoAppControls
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Appium_Core.Utilities.AssertUtilities import AssertUtilities
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtlities


class ShellApiDemos:
    def __init__(self):
        self.apiDemosControls = ApiDemoAppControls()

    def click_Views(self):
        WaitUtilities.wait_for_element(self.apiDemosControls.accessibility, self.apiDemosControls.views)
        text = AndroidUtlities.get_text(self.apiDemosControls.views)
        AssertUtilities.assertEquals(text, self.apiDemosControls.views)
        AndroidUtlities.click(self.apiDemosControls.accessibility, self.apiDemosControls.views)

    def click_Controls(self):
        AndroidUtlities.isDisplayed(self.apiDemosControls.accessibility, self.apiDemosControls.controls)
        AndroidUtlities.click(self.apiDemosControls.accessibility, self.apiDemosControls.controls)

    def click_CheckBox(self):
        AndroidUtlities.click(self.apiDemosControls.accessibility,self.apiDemosControls.light_Theme)
        WaitUtilities.wait_for_element(self.apiDemosControls.accessibility,self.apiDemosControls.check_Box)
        AndroidUtlities.click(self.apiDemosControls.accessibility,self.apiDemosControls.check_Box)
