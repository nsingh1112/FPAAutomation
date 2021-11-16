from selenium.webdriver.common.by import By


class TutorialsPointObjects:

    def __init__(self, driver):
        self.driver = driver

    first_name_label = (By.XPATH, "//strong[text()='First name:  ']")
    last_name_label = (By.XPATH, "//strong[text()='Last name:  ']")
    first_name = (By.CSS_SELECTOR, "input[name='firstname']")
    last_name = (By.CSS_SELECTOR, "input[name='lastname']")
    documentation = (By.XPATH, "//a[@id='m-documentation']/span[text()='Documentation']")
    # sex_male = (By.CSS_SELECTOR, "input[value='Male']")
    sex_male = (By.XPATH, "//input[@value='Female']/preceding-sibling::input")
    sex_female = (By.CSS_SELECTOR, "input[value='Female']")
    manual_tester = (By.CSS_SELECTOR, "input[value='Manual Tester']")
    automation_tester = (By.CSS_SELECTOR, "input[value='Automation Tester']")
    yoe_label = (By.XPATH, "//strong[text()='Years of Experience:  ']")
    yoe_five = (By.CSS_SELECTOR, "input[value='5']")
    yoe_seven = (By.CSS_SELECTOR, "input[value='7']")
    date_label = (By.XPATH, "//strong[text()='Date:  ']")
    submit_btn = (By.CSS_SELECTOR, "button[name='submit']")
    continents = (By.CSS_SELECTOR, "select[name='continents']")

    def get_first_name_label(self):
        return self.driver.find_element(*TutorialsPointObjects.first_name_label)

    def get_last_name_label(self):
        return self.driver.find_element(*TutorialsPointObjects.last_name_label)

    def get_first_name(self):
        return self.driver.find_element(*TutorialsPointObjects.first_name)

    def get_last_name(self):
        return self.driver.find_element(*TutorialsPointObjects.last_name)

    def get_sex_male(self):
        return self.driver.find_element(*TutorialsPointObjects.sex_male)

    def get_sex_female(self):
        return self.driver.find_element(*TutorialsPointObjects.sex_female)

    def get_yoe_label(self):
        return self.driver.find_element(*TutorialsPointObjects.yoe_label)

    def get_yoe_five(self):
        return self.driver.find_element(*TutorialsPointObjects.yoe_five)

    def get_yoe_seven(self):
        return self.driver.find_element(*TutorialsPointObjects.yoe_seven)

    def get_date_label(self):
        return self.driver.find_element(*TutorialsPointObjects.date_label)

    def get_submit_btn(self):
        return self.driver.find_element(*TutorialsPointObjects.submit_btn)

    def get_continents(self):
        return self.driver.find_element(*TutorialsPointObjects.continents)

    def get_manual_tester(self):
        return self.driver.find_element(*TutorialsPointObjects.manual_tester)

    def get_automation_tester(self):
        return self.driver.find_element(*TutorialsPointObjects.automation_tester)

    def get_documentation(self):
        return self.driver.find_element(*TutorialsPointObjects.documentation)
