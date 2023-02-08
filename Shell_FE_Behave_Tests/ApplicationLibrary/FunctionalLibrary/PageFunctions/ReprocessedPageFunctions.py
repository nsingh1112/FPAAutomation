import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.ReconciledDataPageControls import \
    ReconciledDataPageControls
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.ReprocessedPageControls import \
    ReprocessedPageControls
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CalendarPageFunctions import \
    CalendarPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonPageFunctions import \
    CommonPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonRowPageFunctions import \
    CommonRowPageFunctions
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper
from Shell_FE_Behave_Tests.Utilities.FPAWaitHelper import FPAWaitHelper


class ReprocessedPageFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.reprocessedPageControls = ReprocessedPageControls(SeleniumBase.driver)


    def click_reprocessed(self):
        FPAWaitHelper.wait_for_element_to_be_clickable(self.reprocessedPageControls.get_reprocessedLink(), 6000)
        FPASeleniumHelper.click_element(self.reprocessedPageControls.get_reprocessedLink())


