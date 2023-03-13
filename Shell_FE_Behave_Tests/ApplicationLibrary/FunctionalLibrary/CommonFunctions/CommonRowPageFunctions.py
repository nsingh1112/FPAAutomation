import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities
from selenium.webdriver.common.by import By

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.UnprocessedRecordsPageControls import \
    UnprocessedRecordsPageControls


class CommonRowPageFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.unprocessedRecordsPageControls = UnprocessedRecordsPageControls(SeleniumBase.driver)


    def get_unprocessedRecordRowHeaders(self):
        WaitUtilities.wait_for_element_to_be_visible(self.unprocessedRecordsPageControls.get_unprocessedRecordRowHeader())
        options1 = self.unprocessedRecordsPageControls.get_unprocessedRecordRowHeader()

        self.validate_rowHeader(options1)

    def validate_rowHeader(self, options1):
        row_header_list = [x.get_attribute('innerHTML') for x in options1]
        current_row_header_list = []

        for row in row_header_list:
            # will scroll until that element is not appeared on page
            if (row != "" and ("label class") not in row):
                row_header = self.driver.find_elements( By.XPATH, "//div[@class='shell-table-header']/table/thead/tr/th[text()='" + str(row) + "']")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", row_header[0])
                time.sleep(1)
                current_row_header_list.append(row_header[0].text)
