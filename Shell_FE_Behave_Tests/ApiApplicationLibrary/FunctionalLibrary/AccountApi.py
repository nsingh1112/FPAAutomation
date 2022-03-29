from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Requests_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Requests_Core.Utilities.RandomTestDataUtilities import RandomTestDataGenerator


class AccountApi:
    log = LoggingUtilities().logger()

    def create_account(self):
        account_dict = FileUtilities.read_json_file_as_dictionary("AccountCreation/CreateAccount.json")
        base_uri = account_dict["baseUri"]
        AccountApi.log.info("Base Uri is: " + base_uri)
        path_param = account_dict["resource"]
        RequestsBase.set_endpoint(base_uri=base_uri, path_params=path_param)
        access_token = FileUtilities.read_json_file_as_dictionary("AccountCreation/AccessToken.json")
        AccountApi.log.info(str(access_token["access_token"]))
        account_dict["headers"]["Authorization"] = str(account_dict["headers"]["Authorization"]) + str(access_token["access_token"])
        header = account_dict["headers"]
        account_dict["requestPayload"]["Name"] = RandomTestDataGenerator.get_name("full_name")
        AccountApi.log.info(account_dict["requestPayload"]["Name"])
        AccountApi.log.info(account_dict["requestPayload"])
        AccountApi.log.info(header)
        RequestsBase.post_request(body_json=account_dict["requestPayload"], headers=header)
        AccountApi.log.info("The status code is: " + str(RequestsBase.response.status_code))
        AccountApi.log.info("The headers passed as part of the request is: " + str(RequestsBase.response.request.headers))
        AccountApi.log.info(RequestsBase.response_body_as_dictionary())