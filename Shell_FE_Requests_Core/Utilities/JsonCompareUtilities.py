import json
import re
import jsonpath
import requests
from nested_lookup import nested_lookup
from deepdiff import DeepDiff
from Shell_FE_Requests_Core.Utilities.LoggingUtilities import LoggingUtilities


class JsonCompareUtils:
    keys = []
    values = []
    log_obj = LoggingUtilities()
    log = log_obj.logger()

    @staticmethod
    def ordered(obj):
        """
        Ordered is a method which will take a json data as a parameter and verify dict , list
        and sort the data based on dict and list instance and return sorted json data
        :Args:
            -obj : json data file
        :Returns:
            Sorted json object
        """
        if isinstance(obj, dict):
            return sorted((key, JsonCompareUtils.ordered(value)) for key, value in obj.items())
        if isinstance(obj, list):
            return sorted(JsonCompareUtils.ordered(x) for x in obj)
        else:
            return obj

    @staticmethod
    def response_isequal(res1, res2):
        """
        It's a method used to compare 2 json data files,
        :Args:
            file1_data : Json data file 1
            file2_data : Json data file 2
        :Returns:
            boolean
        """
        if isinstance(res1, requests.models.Response) and isinstance(res2, requests.models.Response):
            json1_data = json.loads(res1.text)
            json2_data = json.loads(res2.text)
            return JsonCompareUtils.ordered(json1_data) == JsonCompareUtils.ordered(json2_data)
        elif isinstance(res1, (dict, list,str)) and isinstance(res2, requests.models.Response):
            json2_data = json.loads(res2.text)
            return JsonCompareUtils.ordered(res1) == JsonCompareUtils.ordered(json2_data)
        elif isinstance(res1, requests.models.Response) and isinstance(res2, (dict, list, str)):
            json1_data = json.loads(res1.text)
            return JsonCompareUtils.ordered(json1_data) == JsonCompareUtils.ordered(res2)
        elif isinstance(res1, (dict, list, str)) and isinstance(res2, (dict, list, str)):
            return JsonCompareUtils.ordered(res1) == JsonCompareUtils.ordered(res2)
        else:
            return False

    # @staticmethod
    # def read_json(read_file):
    #     with open(read_file) as file:
    #         json_data = json.load(file)
    #     return json_data

    @staticmethod
    def search_values_in_response_with_key(json_obj, user_key):
        """
        This is the method to search the particular value based on the user provided key
        :Args:
            json_obj : Json Data
            user_ey : Key to search in the json data
        :Returns:
            List of values matched to user key
        """
        if isinstance(json_obj, requests.models.Response):

            data = json.loads(json_obj.text)
            JsonCompareUtils.log.info("Following are the values matched with key  ' {} ' ".format(user_key))
            JsonCompareUtils.log.info(nested_lookup(user_key, data)[0])
            return nested_lookup(user_key, data)
        else:
            data = json.loads(json_obj)
            JsonCompareUtils.log.info("Following are the values matched with key  ' {} ' ".format(user_key))
            JsonCompareUtils.log.info(nested_lookup(user_key, data)[0])
            return nested_lookup(user_key, data)

    @staticmethod
    def get_node_value(res, key):
        """
        This method can be used to get a value for a particular key from json response.

        :Args:
            res: api response data
            key: Key item to search in the response data
        :Returns:
            List of Values for key provided
        """

        # json_response = json.loads(res.text)
        # data = res.text
        # parse_json = json.loads(data)
        # jsonpath.jsonpath(parse_json, "['data'][0]['email']")
        #
        # JsonCompareUtils.log.info(res)
        # if isinstance(res, list):
        #     res = defaultdict(list)
        #     for sub in res:
        #         for key in sub:
        #             res[key].append(sub[key])
        #     JsonCompareUtils.log.info(jsonpath.jsonpath(res, key))
        #     return jsonpath.jsonpath(res, key)
        # else:
        #     JsonCompareUtils.log.info(jsonpath.jsonpath(res, key))
        #     return jsonpath.jsonpath(res, key)
        if isinstance(res, requests.models.Response):
            value = jsonpath.jsonpath(res.json(), key)
            JsonCompareUtils.log.info(f"Node value: '{value[0]}' for jsonpath : '{key}'")
            return value[0]
        else:
            value = jsonpath.jsonpath(res, key)
            JsonCompareUtils.log.info(f"Node value: '{value[0]}' for jsonpath : '{key}'")
            return value[0]

        # value = jsonpath.jsonpath(res, key)
        # JsonCompareUtils.log.info(f"Node value: '{value[0]}' for jsonpath : '{key}'")
        # return value[0]

    # @staticmethod
    # def search_key(json_file_path):
    #     json_data = JsonCompareUtils.read_json(json_file_path)
    #     return json_data

    @staticmethod
    def find_difference(res1, res2):
        json1_data = json.loads(res1.text)
        json2_data = json.loads(res2.text)
        # keys = []
        # values = []
        # global JsonCompareUtils.keys

        if len(json1_data) != len(json2_data):

            for js1, js2 in zip(JsonCompareUtils.ordered(json1_data), JsonCompareUtils.ordered(json2_data)):
                if js1[0] != js2[0]:
                    # keys.append((js1[0], js2[0]))
                    JsonCompareUtils.keys.append((js1[0], js2[0]))
                if js1[1] != js2[1]:
                    # values.append((js1[1], js2[1]))
                    JsonCompareUtils.values.append((js1[1], js2[1]))
        return JsonCompareUtils.keys, JsonCompareUtils.values

    @staticmethod
    def deep_difference(res1, res2):
        json1_data = json.loads(res1.text)
        json2_data = json.loads(res2.text)
        deep_diff = DeepDiff(json1_data, json2_data, ignore_order=True)
        JsonCompareUtils.log.info(f"Difference between the responses: {deep_diff} ")
        return deep_diff

    @staticmethod
    def is_value_present_in_res(value, res):
        res_str = res.text
        JsonCompareUtils.log.info("Searching a {} value in {} res".format(value, res_str))
        pattern = r'(^|[^\w]){}([^\w]|$)'.format(value)
        pattern = re.compile(pattern, re.IGNORECASE)
        matches = re.search(pattern, res_str)
        return bool(matches)
