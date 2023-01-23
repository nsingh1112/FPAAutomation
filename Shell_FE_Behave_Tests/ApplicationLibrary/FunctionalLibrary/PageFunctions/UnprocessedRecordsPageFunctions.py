import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.UnprocessedRecordsPageControls import \
    UnprocessedRecordsPageControls
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper


class UnprocessedRecordsPageFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.unprocessedRecordsPageControls = UnprocessedRecordsPageControls(SeleniumBase.driver)

    def validate_pageTitle(self):
        WaitUtilities.wait_for_element_to_be_visible(self.unprocessedRecordsPageControls.get_unprocessedRecordPageTitle())
        if FPASeleniumHelper.check_element_exists_by_xpath( self.unprocessedRecordsPageControls.get_unprocessedRecordPageTitle()):
            SeleniumUtilities.log.info("Unprocessed Record Page title is correct")

        else:
            SeleniumUtilities.log.error("Unprocessed Record Page title is not correct")

    def get_unprocessedRecordRowHeaders(self):
        WaitUtilities.wait_for_element_to_be_visible(self.unprocessedRecordsPageControls.get_unprocessedRecordRowHeader())
        options1 = self.unprocessedRecordsPageControls.get_unprocessedRecordRowHeader()

        unprocessed_row_header_list = [x.get_attribute('innerHTML') for x in options1]
        elementList = []
        current_row_header_list = []
        for row in unprocessed_row_header_list:
            # will scroll until that element is not appeared on page
            if(row != ""):
               unprocessed_row_header = self.driver.find_elements_by_xpath(
                   "//div[@class='shell-table-header']/table/thead/tr/th[text()='" + str(row) + "']")
               self.driver.execute_script("arguments[0].scrollIntoView(true);", unprocessed_row_header[0])
               current_row_header_list.append(unprocessed_row_header[0].text)

        # self.driver.execute_script(
        # "window.scrollBy(0,document.body.scrollHeight|| document.documentElement.scrollHeight)", "")