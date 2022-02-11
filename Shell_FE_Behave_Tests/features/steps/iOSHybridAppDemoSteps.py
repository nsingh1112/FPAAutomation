import time

from behave import *

from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionalLibrary.iOSHybridDemoFunctions import HybridAppFunctions


@given(u'I launched the mobile native Safari app')
def step_impl(context):
    context.feature.iOS_hybrid = HybridAppFunctions()
    parent_context = context.feature.iOS_hybrid.current_contex()
    print(parent_context)


@when('I am testing the search functionality')
def step_impl(context):
    context.feature.iOS_hybrid.click_search()
    context.feature.iOS_hybrid.pass_value_to_search_field("Python Automation Testing")
    time.sleep(10)


@when('I test the swicth context')
def step_impl(context):
    app_views = context.feature.iOS_hybrid.get_context_of_app()
    print("Total view of the app:",app_views)
    time.sleep(5)


@then(u'I am testing the web_view after switching')
def step_impl(context):
    pass
