import threading
import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from behave import *
from selenium import webdriver

from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.DashBoardPageFunctions import \
    DashBoardPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.LoginFunctions import LoginFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.HomePageFunctions import HomePageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.ReconciledDataPageFunctions import \
    ReconciledDataPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.UnprocessedRecordsPageFunctions import \
    UnprocessedRecordsPageFunctions


@given(u'Launch the browser and navigate to the url')
def step_impl(context):


    t1 = threading.Thread(
        name='run test parallel',
        target=parallel_executor,
        args=[context])
    t1.start()
    t2 = threading.Thread(
        name='run test parallel',
        target=parallel_executor1,
        args=[context])
    t2.start()
    t2.join()
    t1.join()
    time.sleep(5)


@when(u'handle the SSO using actions')
def handle_sso_certificate(context):
    """In this method we are handling the SSO certificate
        :args:
        target = we should pass the method name in the target
        In Parallel_executor1 method we have used keyboard actions to click "ok" in the pop up
    """
    t1 = threading.Thread(
        name='run test parallel',
        target=parallel_executor,
        args=[context])
    t1.start()
    t2 = threading.Thread(
        name='run test parallel',
        target=parallel_executor1,
        args=[context])
    t2.start()
    t2.join()
    t1.join()


@when('The user validates the homepage')
def step_impl(context):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.homePage_functions.validate_leftListItems()


@when('The user validates the dashboardItems')
def step_impl(context):
    context.dashboardPage_functions = DashBoardPageFunctions(SeleniumBase.driver)
    context.dashboardPage_functions.get_dashboardItems()
    context.dashboardPage_functions.validate_dashboardGraphicalRepresentation()
    context.dashboardPage_functions.validate_darkMode()

@when('The user Clicks on Unprocessed records under RECONCILIATION')
def step_impl(context):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.homePage_functions.click_unprocessedRecord()
    context.unprocessedRecordsPage_functions = UnprocessedRecordsPageFunctions(SeleniumBase.driver)
    context.unprocessedRecordsPage_functions.validate_pageTitle()
    context.unprocessedRecordsPage_functions.get_totalUnprocessedRecord()
    context.unprocessedRecordsPage_functions.get_unprocessedRecordRowHeaders()


def parallel_executor(context):
    context.loginPage_functions = LoginFunctions(SeleniumBase.driver)
    context.loginPage_functions.access_shell_hub()


def parallel_executor1(context):
    time.sleep(5)
    context.loginPage_functions = LoginFunctions(SeleniumBase.driver)
    context.loginPage_functions.press_enter_button()
