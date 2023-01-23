import os
import sys
import allure
from allure_commons.types import AttachmentType
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry

sys.path.insert(0, os.path.dirname(os.getcwd()))
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Behave_Tests.Utilities import FPASeleniumHelper


def before_all(context):
    # For UI automation
    SeleniumBase.initialize_values()


def before_feature(context, feature):
    for scenario in feature.scenarios:
        patch_scenario_with_autoretry(scenario, max_attempts=1)
    if "web" in context.feature.tags:
        SeleniumBase.browser_initialization()


def after_step(context, step):
    if step.status == "failed":
        screenshot_name = str(context.scenario.name).replace(" ", "_")
        FPASeleniumHelper.take_screenshot(screenshot_name)
        # For UI automation
        if "web" in context.feature.tags:
            allure.attach(SeleniumBase.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=AttachmentType.PNG)
            allure.issue(SeleniumBase.driver.current_url)


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

    SeleniumBase.driver.quit()


def after_scenario(context, scenario):
    screenshot_name = str(context.scenario.name).replace(" ", "_")
    FPASeleniumHelper.take_screenshot(screenshot_name)
    allure.attach(SeleniumBase.driver.get_screenshot_as_png(), name="screenshot",
                  attachment_type=AttachmentType.PNG)
    allure.issue(SeleniumBase.driver.current_url)

def after_all(context):
    # For UI automation
    SeleniumBase.dispose()


