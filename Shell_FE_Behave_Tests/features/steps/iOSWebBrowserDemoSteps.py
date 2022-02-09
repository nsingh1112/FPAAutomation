import time

from behave import *
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionLibrary.WebBrowserFunctions import BrowserFunctions


@given('I have launched the safari app')
def launching_app(context):
    context.webBrowser = BrowserFunctions()


@when('I am testing the background and foreground methods')
def testing_background_foreground(context):
    context.webBrowser.check_background()
    context.webBrowser.foreground_app(AppiumBase.bundle_id)
    context.webBrowser.check_background()
    safari_bundleId = FileUtilities.read_json_file_as_dictionary("Appinfo.json")
    context.webBrowser.foreground_app(safari_bundleId["bundleId"])
