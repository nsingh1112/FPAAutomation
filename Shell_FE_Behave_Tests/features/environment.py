from behave import *
import os
from Shell_FE_Appium_Core.AppiumBase import AppiumBase

from appium import webdriver
import logging


def before_all(context):

    #AppiumBase.startAppiumServer()
    #AppiumBase.is_App_installed()
    AppiumBase.read_config()
    AppiumBase.read_values('nativeApp')
    context.driver = AppiumBase.launch_app()




def after_all(context):
    AppiumBase.close_driver()
    #AppiumBase.stopAppiumServer()
    #AppiumBase.stopAppiumServer()


