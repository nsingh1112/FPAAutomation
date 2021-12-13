import os
import sys
import allure
from allure_commons.types import AttachmentType
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities

sys.path.insert(0, os.path.dirname(os.getcwd()))


def before_all(context):
    # For UI automation
    SeleniumBase.initialize_values()
    # For Mobile automation
    AppiumBase.read_config()


def before_feature(context, feature):
    if "web" in context.feature.tags:
        SeleniumBase.browser_initialization()
    elif "mobile" in context.feature.tags:
        AppiumBase.read_values('nativeApp')
        context.driver = AppiumBase.launch_app()


def after_step(context, step):
    if step.status == "failed":
        screenshot_name = str(context.scenario.name).replace(" ", "_")
        # For UI automation
        if "web" in context.feature.tags:
            BrowserUtilities.take_screenshot(screenshot_name)
        # For Mobile automation
        elif "mobile" in context.feature.tags:
            AndroidUtilities.take_screenshot(screenshot_name)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        # For UI automation
        if "web" in context.feature.tags:
            allure.attach(SeleniumBase.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=AttachmentType.PNG)
        # For Mobile automation
        elif "mobile" in context.feature.tags:
            allure.attach(AppiumBase.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=AttachmentType.PNG)


def after_feature(context, feature):
    if "mobile" in context.feature.tags:
        AppiumBase.close_driver()


def after_all(context):
    # For UI automation
    SeleniumBase.dispose()
