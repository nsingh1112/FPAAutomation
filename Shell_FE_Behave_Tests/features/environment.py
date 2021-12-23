import os
import sys
import allure
from allure_commons.types import AttachmentType
sys.path.insert(0, os.path.dirname(os.getcwd()))
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities


def before_all(context):
    # For UI automation
    SeleniumBase.initialize_values()
    # For Mobile automation
    AppiumBase.start_appium_server()
    AppiumBase.read_values()


def before_feature(context, feature):
    if "web" in context.feature.tags:
        SeleniumBase.browser_initialization()
    elif "mobile" in context.feature.tags:
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
    # region Copy history contents from Reports to AllureJson folder
    src_directory = os.path.dirname(os.getcwd()) + "/Shell_FE_Behave_Tests/TestResults/Reports/history/"
    dst_directory = os.path.dirname(os.getcwd()) + "/Shell_FE_Behave_Tests/TestResults/AllureJson/history/"
    all_files = os.listdir(src_directory)
    for file in all_files:
        shutil.move(src_directory + file, dst_directory + file)
    # endregion
    # For UI automation
    SeleniumBase.dispose()
    # For mobile automation
    AppiumBase.stop_appium_server()
