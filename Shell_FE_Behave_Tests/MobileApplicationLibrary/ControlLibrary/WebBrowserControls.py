from appium.webdriver.common.mobileby import MobileBy


class BrowserControls:

    def __init__(self, driver):
        self.driver = driver

    user_name = (MobileBy.XPATH,"//input[@type='email']")
    next_btn  = (MobileBy.XPATH,"//input[@type='submit']")
    authentication_text = (MobileBy.LINK_TEXT," Select Authentication System")


    def get_username(self):
        return self.driver.find_element(*BrowserControls.user_name)

    def get_next_btn(self):
        return self.driver.find_element(*BrowserControls.next_btn)

