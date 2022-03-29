import time
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Requests_Core.Utilities.LoggingUtilities import LoggingUtilities


class JsonComparison:
    log = LoggingUtilities().logger()

    def get_expected_node_value(self):
        expected_node_data = FileUtilities.read_json_file_as_dictionary("UsersApi/JsonComparisonExpectedData.json")
        return expected_node_data['expected_node_data']

    def get_expected_text(self):
        expected_text = FileUtilities.read_json_file_as_dictionary("UsersApi/JsonComparisonExpectedData.json")
        return expected_text['expected_text']

    def get_threshold_value(self):
        threshold_value = FileUtilities.read_json_file_as_dictionary("UsersApi/JsonComparisonExpectedData.json")
        return threshold_value['threshold']
