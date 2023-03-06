import threading
import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from behave import *

from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.ActualProcessingPageFunctions import \
    ActualProcessingPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.HomePageFunctions import HomePageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.LogsPageFunctions import LogsPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.ReconcilationPageFunctions import \
    ReconcilationPageFunctions


@when('The user Clicks on Logs "{logsItems}"')
def step_impl(context, logsItems = None):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.homePage_functions.validate_applicationTitle()
    if (logsItems == "Reconciliation"):
        context.homePage_functions.click_reconcilation()
    elif (logsItems == "Reconciliation Errors"):
        context.homePage_functions.click_reconciliationErrors()
    else:
        context.homePage_functions.click_actualErrors()


@then('The user validates Logs "{logsItems}" page title')
def step_impl(context, logsItems = None ):
    context.logsPageFunctions = LogsPageFunctions(SeleniumBase.driver)
    if (logsItems == "Reconciliation"):
        context.logsPageFunctions.validate_reconciliationPageTitle()
    elif (logsItems == "Reconciliation Errors"):
        context.logsPageFunctions.validate_reconciliationErrorPageTitle()
    else:
        context.logsPageFunctions.validate_actualsErrorsPageTitle()

@then('The user validates Logs "{logsItems}" data Fields')
def step_impl(context, logsItems = None ):
    context.logsPageFunctions = LogsPageFunctions(SeleniumBase.driver)
    context.logsPageFunctions.verify_dataFields()
    context.logsPageFunctions.verify_searchByTextCriteria(logsItems)


@then('The user Validates Logs Label')
def step_impl(context):
    context.logsPageFunctions = LogsPageFunctions(SeleniumBase.driver)
    context.logsPageFunctions.validate_dataRowHeaders()


