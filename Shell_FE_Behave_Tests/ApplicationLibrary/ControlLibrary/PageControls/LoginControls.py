from selenium.webdriver.common.by import By


class LoginControls:

    def __init__(self, driver):
        self.driver = driver

    accept_button = (By.ID, "idSIButton9")

    def get_accept_button(self):
        return self.driver.find_element(*LoginControls.accept_button)
    