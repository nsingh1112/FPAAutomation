import threading
import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from behave import *
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
        context.reconcilationPageFunctions.get_receivedStartEndDate()
    else:
        context.reconcilationPageFunctions.validate_reconciledDataPageTitle()


@then('The user validates Reconciliation data Fields')
def step_impl(context):
    context.reconcilationPageFunctions = ReconcilationPageFunctions(SeleniumBase.driver)
    context.reconcilationPageFunctions.verify_dataFields()


@then('The user Validates Reconciliation Label')
def step_impl(context):
    context.reconcilationPageFunctions = ReconcilationPageFunctions(SeleniumBase.driver)
    context.reconcilationPageFunctions.validate_dataRowHeaders()


