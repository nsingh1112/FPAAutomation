import threading
import time

from behave import *
from selenium import webdriver

from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.ShellHubFunctions import ShellHubFunctions
from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities


@given(u'Launch th chrome browser and navigate to Shell hub home page')
def step_impl(context):
    context.shellhub_functions = ShellHubFunctions()
    context.shellhub_functions.access_shell_hub()


@when(u'Pass username to the username field')
def step_impl(context):
    context.shellhub_functions.send_username()
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


@then('It should land on stay sign in page')
def stay_signin(context):
    status = context.shellhub_functions.stay_signin_page()
    AssertionUtilities.assert_if_true(status)


def parallel_executor(context):
    context.shellhub_functions.next_button()


def parallel_executor1(context):
    time.sleep(5)
    context.shellhub_functions.press_enter_button()
