import os
import sys
import allure
from allure_commons.types import AttachmentType
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
sys.path.insert(0, os.path.dirname(os.getcwd()))
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities
from Shell_FE_Requests_Core.RequestsBase import RequestsBase


def before_all(context):
    # For UI automation
    SeleniumBase.initialize_values()
    # For Mobile automation
    AppiumBase.start_appium_server()
    # For API automation
    RequestsBase.initialize_values()


def before_feature(context, feature):
    for scenario in feature.scenarios:
        patch_scenario_with_autoretry(scenario, max_attempts=2)
    if "web" in context.feature.tags:
        SeleniumBase.browser_initialization()
    elif "mobile" in context.feature.tags:
        if "iOS" in context.feature.tags:
            AppiumBase.launch_application("ios")
        elif "android" in context.feature.tags:
            AppiumBase.launch_application("android")
        else:
            AppiumBase.launch_application()


def after_step(context, step):
      if step.status == "failed":
        screenshot_name = str(context.scenario.name).replace(" ", "_")
        # For UI automation
        if "web" in context.feature.tags:
            BrowserUtilities.take_screenshot(screenshot_name)
        # For Mobile automation
        elif "mobile" in context.feature.tags:
            AndroidUtilities.take_screenshot(screenshot_name)


def after_feature(context, feature):
    """The below code is used to mark the test results in Browserstack as passed or failed based on the assertions
    validated. Can be commented out or removed if in case Browserstack execution is not performed"""
    # if context.failed is True:
    #     SeleniumBase.driver.execute_script(
    #         'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "At '
    #         'least 1 assertion failed"}}')
    # if context.failed is not True:
    #     SeleniumBase.driver.execute_script(
    #         'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All '
    #         'assertions passed"}}')
    if "mobile" in context.feature.tags:
        AppiumBase.close_driver()


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


def after_all(context):
    # For UI automation
    SeleniumBase.dispose()
    # For mobile automation
    AppiumBase.stop_appium_server()

