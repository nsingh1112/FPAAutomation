from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.LoggingUtilities import LoggingUtilities


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
        # client_id = ""
        # client_secret = ""
        # token_url = ""
        # username = ""
        # password = ""

        client_id = "3MVG90J3nJBMnqrSl_IljUnQrWdUnYWJ0zHjPfS32RsfN4rSroAQMpXmpp.BM4Nan6ZOz1SNXBussyS2gp5A6"
        client_secret = "80E6E932427D5D4A2EE0D89002B278C7EBF07F0320DC34600D4AAB2649B42AAC"
        token_url = "https://shell-gc--staging.my.salesforce.com/services/oauth2/token"
        test_url = "https://shell-gc--staging.my.salesforce.com/services/data/v53.0"
        username = "insadl@shell.com.shell-gc.staging"
        password = "Springiscoming51@"

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
        # test_url = ""
        test_url = "https://shell-gc--staging.my.salesforce.com/services/data/v53.0"
        api_call_headers = {'Authorization': 'Bearer ' + access_token}
        RequestsBase.get_request(url=test_url, headers=api_call_headers)
        Oauth2.log.info("The status code is: " + str(RequestsBase.response.status_code))