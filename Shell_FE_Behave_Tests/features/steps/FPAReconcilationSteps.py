import threading
import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from behave import *
from selenium import webdriver

from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonPageFunctions import \
    CommonPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.HomePageFunctions import HomePageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.ReconciledDataPageFunctions import \
    ReconciledDataPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.ReprocessedPageFunctions import \
    ReprocessedPageFunctions


@when('The user Clicks on Reconciled Data under RECONCILIATION')
def step_impl(context):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.homePage_functions.click_reconciledData()


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
    context.reconciledDataPageFunctions.enter_receivedDate(dashboardItems)
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
    time.sleep(5)

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


