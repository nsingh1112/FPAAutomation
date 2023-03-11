import threading
import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from behave import *
from selenium import webdriver

from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonPageFunctions import \
    CommonPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.DashBoardPageFunctions import \
    DashBoardPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.EnteredInDEXPageFunctions import \
    EnteredInDEXPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.FailedReconciliationPageFunctions import \
    FailedReconciliationPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.FailedToEnteredInDEXPageFunctions import \
    FailedToEnteredInDEXPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.HomePageFunctions import HomePageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.ReconciledDataPageFunctions import \
    ReconciledDataPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.ReprocessedPageFunctions import \
    ReprocessedPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.UnprocessedRecordsPageFunctions import \
    UnprocessedRecordsPageFunctions


@when('The user Clicks on "{dashboardItems}"')
def step_impl(context, dashboardItems = None):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.commonPage_functions = CommonPageFunctions(SeleniumBase.driver)
    context.commonPage_functions.click_Homepage()
    if(dashboardItems == "Reconciliation"):
        context.homePage_functions.click_reconciled()
    else:
        context.homePage_functions.click_reprocessed()


@then('The user validates Reconciled Data page title')
def step_impl(context):
    context.reconciledDataPageFunctions = ReconciledDataPageFunctions(SeleniumBase.driver)
    context.reconciledDataPageFunctions.validate_pageTitle()


@then('The user validates Reconciled Data Fields')
def step_impl(context):
    context.reconciledDataPageFunctions = ReconciledDataPageFunctions(SeleniumBase.driver)
    context.reconciledDataPageFunctions.verify_reconciledDataFields()


@then('The user enters received date for "{dashboardItems}" and click on search button')
def step_impl(context, dashboardItems = None):
    context.reconciledDataPageFunctions = ReconciledDataPageFunctions(SeleniumBase.driver)
    startDate,endDate =context.reconciledDataPageFunctions.get_receivedStartEndDate()
    context.reconciledDataPageFunctions.enter_receivedDate(dashboardItems,startDate,endDate)
    context.commonPage_functions = CommonPageFunctions(SeleniumBase.driver)
    context.commonPage_functions.select_Status()
    context.reconciledDataPageFunctions.click_search()

@then('The user Validates the Reconciled ReportPage Label')
def step_impl(context):
    context.reconciledDataPageFunctions = ReconciledDataPageFunctions(SeleniumBase.driver)
    context.reconciledDataPageFunctions.get_reconciledDataRowHeaders()


@then('The user enters received date and click on Clear button')
def step_impl(context):

    context.reconciledDataPageFunctions = ReconciledDataPageFunctions(SeleniumBase.driver)
    context.reconciledDataPageFunctions.click_Clear()

@when('The user Clicks on Reprocessed')
def step_impl(context):
    context.commonPage_functions = CommonPageFunctions(SeleniumBase.driver)
    context.commonPage_functions.click_Homepage()
    context.reprocessedPageFunctions = ReprocessedPageFunctions(SeleniumBase.driver)
    context.reprocessedPageFunctions.click_reprocessed()

@then('The user validates Reprocessed page title')
def step_impl(context):
    context.reconciledDataPageFunctions = ReconciledDataPageFunctions(SeleniumBase.driver)
    context.reconciledDataPageFunctions.validate_pageTitle()

@then('The user validates Reprocessed Data Fields')
def step_impl(context):
    context.reconciledDataPageFunctions = ReconciledDataPageFunctions(SeleniumBase.driver)
    context.reconciledDataPageFunctions.verify_reconciledDataFields()

@then('The user Validates the Reprocessed ReportPage Label')
def step_impl(context):
    context.reconciledDataPageFunctions = ReconciledDataPageFunctions(SeleniumBase.driver)
    context.reconciledDataPageFunctions.get_reconciledDataRowHeaders()

@when('The user Clicks on Failed Reconciliation Dashboard Items')
def step_impl(context):
    context.commonPage_functions = CommonPageFunctions(SeleniumBase.driver)
    context.commonPage_functions.click_Homepage()
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.homePage_functions.click_failedReconciliation()

@then('The user validates Failed Reconciliation Page title')
def step_impl(context):
    context.failedReconciliationPageFunctions = FailedReconciliationPageFunctions(SeleniumBase.driver)
    context.failedReconciliationPageFunctions.validate_pageTitle()

@then('The user validates Failed Reconciliation Data Fields')
def step_impl(context):
    context.failedReconciliationPageFunctions = FailedReconciliationPageFunctions(SeleniumBase.driver)
    context.failedReconciliationPageFunctions.verify_failedReconciliationDataFields()

@then('The user enters received date for and click on search button')
def step_impl(context):
    context.failedReconciliationPageFunctions = FailedReconciliationPageFunctions(SeleniumBase.driver)
    startDate, endDate = context.failedReconciliationPageFunctions.get_receivedStartEndDate()
    context.failedReconciliationPageFunctions.enter_receivedDate(startDate, endDate)
    orderId = context.failedReconciliationPageFunctions.get_getAndEnterOrderID()
    context.reconciledDataPageFunctions = ReconciledDataPageFunctions(SeleniumBase.driver)
    context.reconciledDataPageFunctions.click_search()
    #context.failedReconciliationPageFunctions.get_validateOrderID(orderId)

