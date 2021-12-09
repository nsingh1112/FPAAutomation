from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


# from selenium.webdriver.common.by import By


class HybridAppControls:

    def __init__(self, driver):
        self.driver = driver

    accept_Terms = "com.android.chrome:id/terms_accept"  # id
    next_Btn = "com.android.chrome:id/next_button"  # id
    positive_Btn = "positive_button"  # id
    search_Box = "search_box_text"  # id
    search_URL = "com.android.chrome:id/url_bar"  # id
    image_Tab = "//span[contains(text(),'Images')]"  # xpath
    image_Tab_View = "//a[contains( text(),'Images')]"  # xpath
    search_by_xpath = "//input[@class='gLFyf gsfi']"
    search_By_name = "q"  # name
    search_by_id = "REsRA"  # id
    by_positive_btn = (By.ID,"positive_button")
    id = "id"
    xpath = "xpath"
    name = "name"
    accept_terms = (MobileBy.ID, "com.android.chrome:id/terms_accept")
    next_btn = (MobileBy.ID, "com.android.chrome:id/next_button")
    positive_btn = (MobileBy.ID, "positive_button")
    search_box = (MobileBy.ID, "search_box_text")
    search_url = (MobileBy.ID, "com.android.chrome:id/url_bar")
    image_tab = (MobileBy.XPATH, "//span[contains(text(),'Images')]")
    search_by_name = (MobileBy.CLASS_NAME, "gLFyf gsfi")
    searchbox_by_xpath = (MobileBy.XPATH,"//a[contains( text(),'Images')]")
    search_box_name = (By.NAME,"q")

    def get_accept_and_terms(self):
        return self.driver.find_element(*HybridAppControls.accept_terms)

    def get_next_btn(self):
        return self.driver.find_element(*HybridAppControls.next_btn)

    def get_finish_btn(self):
        return self.driver.find_element(*HybridAppControls.positive_btn)

    def get_search_box(self):
        return self.driver.find_element(*HybridAppControls.search_box)

    def get_search_url(self):
        return self.driver.find_element(*HybridAppControls.search_url)

    def get_after_search_box(self):
        return self.driver.find_element(*HybridAppControls.search_box_name)

    def get_image_tab(self):
        return self.driver.find_element(*HybridAppControls.image_tab)

    def get_search_by_name(self):
        return self.driver.find_element(*HybridAppControls.searchbox_by_xpath)
