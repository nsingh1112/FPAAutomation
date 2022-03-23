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

    def get_access_token(self):
        """
        User needs to provide mandatory details to retrieve access token and then use access token to raise another request
        token_url = Url from which toke  needs to be retrieved
        client_id = consumer key of your connected app
        username = your login username for org
        password =  your org login password
        client_secret = consumer secret of your connected app
        :return:
        """
        client_id = ""
        client_secret = ""
        token_url = ""
        username = ""
        password = ""

        data =  {'grant_type': 'password','username': username, 'password': password, 'client_id': client_id, 'client_secret': client_secret}
        access_token = RequestsBase.get_access_token(url= token_url, data=data)
        UsersApi.log.info("The status code is: " + str(RequestsBase.response.status_code))
        UsersApi.log.info("The headers passed as part of the request is: " + str(RequestsBase.response.request.headers))
        return access_token

    def oauth2_request(self, access_token):
        """
        test_url = instance URL you need to make a request
        :param access_token:
        """
        test_url = ""
        api_call_headers = {'Authorization': 'Bearer ' + access_token}
        RequestsBase.get_request(url=test_url, headers=api_call_headers)
        UsersApi.log.info("The status code is: " + str(RequestsBase.response.status_code))