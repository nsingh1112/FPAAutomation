from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Requests_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Requests_Core.Utilities.EncryptionDecryption import EncryptionDecryption

class Oauth2:
    log = LoggingUtilities().logger()

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
        username = "insadl@shell.com.shell-gc.staging"
        environment = "UAT"
        position = "System Administrator"
        users_dict = FileUtilities.read_json_file_as_dictionary("SecretIds.json")
        client_id = users_dict["client_id"]
        client_secret = users_dict["client_secret"]
        token_url = users_dict["token_url"]
        password = EncryptionDecryption.decrypt_user_creds(environment=environment, position=position,
                                                         name=username)
        Oauth2.log.info("result: " + str(password))
        data =  {'grant_type': 'password','username': username, 'password': password, 'client_id': client_id, 'client_secret': client_secret}
        access_token = RequestsBase.get_access_token(url= token_url, data=data)
        Oauth2.log.info("The status code is: " + str(RequestsBase.response.status_code))
        Oauth2.log.info("The headers passed as part of the request is: " + str(RequestsBase.response.request.headers))
        return access_token

    def oauth2_request(self, access_token):
        """
        test_url = instance URL you need to make a request
        :param access_token:
        """
        users_dict = FileUtilities.read_json_file_as_dictionary("SecretIds.json")
        test_url = users_dict["test_url"]
        api_call_headers = {'Authorization': 'Bearer ' + access_token}
        RequestsBase.get_request(url=test_url, headers=api_call_headers)
        Oauth2.log.info("The status code is: " + str(RequestsBase.response.status_code))