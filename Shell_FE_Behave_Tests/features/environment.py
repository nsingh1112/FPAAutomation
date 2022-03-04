import os
import sys

sys.path.insert(0, os.path.dirname(os.getcwd()))
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from allure_commons.types import AttachmentType
import allure
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities
from Shell_FE_Appium_Core.Utilities.iOSUtilities import IOSUtilities


def before_all(context):
    AppiumBase.start_appium_server()


def before_feature(context, feature):
    print(context.feature.tags)
    if "iOS" in context.feature.tags:
        AppiumBase.launch_application("ios")
    elif "android" in context.feature.tags:
        AppiumBase.launch_application("android")
    else:
        AppiumBase.launch_application()


def after_step(context, step):
    if step.status == "failed":
        screenshot_name = str(context.scenario.name).replace(" ", "_")
        AndroidUtilities.take_screenshot(screenshot_name)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        allure.attach(AppiumBase.driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=AttachmentType.PNG)


def after_all(context):
    AppiumBase.close_driver()
    AppiumBase.stop_appium_server()
