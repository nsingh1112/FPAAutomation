from appium.webdriver.common.mobileby import MobileBy

from Shell_FE_Appium_Core.AppiumBase import AppiumBase


class IOSDemoControls:
    def __init__(self, driver):
        self.driver = driver

    alert_view = (MobileBy.XPATH, "//XCUIElementTypeApplication["
                                  "@name='UIKitCatalog']/XCUIElementTypeWindow/XCUIElementTypeOther"
                                  "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                  "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                  "/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeOther["
                                  "1]/XCUIElementTypeOther")
    simple_alert = (MobileBy.XPATH, "//XCUIElementTypeApplication["
                                    "@name='UIKitCatalog']/XCUIElementTypeWindow/XCUIElementTypeOther"
                                    "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                    "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                    "/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeOther["
                                    "2]/XCUIElementTypeOther")
    okay_button = (MobileBy.IOS_PREDICATE, "label=='OK'")
    okay_cancel_btn = (MobileBy.XPATH, "//XCUIElementTypeApplication["
                                       "@name='UIKitCatalog']/XCUIElementTypeWindow/XCUIElementTypeOther"
                                       "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                       "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                       "/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeOther["
                                       "1]/XCUIElementTypeOther")
    multiple_choice = (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther"
                                                 "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                                 "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable"
                                                 "/XCUIElementTypeCell[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther")
    cancel_btn = (MobileBy.IOS_PREDICATE, "label == 'Cancel'")
    choice_btn = (MobileBy.IOS_PREDICATE, "label == 'Choice One'")
    text_entry_alert = (MobileBy.XPATH, "//XCUIElementTypeApplication["
                                        "@name='UIKitCatalog']/XCUIElementTypeWindow/XCUIElementTypeOther"
                                        "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                        "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                        "/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeOther["
                                        "1]/XCUIElementTypeOther")
    text_field = (MobileBy.XPATH, '//XCUIElementTypeAlert[@name="A Short Title Is '
                                  'Best"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther['
                                  '2]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther['
                                  '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView'
                                  '/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                  '/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther')
    confirm_cancel_btn = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UIKitCatalog"]/XCUIElementTypeWindow['
                                          '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                          '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                          '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell['
                                          '6]/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    confirm_btn = (MobileBy.ACCESSIBILITY_ID, "Confirm")
    picker_view_tab = (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther"
                                                 "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                                                 "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable"
                                                 "/XCUIElementTypeCell[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther")
    time_scroll_wheel = (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypePickerWheel[`value == 'PM'`]")

    def get_alert_view(self):
        return self.driver.find_element(*IOSDemoControls.alert_view)

    def get_simple_alert(self):
        return self.driver.find_element(*IOSDemoControls.simple_alert)

    def get_okay_btn(self):
        return self.driver.find_element(*IOSDemoControls.okay_button)

    def get_okay_cancel_btn(self):
        return self.driver.find_element(*IOSDemoControls.okay_cancel_btn)

    def get_other_alert(self):
        return self.driver.find_element(*IOSDemoControls.multiple_choice)

    def get_choice_btn(self):
        return self.driver.find_element(*IOSDemoControls.choice_btn)

    def get_text_entry(self):
        return self.driver.find_element(*IOSDemoControls.text_entry_alert)

    def get_text_field(self):
        return self.driver.find_element(*IOSDemoControls.text_field)

    def get_confirm_cancel_btn(self):
        return self.driver.find_element(*IOSDemoControls.confirm_cancel_btn)

    def get_confirm_btn(self):
        return self.driver.find_element(*IOSDemoControls.confirm_btn)

    def get_picker_wheel_tab(self):
        return self.driver.find_element(*IOSDemoControls.picker_view_tab)

    def get_scroll_wheel(self):
        return self.driver.find_element(*IOSDemoControls.time_scroll_wheel)

    # def get_current_time(self):
    #     return self.driver.find_element(*IOSDemoControls.time_value)
