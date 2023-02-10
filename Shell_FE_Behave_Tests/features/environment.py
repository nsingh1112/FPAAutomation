import os
import sys
import allure
from allure_commons.types import AttachmentType
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry

sys.path.insert(0, os.path.dirname(os.getcwd()))
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Behave_Tests.Utilities.FPASeleniumHelper import FPASeleniumHelper


def before_all(context):
    # For UI automation
    SeleniumBase.initialize_values()


def before_feature(context, feature):
    for scenario in feature.scenarios:
        patch_scenario_with_autoretry(scenario, max_attempts=1)
    if "web" in context.feature.tags:
        SeleniumBase.browser_initialization()


def after_step(context, step):
    screenshot_name = str(context.scenario.name).replace(" ", "_")
    FPASeleniumHelper.take_screenshot(screenshot_name)
    # For UI automation
    if "web" in context.feature.tags:
        allure.attach(SeleniumBase.driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
        allure.issue(SeleniumBase.driver.current_url)


def after_feature(context, feature):
    pass


def after_scenario(context, scenario):
    screenshot_name = str(context.scenario.name).replace(" ", "_")
    FPASeleniumHelper.take_screenshot(screenshot_name)
    allure.attach(SeleniumBase.driver.get_screenshot_as_png(), name="screenshot",
                  attachment_type=AttachmentType.PNG)
    allure.issue(SeleniumBase.driver.current_url)

def after_all(context):
    # For UI automation
    SeleniumBase.dispose()


