import sys
from behave import *
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from pprint import pprint


@Given('user navigates to Google home page')
def url_navigation(context):
    context.driver.get(SeleniumBase.url)
    pprint(sys.path)
    SeleniumBase.dispose()
