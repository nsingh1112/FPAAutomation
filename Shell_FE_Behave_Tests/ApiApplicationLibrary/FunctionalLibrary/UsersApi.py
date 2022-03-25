import time
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Requests_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Requests_Core.Utilities.RandomTestDataUtilities import RandomTestDataGenerator

class UsersApi:
    log = LoggingUtilities().logger()

    def get_available_users(self):
        UsersApi.log.info("Base Uri is: " + RequestsBase.base_uri)
        resource = "public/v2/users"
        RequestsBase.set_endpoint(path_params=resource)
        users_dict = FileUtilities.read_json_file_as_dictionary("UsersApi/GetUsers.json")
        params = users_dict["params"]
        header = users_dict["headers"]
        RequestsBase.get_request(query_params=params, headers=header)
        UsersApi.log.info("The status code is: " + str(RequestsBase.response.status_code))
        UsersApi.log.info("The headers passed as part of the request is: " + str(RequestsBase.response.request.headers))

    def validate_gender_get_users(self, gender, response_json_name):
        user_dict = RequestsBase.response_body_as_dictionary()
        scenario_name = str(response_json_name).replace(" ", "_")
        FileUtilities.write_into_json(user_dict, f"UsersApi/{scenario_name}.json")
        result = False
        for i in user_dict:
            if i["gender"] == gender:
                result = True
                break
        return result

    def create_user(self, user):
        resource = "public/v2/users"
        RequestsBase.set_endpoint(path_params=resource)
        users_dict = FileUtilities.read_json_file_as_dictionary("UsersApi/GetUsers.json")
        header = users_dict["headers"]
        create_user = FileUtilities.read_json_file_as_dictionary("UsersApi/CreateUser.json")
        create_user[user]["email"] = RandomTestDataGenerator.get_email(str(create_user[user]["email"]), 10)
        UsersApi.log.info(create_user[user])
        RequestsBase.post_request(body_data=create_user[user], headers=header)
        UsersApi.log.info("The status code is: " + str(RequestsBase.response.status_code))
        UsersApi.log.info("The headers passed as part of the request is: " + str(RequestsBase.response.request.headers))

    def get_users(self):
        users_dict = FileUtilities.read_json_file_as_dictionary("UsersApi/GetUsers.json")
        base_uri = users_dict["getUsersApi"]["baseUri"]
        UsersApi.log.info("Base Uri is: " + base_uri)
        path_param = users_dict["getUsersApi"]["resource"]
        RequestsBase.set_endpoint(base_uri=base_uri, path_params=path_param)
        params = users_dict["getUsersApi"]["params"]
        header = users_dict["getUsersApi"]["headers"]
        RequestsBase.get_request(query_params=params, headers=header)
        UsersApi.log.info("The status code is: " + str(RequestsBase.response.status_code))
        UsersApi.log.info("The headers passed as part of the request is: " + str(RequestsBase.response.request.headers))

