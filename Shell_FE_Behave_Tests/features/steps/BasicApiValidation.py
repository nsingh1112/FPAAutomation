from behave import Given, When, Then

from Shell_FE_Behave_Tests.ApiApplicationLibrary.FunctionalLibrary.UsersApi import UsersApi
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Requests_Core.Utilities.AssertionUtilities import AssertionUtilities
import time


@When('user sends a GET request to retrieve user details')
def step_impl(context):
    context.feature.users_api = UsersApi()
    context.feature.users_api.get_available_users()


@Then('user validates if the response status is "{expected_code}"')
def step_impl(context, expected_code):
    AssertionUtilities.assert_equals(expected_code, str(RequestsBase.response_status_code()))


@Then('user verifies if "{gender}" user is available in the response body')
def step_impl(context, gender):
    result = context.feature.users_api.validate_gender_get_users(gender, context.scenario.name)
    AssertionUtilities.assert_if_true(result)


@When('user sends a POST request to create new "{user}"')
def step_impl(context, user):
    context.feature.users_api.create_user(user)


@Then('user validates if the Create User response status is {expected_code}')
def step_impl(context, expected_code):
    AssertionUtilities.assert_equals(expected_code, str(RequestsBase.response_status_code()))


@Then('user validates if the "{user}" has been created successfully')
def step_impl(context, user):
    user_dict = RequestsBase.response_body_as_dictionary()
    create_user = FileUtilities.read_json_file_as_dictionary("UsersApi/CreateUser.json")
    scenario_name = str(context.scenario.name).replace(" ", "_")
    FileUtilities.write_into_json(user_dict, f"UsersApi/{scenario_name}.json")
    AssertionUtilities.assert_equals(create_user[user]["name"], user_dict["name"])

@When('user sends a GET request to retrieve users')
def step_impl(context):
    context.feature.users_api.get_users()
