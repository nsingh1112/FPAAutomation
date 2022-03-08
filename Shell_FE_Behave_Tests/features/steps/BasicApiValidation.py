from behave import Given, When, Then
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Requests_Core.Utilities.AssertionUtilities import AssertionUtilities
import time

@When('user sends a GET request to retrieve user details')
def step_impl(context):
    print("Base Uri is: " + RequestsBase.base_uri)
    resource = "public/v2/users"
    RequestsBase.set_endpoint(resource)
    users_dict = FileUtilities.read_json_file_as_dictionary("UsersApi/GetUsers.json")
    params = users_dict["params"]
    header = users_dict["headers"]
    RequestsBase.get_request(query_params=params, headers=header)
    print("The status code is: " + str(RequestsBase.response.status_code))
    print("The headers passed as part of the request is: " + str(RequestsBase.response.request.headers))


@Then('user validates if the response status is "{expected_code}"')
def step_impl(context, expected_code):
    AssertionUtilities.assert_equals(expected_code, str(RequestsBase.response_status_code()))


@Then('user verifies if "{gender}" user is available in the response body')
def step_impl(context, gender):
    user_dict = RequestsBase.response_body_as_dictionary()
    scenario_name = str(context.scenario.name).replace(" ", "_")
    FileUtilities.write_into_json(user_dict, f"UsersApi/{scenario_name}.json")
    result = False
    for i in user_dict:
        if i["gender"] == gender:
            result = True
            break
    AssertionUtilities.assert_if_true(result)


@When('user sends a POST request to create new user')
def step_impl(context):
    resource = "public/v2/users"
    RequestsBase.set_endpoint(resource)
    users_dict = FileUtilities.read_json_file_as_dictionary("UsersApi/GetUsers.json")
    header = users_dict["headers"]
    create_user = FileUtilities.read_json_file_as_dictionary("UsersApi/CreateUser.json")
    time_stamp = str(time.strftime("%H_%S")).replace("_", "")
    create_user["email"] = f"abc{time_stamp}@amail.com"
    RequestsBase.post_request(body_data=create_user, headers=header)
    print("The status code is: " + str(RequestsBase.response.status_code))
    print("The headers passed as part of the request is: " + str(RequestsBase.response.request.headers))


@Then('user validates if the Create User response status is {expected_code}')
def step_impl(context, expected_code):
    AssertionUtilities.assert_equals(expected_code, str(RequestsBase.response_status_code()))


@Then('user validates if the user has been created successfully')
def step_impl(context):
    user_dict = RequestsBase.response_body_as_dictionary()
    create_user = FileUtilities.read_json_file_as_dictionary("UsersApi/CreateUser.json")
    scenario_name = str(context.scenario.name).replace(" ", "_")
    FileUtilities.write_into_json(user_dict, f"UsersApi/{scenario_name}.json")
    AssertionUtilities.assert_equals(create_user["name"], user_dict["name"])
