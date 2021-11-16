from selenium.webdriver.common.by import By


class AcademyObjects:

    def __init__(self, driver):
        self.driver = driver

    open_window_button = (By.ID, "openwindow")
    open_tab_button = (By.ID, "opentab")
    open_alert_button = (By.ID, "alertbtn")
    confirm_alert_button = (By.ID, "confirmbtn")
    hide_button = (By.ID, "hide-textbox")
    show_button = (By.ID, "show-textbox")
    hidden_textbox = (By.ID, "displayed-text")
    mousehover_button = (By.ID, "mousehover")
    top = (By.XPATH, "//div[@class='mouse-hover-content']/a[1]")
    reload = (By.XPATH, "//div[@class='mouse-hover-content']/a[2]")
    header = (By.XPATH, "//header/following-sibling::h1")
    option_one = (By.CSS_SELECTOR, "#dropdown-class-example > option[value='option1']")
    # frame = (By.CSS_SELECTOR, "#courses-iframe")
    frame = "courses-iframe"
    frame_blog = (By.XPATH, "(//li/a[text()='Blog'])[1]")
    dropdown = (By.ID, "dropdown-class-example")

    def get_open_window(self):
        return self.driver.find_element(*AcademyObjects.open_window_button)

    def get_open_tab(self):
        return self.driver.find_element(*AcademyObjects.open_tab_button)

    def get_open_alert(self):
        return self.driver.find_element(*AcademyObjects.open_alert_button)

    def get_confirm_alert(self):
        return self.driver.find_element(*AcademyObjects.confirm_alert_button)

    def get_hide_button(self):
        return self.driver.find_element(*AcademyObjects.hide_button)

    def get_show_button(self):
        return self.driver.find_element(*AcademyObjects.show_button)

    def get_hidden_textbox(self):
        return self.driver.find_element(*AcademyObjects.hidden_textbox)

    def get_mouse_hover(self):
        return self.driver.find_element(*AcademyObjects.mousehover_button)

    def get_top(self):
        return self.driver.find_element(*AcademyObjects.top)

    def get_reload(self):
        return self.driver.find_element(*AcademyObjects.reload)

    def get_header(self):
        return self.driver.find_element(*AcademyObjects.header)

    def get_option_one(self):
        return self.driver.find_element(*AcademyObjects.option_one)

    def get_frame(self):
        # return self.driver.find_element(*AcademyObjects.frame)
        return self.driver.find_element_by_id(AcademyObjects.frame)

    def get_frame_blg(self):
        return self.driver.find_element(*AcademyObjects.frame_blog)

    def get_dropdown(self):
        return self.driver.find_element(*AcademyObjects.dropdown)