from Shell_FE_Appium_Core import AppiumBase
from Shell_FE_Behave_Tests.MobileApplicationLibrary.ControlLibrary.WebBrowserControls import BrowserControls
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities

class BrowserFunctions:
    # def __init__(self):
    #     self.BrowserControls = BrowserControls(AppiumBase.driver)

    def launc_web(self,url):
        AndroidUtilities.navigate_to_url(url)
