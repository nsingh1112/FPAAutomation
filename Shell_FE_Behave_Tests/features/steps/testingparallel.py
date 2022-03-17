import time
from allure_commons._allure import step
from behave.__main__ import main as behave_main
import threading
from behave import *
import os

@step(u'run in parallel "{feature}"')
def step_impl(context, feature):
    # print("running parallel tests ")
    t = threading.Thread(
        name='run test parallel',
        target=parallel_executor,
        args=[context, feature])
    t.start()


def parallel_executor(context, feature_name):
    behave_main('-i "{}" --no-capture --no-skipped'.format(feature_name))
