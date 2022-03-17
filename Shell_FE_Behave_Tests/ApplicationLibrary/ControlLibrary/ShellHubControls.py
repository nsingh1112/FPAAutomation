from selenium.webdriver.common.by import By


class ShellHubControls:

    def __init__(self, driver):
        self.driver = driver

    search_box = (By.CSS_SELECTOR, "#searchbox")
    yammer = (By.XPATH, "//a[text()='Yammer']")
    user_name = (By.ID, "user-name")
    log_out = (By.XPATH, "//button[text()='Log Out']")
    pick_account = (By.XPATH, "//div[text()='Pick an account']")
    search = (By.CSS_SELECTOR, "#search-button .icomoon-search2")
    logo_img = (By.XPATH, '//*[@class="img-responsive"]')

    def get_search_box(self):
        return self.driver.find_element(*ShellHubControls.search_box)

    def get_yammer(self):
        return self.driver.find_element(*ShellHubControls.yammer)

    def get_user_name(self):
        return self.driver.find_element(*ShellHubControls.user_name)

    def get_log_out(self):
        return self.driver.find_element(*ShellHubControls.log_out)

    def get_pick_account(self):
        return self.driver.find_element(*ShellHubControls.pick_account)

    def get_search(self):
        return self.driver.find_element(*ShellHubControls.search)
