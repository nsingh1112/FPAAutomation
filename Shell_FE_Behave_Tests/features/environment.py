import os
import sys
import allure
from allure_commons.types import AttachmentType
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
sys.path.insert(0, os.path.dirname(os.getcwd()))
from Shell_FE_Requests_Core.RequestsBase import RequestsBase


def before_all(context):
    RequestsBase.initialize_values()

