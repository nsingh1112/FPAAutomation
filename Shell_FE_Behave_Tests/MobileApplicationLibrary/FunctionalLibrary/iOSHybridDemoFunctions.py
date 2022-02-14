from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Behave_Tests.MobileApplicationLibrary.ControlLibrary.iOSHybridDemoControls import IOSSafariControls
from Shell_FE_Appium_Core.Utilities.iOSUtilities import IOSUtilities


class HybridAppFunctions:

    def __init__(self):
        self.safariFunction = IOSSafariControls(AppiumBase.driver)

    def click_search(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.safariFunction.search_bar)
        IOSUtilities.click_element(self.safariFunction.get_search_bar())

    def get_context_of_app(self):
        contexts = IOSUtilities.get_app_contexts()
        return contexts

    def pass_value_to_search_field(self,text_to_send):
        WaitUtilities.wait_for_element_to_be_clickable(self.safariFunction.text_field)
        IOSUtilities.click_element(self.safariFunction.get_text_field())
        IOSUtilities.send_text_to_element(self.safariFunction.get_text_field(),text_to_send)
        IOSUtilities.tap_element_by_coordinate(342, 635)

    def switch_app_view(self,view):
        IOSUtilities.switch_context(view)

    def current_contex(self):
        context = IOSUtilities.get_current_context()
        return context




