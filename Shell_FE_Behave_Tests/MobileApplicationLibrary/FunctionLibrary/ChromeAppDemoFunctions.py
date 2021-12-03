from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtlities
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Behave_Tests.MobileApplicationLibrary.ControlLibrary.ChromeAppDemoControls import HybridAppControls


class HybridAppFunctions:

    def __init__(self):
        self.appFunctions = HybridAppControls()

    def open_Chrome(self):
        AndroidUtlities.click(self.appFunctions.id, self.appFunctions.accept_Terms)
        # WaitUtilities.wait_for_element(self.appFunctions.id, self.appFunctions.next_Btn)
        # AndroidUtlities.click(self.appFunctions.id,self.appFunctions.next_Btn)
        WaitUtilities.wait_for_element(self.appFunctions.id,self.appFunctions.positive_Btn)
        AndroidUtlities.click(self.appFunctions.id,self.appFunctions.positive_Btn)

    def click_search_Box(self):
        WaitUtilities.wait_for_element(self.appFunctions.id,self.appFunctions.search_Box)
        AndroidUtlities.click(self.appFunctions.id,self.appFunctions.search_Box)

    def send_Value(self,search_text):
        AndroidUtlities.send_keys(self.appFunctions.search_URL,search_text)
        AndroidUtlities.press_KeyCode(66)

    def get_AppViews(self):
        app_context = AndroidUtlities.get_currentAppContext()
        return app_context

    def switching_View(self,context_value):
        AndroidUtlities.switch_Context(context_value)

    def click_image_tab(self):
        AndroidUtlities.click(self.appFunctions.xpath,self.appFunctions.image_Tab_View)

    def remove_text(self):
        AndroidUtlities.click(self.appFunctions.xpath,self.appFunctions.search_by_xpath)
        AndroidUtlities.clear_text(self.appFunctions.xpath,self.appFunctions.search_by_xpath)

    def replace_value(self,text_to_be_replaced):
        AndroidUtlities.send_keys_by_xpath(self.appFunctions.search_by_xpath,text_to_be_replaced)







