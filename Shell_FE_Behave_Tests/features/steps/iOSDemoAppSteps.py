import time

from behave import *
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities

@given('I have launched the Integration App')
def step_impl(context):
    AndroidUtilities.take_screenshot("iOSTest")
    time.sleep(5)


