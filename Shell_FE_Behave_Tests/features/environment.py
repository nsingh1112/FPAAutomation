from behave import *
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from appium import webdriver


def before_all(context):
    AppiumBase.read_config()
    AppiumBase.read_values()
    context.driver = AppiumBase.launch_app()


def after_all(context):
    context.driver.quit()

