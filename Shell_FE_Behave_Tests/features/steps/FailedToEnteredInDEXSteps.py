import threading
import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from behave import *
from selenium import webdriver

from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonPageFunctions import \
    CommonPageFunctions
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


@when('The user Clicks on Failed To Enter In DEX Dashboard Items')
def step_impl(context):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.homePage_functions.click_failedToEnterInDEX()

@then('The user validates the Failed To Enter In DEX Page title')
def step_impl(context):
    context.failedToEnteredInDEXPageFunctions = FailedToEnteredInDEXPageFunctions(SeleniumBase.driver)
    context.failedToEnteredInDEXPageFunctions.validate_FailedToEnterInDExPageTitle()

@then('The user validates Failed To Enter In DEX Data Fields')
def step_impl(context):
    context.failedToEnteredInDEXPageFunctions = FailedToEnteredInDEXPageFunctions(SeleniumBase.driver)
    context.failedToEnteredInDEXPageFunctions.verify_failedToEnterInDEXDataFields()

@then('The user enters received date in Failed To Enter In DEX and click on search button')
def step_impl(context):
    context.failedToEnteredInDEXPageFunctions = FailedToEnteredInDEXPageFunctions(SeleniumBase.driver)
    context.failedToEnteredInDEXPageFunctions.enter_receivedDate()
    context.commonPage_functions = CommonPageFunctions(SeleniumBase.driver)
    context.commonPage_functions.click_search()

@then('The user Validates the Label displayed in the Failed To Enter In DEX')
def step_impl(context):
    context.failedToEnteredInDEXPageFunctions = FailedToEnteredInDEXPageFunctions(SeleniumBase.driver)
    context.failedToEnteredInDEXPageFunctions.get_failedToEnterInDEXDataRowHeaders()
