import time

from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Requests_Core.Utilities.LoggingUtilities import LoggingUtilities


class UsersApi:
    log = LoggingUtilities().logger()

    def get_available_users(self):
        UsersApi.log.info("Base Uri is: " + RequestsBase.base_uri)
        resource = "public/v2/users"
        RequestsBase.set_endpoint(resource)
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

    def create_user(self):
        resource = "public/v2/users"
        RequestsBase.set_endpoint(resource)
        users_dict = FileUtilities.read_json_file_as_dictionary("UsersApi/GetUsers.json")
        header = users_dict["headers"]
        create_user = FileUtilities.read_json_file_as_dictionary("UsersApi/CreateUser.json")
        time_stamp = str(time.strftime("%H_%S")).replace("_", "")
        create_user["email"] = f"abc{time_stamp}@amail.com"
        RequestsBase.post_request(body_data=create_user, headers=header)
        UsersApi.log.info("The status code is: " + str(RequestsBase.response.status_code))
        UsersApi.log.info("The headers passed as part of the request is: " + str(RequestsBase.response.request.headers))
