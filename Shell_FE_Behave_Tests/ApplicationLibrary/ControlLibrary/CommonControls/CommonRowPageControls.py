from selenium.webdriver.common.by import By


class CommonRowPageControls:

    def __init__(self, driver):
        self.driver = driver

    homepage = (By.XPATH, "//div[@class='shell-menu-item-content' and text()='Home']")

    def get_Homepage(self):
        return self.driver.find_element(*CommonRowPageControls.homepage)

