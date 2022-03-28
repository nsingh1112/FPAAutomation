
import time

from behave import *

from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionalLibrary.WebBrowserFunctions import BrowserFunctions



@given('I have launched the chrome app')
def launching_app(context):
    context.webBrowser = BrowserFunctions()


@when('I am passing the URL')
def launching_url(context):
    context.webBrowser.launch_web("https://hub.shell.com")
    time.sleep(2)


@then('I verify it landed on the corresponding URL')
def verifying_title(context):
    context.webBrowser.verify_title()
    # context.webBrowser.get_context()
    # context.webBrowser.switch_context("CHROMIUM")


@then('I am passing the username')
def send_username(context):
    context.webBrowser.click_username()
    context.webBrowser.pass_value()


@then('I verify it is landed on the Authentication system page')
def check_authentication(context):
    context.webBrowser.check_authentication()


