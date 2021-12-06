from appium.webdriver.common.mobileby import MobileBy
class ApiDemoAppControls:

    def __init__(self,driver):
        self.driver = driver
    views = "Views"
    controls = "Controls"  # accessibility_id
    light_Theme = "1. Light Theme"  # accessibilty_id
    check_Box = "Checkbox 1"  # accessibility_id
    view_tab = (MobileBy.ACCESSIBILITY_ID,"Views")
    control_tab = (MobileBy.ACCESSIBILITY_ID,"Controls")
    light_theme_tab = (MobileBy.ACCESSIBILITY_ID,"1. Light Theme")
    check_box = (MobileBy.ACCESSIBILITY_ID,"Checkbox 1")


    # Locatortype
    accessibility = "accessibility_id"
    id = "id"
    xpath = "xpath"
    className = "classname"

    def get_view_tab(self):
        return self.driver.find_element(*ApiDemoAppControls.view_tab)

    def get_controls_view(self):
        return self.driver.find_element(*ApiDemoAppControls.control_tab)

    def get_light_theme(self):
        return self.driver.find_element(*ApiDemoAppControls.light_theme_tab)

    def get_checkbox(self):
        return self.driver.find_element(*ApiDemoAppControls.check_box)






