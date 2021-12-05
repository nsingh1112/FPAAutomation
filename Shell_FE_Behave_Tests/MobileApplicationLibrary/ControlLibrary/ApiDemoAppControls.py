from appium.webdriver.common.mobileby import MobileBy
class ApiDemoAppControls:

    def __init__(self,driver):
        self.driver = driver

    views = "Views"  # accessibility_id
    controls = "Controls"  # accessibility_id
    light_Theme = "1. Light Theme"  # accessibilty_id
    check_Box = "Checkbox 1"  # accessibility_id
    open_view = (MobileBy.ACCESSIBILITY_ID,"Views")

    # Locatortype
    accessibility = "accessibility_id"
    id = "id"
    xpath = "xpath"
    className = "classname"

    def open_view_tab(self):
        return self.driver.find_element(*ApiDemoAppControls.open_view)



