import sys
from behave import *
from Shell_FE_Appium_Core.AppiumBase import AppiumBase

@given('I am launching the mobile app')
def step_impl(context):
    print("I am launching application")
    AppiumBase.LaunchApp()

