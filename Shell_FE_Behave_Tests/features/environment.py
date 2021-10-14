from behave import *
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase


def before_all(context):
    SeleniumBase.read_config()
    SeleniumBase.initialize_values()
    context.driver = SeleniumBase.browser_initialization()


def after_all():
    SeleniumBase.dispose()
