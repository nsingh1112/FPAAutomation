import os
import sys
import allure
from allure_commons.types import AttachmentType
sys.path.insert(0, os.path.dirname(os.getcwd()))
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities


def before_all(context):
    SeleniumBase.initialize_values()
    SeleniumBase.browser_initialization()

def after_step(context, step):
    if step.status == "failed":
        screenshot_name = str(context.scenario.name).replace(" ", "_")
        BrowserUtilities.take_screenshot(screenshot_name)

def after_scenario(context, scenario):
    if scenario.status == "failed":
        allure.attach(SeleniumBase.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=AttachmentType.PNG)

def after_all(context):
    # For UI automation
    SeleniumBase.dispose()
