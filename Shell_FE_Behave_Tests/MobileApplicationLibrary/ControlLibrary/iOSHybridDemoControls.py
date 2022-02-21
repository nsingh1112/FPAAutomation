from appium.webdriver.common.mobileby import MobileBy


class IOSSafariControls:

    def __init__(self, driver):
        self.driver = driver

    search_bar = (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeCell[`name == "
                                            "'com.apple.mobilesafari.framework-customization-sectionContent"
                                            "'`]/XCUIElementTypeOther")

    text_field = (MobileBy.IOS_PREDICATE, "label == 'Address'")

    def get_search_bar(self):
        return self.driver.find_element(*IOSSafariControls.search_bar)

    def get_text_field(self):
        return self.driver.find_element(*IOSSafariControls.text_field)



