import threading
import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.DbUtilities import DbUtilities
from behave import *
from selenium import webdriver

from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonPageFunctions import \
    CommonPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.DocumentsPageFunctions import \
    DocumentsPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.FailedReconciliationPageFunctions import \
    FailedReconciliationPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.HomePageFunctions import HomePageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.ReconciledDataPageFunctions import \
    ReconciledDataPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.ReprocessedPageFunctions import \
    ReprocessedPageFunctions


@when('The user Clicks on Documents "{documentsItems}"')
def step_impl(context, documentsItems = None):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    if (documentsItems == "Terminal Report"):
        context.homePage_functions.click_terminalReport()
    else:
        context.homePage_functions.click_invoices()

@then('The user validates "{documentsItems}" page title')
def step_impl(context, documentsItems = None ):
    context.documentsPageFunctions = DocumentsPageFunctions(SeleniumBase.driver)
    if (documentsItems == "Terminal Report"):
        context.documentsPageFunctions.validate_terminalReportPageTitle()
    else:
        context.documentsPageFunctions.validate_invoicesTitle()

@then('The user validates data Fields')
def step_impl(context):
    context.documentsPageFunctions = DocumentsPageFunctions(SeleniumBase.driver)
    context.documentsPageFunctions.verify_terminalreportDataFields()

@then('The user enters document type and search by text and click on search button')
def step_impl(context):
    context.commonPage_functions = CommonPageFunctions(SeleniumBase.driver)
    context.commonPage_functions.select_DocumentType()
    context.commonPage_functions.click_search()


@then('The user Validates the Label')
def step_impl(context):
    context.documentsPageFunctions = DocumentsPageFunctions(SeleniumBase.driver)
    context.documentsPageFunctions.get_terminalReportDataRowHeaders()

@then('The user Clicks on file name and verify the file is opened in new tab')
def step_impl(context):
    context.documentsPageFunctions = DocumentsPageFunctions(SeleniumBase.driver)
    context.documentsPageFunctions.click_filename()



