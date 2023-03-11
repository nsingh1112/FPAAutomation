import threading
import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from behave import *

from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonPageFunctions import \
    CommonPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.HomePageFunctions import HomePageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.ReconcilationPageFunctions import \
    ReconcilationPageFunctions


@when('The user Clicks on Reconciliation "{reconciliationItems}"')
def step_impl(context, reconciliationItems = None):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.homePage_functions.validate_applicationTitle()
    if (reconciliationItems == "Unprocessed Records"):
        context.homePage_functions.click_unprocessedRecord()
    else:
        context.homePage_functions.click_reconciledData()


@then('The user validates Reconciliation "{reconciliationItems}" page title')
def step_impl(context, reconciliationItems = None ):
    context.reconcilationPageFunctions = ReconcilationPageFunctions(SeleniumBase.driver)
    if (reconciliationItems == "Unprocessed Records"):
        context.reconcilationPageFunctions.validate_unprocessedRecordPageTitle()
        #context.reconcilationPageFunctions.get_receivedStartEndDate()
    else:
        context.reconcilationPageFunctions.validate_reconciledDataPageTitle()


@then('The user validates Reconciliation "{reconciliationItems}" data Fields')
def step_impl(context, reconciliationItems = None):
    context.reconcilationPageFunctions = ReconcilationPageFunctions(SeleniumBase.driver)
    if (reconciliationItems == "Unprocessed Records"):
        context.reconcilationPageFunctions.verify_dataFields()
        context.reconcilationPageFunctions.verify_reconcileUnprocessedRecordsButton()
    else:
        context.reconcilationPageFunctions.verify_dataFields()


@then('The user Validates Reconciliation Label')
def step_impl(context):
    context.reconcilationPageFunctions = ReconcilationPageFunctions(SeleniumBase.driver)
    context.reconcilationPageFunctions.validate_dataRowHeaders()


@then('The user selects and updates a Reconciliation "{reconciliationItems}"')
def step_impl(context, reconciliationItems = None):
    context.reconcilationPageFunctions = ReconcilationPageFunctions(SeleniumBase.driver)
    context.commonPage_functions = CommonPageFunctions(SeleniumBase.driver)
    if (reconciliationItems == "Unprocessed Records"):
        orderID = context.reconcilationPageFunctions.getAndEnter_unprocessedRecordOrderID()
        context.commonPage_functions.click_search()
        context.reconcilationPageFunctions.update_unprocessedRecord()
        context.commonPage_functions.wait_forToastToDisable()
        context.reconcilationPageFunctions.enter_unprocessedRecordOrderID(orderID)
        context.commonPage_functions.click_search()
    else:
        context.reconcilationPageFunctions.select_reconciledDataToUpdate()


@then('The user validates Reconciliation "{reconciliationItems}" record')
def step_impl(context, reconciliationItems = None):
    context.reconcilationPageFunctions = ReconcilationPageFunctions(SeleniumBase.driver)
    if (reconciliationItems == "Unprocessed Records"):
        context.reconcilationPageFunctions.validate_updatedUnprocessedRecord()


