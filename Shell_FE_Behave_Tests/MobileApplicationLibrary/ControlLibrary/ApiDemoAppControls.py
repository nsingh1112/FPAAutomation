from appium.webdriver.common.mobileby import MobileBy


class ApiDemoAppControls:

    def __init__(self, driver):
        self.driver = driver

    view_tab = (MobileBy.ACCESSIBILITY_ID, "Views")
    control_tab = (MobileBy.ACCESSIBILITY_ID, "Controls")
    light_theme_tab = (MobileBy.ACCESSIBILITY_ID, "1. Light Theme")
    check_box = (MobileBy.ACCESSIBILITY_ID, "Checkbox 1")
    popup_btn = (MobileBy.ACCESSIBILITY_ID, "Make a Popup!")
    popup_menu = (MobileBy.ACCESSIBILITY_ID, "Popup Menu")
    text_swictcher = (MobileBy.ACCESSIBILITY_ID, "TextSwitcher")
    next_btn = (MobileBy.ACCESSIBILITY_ID, "Next")
    drag_and_drop = (MobileBy.ACCESSIBILITY_ID, "Drag and Drop")
    source_element = (MobileBy.ID, "io.appium.android.apis:id/drag_dot_1")
    target_element = (MobileBy.ID, "io.appium.android.apis:id/drag_dot_2")
    result_text = (MobileBy.ID, "io.appium.android.apis:id/drag_result_text")

    def get_view_tab(self):
        return self.driver.find_element(*ApiDemoAppControls.view_tab)

    def get_controls_view(self):
        return self.driver.find_element(*ApiDemoAppControls.control_tab)

    def get_light_theme(self):
        return self.driver.find_element(*ApiDemoAppControls.light_theme_tab)

    def get_checkbox(self):
        return self.driver.find_element(*ApiDemoAppControls.check_box)

    def get_popup_menu(self):
        return self.driver.find_element(*ApiDemoAppControls.popup_menu)

    def get_popup_btn(self):
        return self.driver.find_element(*ApiDemoAppControls.popup_btn)

    def get_text_switcher(self):
        return self.driver.find_element(*ApiDemoAppControls.text_swictcher)

    def get_next_btn(self):
        return self.driver.find_element(*ApiDemoAppControls.next_btn)

    def get_drag_and_drop_tab(self):
        return self.driver.find_element(*ApiDemoAppControls.drag_and_drop)

    def get_source_element(self):
        return self.driver.find_element(*ApiDemoAppControls.source_element)

    def get_target_element(self):
        return self.driver.find_element(*ApiDemoAppControls.target_element)

    def get_result_text(self):
        return self.driver.find_element(*ApiDemoAppControls.result_text)