@then('The user Validates the Failed Reconciliation Label')
def step_impl(context):
    context.failedReconciliationPageFunctions = FailedReconciliationPageFunctions(SeleniumBase.driver)
    context.failedReconciliationPageFunctions.get_failedReconciliationDataRowHeaders()

@when('The user Clicks on Failed To Enter In DEX Dashboard Items')
def step_impl(context):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.commonPage_functions = CommonPageFunctions(SeleniumBase.driver)
    context.commonPage_functions.click_Homepage()
    context.homePage_functions.click_failedToEnterInDEX()

@then('The user validates the Failed To Enter In DEX Page title')
def step_impl(context):
    context.failedToEnteredInDEXPageFunctions = FailedToEnteredInDEXPageFunctions(SeleniumBase.driver)
    context.failedToEnteredInDEXPageFunctions.validate_FailedToEnterInDExPageTitle()

@then('The user validates Failed To Enter In DEX Data Fields')
def step_impl(context):
    context.failedToEnteredInDEXPageFunctions = FailedToEnteredInDEXPageFunctions(SeleniumBase.driver)
    context.failedToEnteredInDEXPageFunctions.verify_failedToEnterInDEXDataFields()

@then('The user enters contract ID and click on search button')
def step_impl(context):
    context.failedToEnteredInDEXPageFunctions = FailedToEnteredInDEXPageFunctions(SeleniumBase.driver)
    contractID = context.failedToEnteredInDEXPageFunctions.get_enterContractID()
    context.commonPage_functions = CommonPageFunctions(SeleniumBase.driver)
    context.commonPage_functions.click_search()
    context.failedToEnteredInDEXPageFunctions.get_validateContractID(contractID)

@then('The user Validates the Label displayed in the Failed To Enter In DEX')
def step_impl(context):
    context.failedToEnteredInDEXPageFunctions = FailedToEnteredInDEXPageFunctions(SeleniumBase.driver)
    context.failedToEnteredInDEXPageFunctions.get_failedToEnterInDEXDataRowHeaders()

@when('The user Clicks on Entered In DEX Dashboard Items')
def step_impl(context):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.commonPage_functions = CommonPageFunctions(SeleniumBase.driver)
    context.commonPage_functions.click_Homepage()
    context.homePage_functions.click_enteredInDEX()

@then('The user validates the Entered In DEX Page title')
def step_impl(context):
    context.enteredInDEXPageFunctions = EnteredInDEXPageFunctions(SeleniumBase.driver)
    context.enteredInDEXPageFunctions.validate_pageTitle()

@then('The user validates Entered In DEX Data Fields')
def step_impl(context):
    context.enteredInDEXPageFunctions = EnteredInDEXPageFunctions(SeleniumBase.driver)
    context.enteredInDEXPageFunctions.verify_enteredInDEXDataFields()

@then('The user enters received date in Entered In DEX and click on search button')
def step_impl(context):
    context.enteredInDEXPageFunctions = EnteredInDEXPageFunctions(SeleniumBase.driver)
    startDate, endDate = context.enteredInDEXPageFunctions.get_bolStartEndDate()
    context.enteredInDEXPageFunctions.enter_bolDate(startDate, endDate)
    context.commonPage_functions = CommonPageFunctions(SeleniumBase.driver)
    context.commonPage_functions.click_search()

@then('The user Validates the Label displayed in the Entered In DEX')
def step_impl(context):
    context.enteredInDEXPageFunctions = EnteredInDEXPageFunctions(SeleniumBase.driver)
    context.enteredInDEXPageFunctions.get_enteredInDEXDataRowHeaders()

@when('The user Clicks on Unprocessed')
def step_impl(context):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.commonPage_functions = CommonPageFunctions(SeleniumBase.driver)
    context.commonPage_functions.click_Homepage()
    context.homePage_functions.click_unprocessed()

@then('The user validates the Unprocessed Page title')
def step_impl(context):
    context.unprocessedRecordsPage_functions = UnprocessedRecordsPageFunctions(SeleniumBase.driver)
    context.unprocessedRecordsPage_functions.validate_pageTitle()

@then('The user validates Unprocessed Data Fields')
def step_impl(context):
    context.unprocessedRecordsPage_functions = UnprocessedRecordsPageFunctions(SeleniumBase.driver)
    context.unprocessedRecordsPage_functions.get_unprocessedRecordRowHeaders()

@then('The user validates total no of records')
def step_impl(context):
    context.unprocessedRecordsPage_functions = UnprocessedRecordsPageFunctions(SeleniumBase.driver)
    context.unprocessedRecordsPage_functions.get_totalUnprocessedRecord()

@when('The user validates the homepage')
def step_impl(context):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.homePage_functions.validate_applicationTitle()
    context.homePage_functions.validate_leftListItems()


@when('The user validates the dashboardItems')
def step_impl(context):
    context.dashboardPage_functions = DashBoardPageFunctions(SeleniumBase.driver)
    context.dashboardPage_functions.get_dashboardItems()
    context.dashboardPage_functions.validate_dashboardGraphicalRepresentation()
    context.dashboardPage_functions.validate_darkMode()

