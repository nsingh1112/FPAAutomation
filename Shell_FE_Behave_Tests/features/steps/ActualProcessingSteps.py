import threading
import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from behave import *

from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.ActualProcessingPageFunctions import \
    ActualProcessingPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.HomePageFunctions import HomePageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.ReconcilationPageFunctions import \
    ReconcilationPageFunctions


@when('The user Clicks on Actual Processing "{actualProcessingItems}"')
def step_impl(context, actualProcessingItems = None):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.homePage_functions.validate_applicationTitle()
    if (actualProcessingItems == "Create"):
        context.homePage_functions.click_create()
    elif (actualProcessingItems == "Manage Actuals"):
        context.homePage_functions.click_manageActuals()
    else:
        context.homePage_functions.click_actualVolumes()


@then('The user validates Actual Processing "{actualProcessingItems}" page title')
def step_impl(context, actualProcessingItems = None ):
    context.actualProcessingPageFunctions = ActualProcessingPageFunctions(SeleniumBase.driver)
    if (actualProcessingItems == "Create"):
        context.actualProcessingPageFunctions.validate_createPageTitle()
    elif (actualProcessingItems == "Manage Actuals"):
        context.actualProcessingPageFunctions.validate_manageActualsPageTitle()
    else:
        context.actualProcessingPageFunctions.validate_manageVolumesPageTitle()

@then('The user validates Actual Processing "{actualProcessingItems}" data Fields')
def step_impl(context, actualProcessingItems = None ):
    context.actualProcessingPageFunctions = ActualProcessingPageFunctions(SeleniumBase.driver)
    context.actualProcessingPageFunctions.verify_dataFields()
    context.actualProcessingPageFunctions.verify_searchByTextCriteria(actualProcessingItems)


@then('The user Validates Actual Processing Label')
def step_impl(context):
    context.actualProcessingPageFunctions = ActualProcessingPageFunctions(SeleniumBase.driver)
    context.actualProcessingPageFunctions.validate_dataRowHeaders()


