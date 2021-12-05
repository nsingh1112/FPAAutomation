from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Behave_Tests.MobileApplicationLibrary.ControlLibrary.ChromeAppDemoControls import HybridAppControls


class HybridAppFunctions:

    def __init__(self):
        self.appFunctions = HybridAppControls()

    def open_chrome(self):
        AndroidUtilities.click(self.appFunctions.id, self.appFunctions.accept_Terms)
        # WaitUtilities.wait_for_element(self.appFunctions.id, self.appFunctions.next_Btn)
        # AndroidUtlities.click(self.appFunctions.id,self.appFunctions.next_Btn)
        WaitUtilities.wait_for_element(self.appFunctions.id,self.appFunctions.positive_Btn)
        AndroidUtilities.click(self.appFunctions.id, self.appFunctions.positive_Btn)

    def click_search_box(self):
        WaitUtilities.wait_for_element(self.appFunctions.id,self.appFunctions.search_Box)
        AndroidUtilities.click(self.appFunctions.id, self.appFunctions.search_Box)

    def send_value(self,search_text):
        AndroidUtilities.send_keys(self.appFunctions.search_URL, search_text)
        AndroidUtilities.press_keycode(66)

    def get_app_views(self):
        app_context = AndroidUtilities.get_current_context()
        return app_context

    def switching_view(self,context_value):
        AndroidUtilities.switch_context(context_value)

    def click_image_tab(self):
        AndroidUtilities.click(self.appFunctions.xpath, self.appFunctions.image_Tab_View)

    def remove_text(self):
        AndroidUtilities.click(self.appFunctions.xpath, self.appFunctions.search_by_xpath)
        AndroidUtilities.clear_text(self.appFunctions.xpath, self.appFunctions.search_by_xpath)

    def replace_value(self,text_to_be_replaced):
        AndroidUtilities.send_keys_by_xpath(self.appFunctions.search_by_xpath, text_to_be_replaced)







