from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Behave_Tests.MobileApplicationLibrary.ControlLibrary.HybridAppDemoControls import HybridAppControls


class HybridAppFunctions:

    def __init__(self):
        self.appFunctions = HybridAppControls(AppiumBase.driver)

    def open_chrome(self):
        AndroidUtilities.click_element(self.appFunctions.get_accept_and_terms())
        # WaitUtilities.wait_for_element(self.appFunctions.id, self.appFunctions.next_Btn)
        # AndroidUtlities.click(self.appFunctions.id,self.appFunctions.next_Btn)
        WaitUtilities.wait_element_to_be_visible(self.appFunctions.by_positive_btn)
        AndroidUtilities.click_element(self.appFunctions.get_finish_btn())

    def click_search_box(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.appFunctions.search_box)
        AndroidUtilities.click_element(self.appFunctions.get_search_box())

    def click_search_url(self):
        AndroidUtilities.click_element(self.appFunctions.get_search_url())

    def send_value(self,search_text):
        AndroidUtilities.send_text_to_element(self.appFunctions.get_search_url(), search_text)
        AndroidUtilities.press_keycode(66)

    def higlight_view(self):
        AndroidUtilities.highlight_field(self.appFunctions.get_search_url())

    def get_app_views(self):
        app_context = AndroidUtilities.get_current_context()
        return app_context

    def switching_view(self,context_value):
        AndroidUtilities.switch_context(context_value)

    def click_image_tab(self):
        AndroidUtilities.click_element(self.appFunctions.get_image_tab())

    def remove_text(self):
        AndroidUtilities.click_element(self.appFunctions.get_after_search_box())
        AndroidUtilities.clear_text(self.appFunctions.get_after_search_box())

    def replace_value(self,text_to_be_replaced):
        AndroidUtilities.send_text_to_element(self.appFunctions.get_search_by_name(), text_to_be_replaced)







