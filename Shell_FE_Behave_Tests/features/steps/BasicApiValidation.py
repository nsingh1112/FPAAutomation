from behave import Given, When, Then
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.FileUtilities import FileUtilities


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
