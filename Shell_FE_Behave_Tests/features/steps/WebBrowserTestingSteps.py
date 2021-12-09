from behave import *

from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionLibrary.WebBrowserFunctions import BrowserFunctions


@given('I have launched the chrome app')
def launching_app(context):
   context.browserfeatures = BrowserFunctions()
   context.browserfeatures.launc_web("https://hub.shell.com")

@when(u'I Am passing the URL')
def step_impl(context):
    pass
    raise NotImplementedError(u'STEP: When I Am passing the URL')

@then(u'I verify it landed on the corresponding URL')
def step_impl(context):
    pass
    raise NotImplementedError(u'STEP: Then I verify it landed on the corresponding URL')
