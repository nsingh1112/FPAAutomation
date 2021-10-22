import sys
from behave import *
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from pprint import pprint

from Shell_FE_Selenium_Core.Utilities.LoggingUtilities import LoggingUtilities

print("Inside Step definition")
logObj = LoggingUtilities()
log = logObj.logger()


@Given('user navigates to Google home page')
def url_navigation(context):
    log.info("Inside feature file")
    context.driver.get(SeleniumBase.url)
    log.info("Navigated to Google home page")
    pprint(sys.path)


@When('user types text')
def send_text(context):
    log.info("Second step executed. User types text")


@When('user clicks on the Search button')
def click_search(context):
    log.info("Third step executed. User clicks on Search button")


@Given('user navigates to Bing home page')
def bing_navigation(context):
    context.driver.get("https://www.bing.com/")
    log = logObj.logger()
    log.info("Navigated to Bing home page")
