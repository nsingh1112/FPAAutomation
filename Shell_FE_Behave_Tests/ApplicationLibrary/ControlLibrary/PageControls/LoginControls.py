from selenium.webdriver.common.by import By


class LoginControls:

    def __init__(self, driver):
        self.driver = driver

    accept_button = (By.ID, "idSIButton9")
    btnPingIdMFA = (By.XPATH, "//button[@class='custom-btn btn-primary-outlined-icon']/span[contains(text(),'PingID MFA')]")
    pingIdMFAUserName = (By.XPATH, "//input[@name='pf.username']")
    pingIdMFAPwd = (By.XPATH, "//input[@name='pf.pass']")
    pingIdMFASignOn = (By.XPATH, "//input[@class='submit-button submit-margin']")
    pingIdMFAAppName = (By.XPATH, "//div[@class='app-name']")



    def get_accept_button(self):
        return self.driver.find_element(*LoginControls.accept_button)

    def get_btnPingIdMFA(self):
        return self.driver.find_element(*LoginControls.btnPingIdMFA)

    def get_pingIdMFAUserName(self):
        return self.driver.find_element(*LoginControls.pingIdMFAUserName)

    def get_pingIdMFAPwd(self):
        return self.driver.find_element(*LoginControls.pingIdMFAPwd)

    def get_pingIdMFASignOn(self):
        return self.driver.find_element(*LoginControls.pingIdMFASignOn)

    def get_pingIdMFAAppName(self):
        return self.driver.find_element(*LoginControls.pingIdMFAAppName)


    