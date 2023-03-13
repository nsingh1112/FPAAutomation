import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.ActualProcessingPageControls import \
    ActualProcessingPageControls
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonRowPageFunctions import \
    CommonRowPageFunctions
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities

class ActualProcessingPageFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.actualProcessingPageControls = ActualProcessingPageControls(SeleniumBase.driver)


    def validate_createPageTitle(self):
        time.sleep(4)
        BrowserUtilities.log.info("entered validate_createPageTitle ")
        WaitUtilities.wait_for_element_to_be_visible(self.actualProcessingPageControls.get_createPageTitle())
        createpageTitle = FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_createPageTitle())
        createpageAggregateLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_createPageAggregateLabel())
        createpageAggregateDataLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_createPageAggregateDataLabel())

        if (createpageTitle and createpageAggregateLabel and createpageAggregateDataLabel):
            SeleniumUtilities.log.info("Create Page title is correct")
        else:
            SeleniumUtilities.log.error("Create Page title is not correct")


    def validate_manageActualsPageTitle(self):
        time.sleep(4)
        BrowserUtilities.log.info("entered validate_manageActualsPageTitle ")
        WaitUtilities.wait_for_element_to_be_visible(self.actualProcessingPageControls.get_manageActualsPageTitle())
        if FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_manageActualsPageTitle()):
            SeleniumUtilities.log.info("Manage Actuals Page title is correct")
        else:
            SeleniumUtilities.log.error("Manage Actuals Page title is not correct")

    def validate_manageVolumesPageTitle(self):
        time.sleep(4)
        BrowserUtilities.log.info("entered validate_manageVolumesPageTitle ")
        WaitUtilities.wait_for_element_to_be_visible(self.actualProcessingPageControls.get_manageVolumesPageTitle())
        if FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_manageVolumesPageTitle()):
            SeleniumUtilities.log.info("Manage Volumes Page title is correct")
        else:
            SeleniumUtilities.log.error("Manage Volumes Page title is not correct")


    def validate_dataRowHeaders(self):
        BrowserUtilities.log.info("entered validate_dataRowHeaders ")
        WaitUtilities.wait_for_element_to_be_visible(self.actualProcessingPageControls.get_rowHeader())
        options1 = self.actualProcessingPageControls.get_rowHeader()
        CommonRowPageFunctions.validate_rowHeader(self, options1)

    def verify_dataFields(self):
        BrowserUtilities.log.info("entered verify_dataFields ")
        WaitUtilities.wait_for_element_to_be_visible(self.actualProcessingPageControls.get_rowHeader())
        isBOLDateLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_bolDateLabel())
        isfinishDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_finishDateInputBox())
        isstartDateInputBox = FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_startDateInputBox())
        issearchByTextLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_searchByTextLabel())
        #issearchByTextCriteriaLabel = FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_searchByTextCriteriaLabel())
        issearchInputText = FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_searchInputText())

        if(isBOLDateLabel and isstartDateInputBox and isfinishDateInputBox and issearchByTextLabel and issearchInputText):
            SeleniumUtilities.log.info("Data Fields Verified")
        else:
            SeleniumUtilities.log.error("Data Fields not Verified")

    def verify_searchByTextCriteria(self, actualProcessingItems):
        BrowserUtilities.log.info("entered verify_searchByTextCriteria ")
        WaitUtilities.wait_for_element_to_be_visible(self.actualProcessingPageControls.get_rowHeader())
        if (actualProcessingItems == "Create"):
            if (FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_createSearchByTextLabel())):
               SeleniumUtilities.log.info("Create Search Criteria Verified")
            else:
                SeleniumUtilities.log.error("Create Search Criteria not Verified")
        elif (actualProcessingItems == "Manage Actuals"):
            if (FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_manageActualsSearchByTextLabel())):
               SeleniumUtilities.log.info("Manage Actuals Search Criteria Verified")
            else:
               SeleniumUtilities.log.error("Manage Actuals Search Criteria not Verified")
        else:
            if (FPASeleniumHelper.check_element_exists_by_xpath(self.actualProcessingPageControls.get_actualVolumeSearchByTextLabel())):
               SeleniumUtilities.log.info("Actual Volume Search Criteria Verified")
            else:
               SeleniumUtilities.log.error("Actual Volume Search Criteria not Verified")


    def validate_colunmheaders(self, dbHeader):
       BrowserUtilities.log.info("entered validate_colunmheaders ")
       expDBColHeader = ['Seq_No','Product_Code','Received_Total_Qty','Original_Total_Received_Qty','Volume_L15','Aggregation_Date','Discharge_Date','Parcel_DC_Date','BOL_Date','Dex_Parcel_ID','Dex_Parcel_Date','Contract_ID','UOM_ID','Buyer','Seller','Created_By','Created_At','Updated_By','Updated_At']
       dbData = ""
       for i in dbHeader:
           xx=str(i).replace('(', '')
           xxx=xx.replace(', )', '')
           dbData += xxx + " "
       actDBColHeader = dbData.replace('\'', '').split()
       print(actDBColHeader)
       if((expDBColHeader.sort()) == (actDBColHeader.sort())):
           SeleniumUtilities.log.info("Actual Volume Search Criteria Verified")
       else:
           SeleniumUtilities.log.error("Actual Volume Search Criteria not Verified")

       time.sleep(1)

    def verify_CreateActualsAllButton(self):
        BrowserUtilities.log.info("entered verify_CreateActualsAllButton ")
        WaitUtilities.wait_for_element_to_be_visible(
            self.actualProcessingPageControls.get_createActualsButton())
        FPASeleniumHelper.click_element(self.actualProcessingPageControls.get_createActualsButton())
        isTitle = FPASeleniumHelper.check_element_exists_by_xpath(
            self.actualProcessingPageControls.get_createActualsPopUpTitle())
        isBody = FPASeleniumHelper.check_element_exists_by_xpath(
            self.actualProcessingPageControls.get_createActualsPopUpBody())
        isCancelBtn = FPASeleniumHelper.check_element_exists_by_xpath(
            self.actualProcessingPageControls.get_createActualsPopUpCancelBtn())
        isSubmitBtn = FPASeleniumHelper.check_element_exists_by_xpath(
            self.actualProcessingPageControls.get_createActualsPopUpSubmitBtn())

        FPASeleniumHelper.click_element(self.actualProcessingPageControls.get_createActualsPopUpCancelBtn())
        if (isTitle and isBody and isCancelBtn and isSubmitBtn):
            SeleniumUtilities.log.info("Create Actuals All Button Fields Verified")
        else:
            SeleniumUtilities.log.error("Create Actuals All Button Fields not Verified")




