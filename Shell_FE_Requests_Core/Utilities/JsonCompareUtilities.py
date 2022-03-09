import json
from collections import defaultdict
import jsonpath
from nested_lookup import nested_lookup


class JsonCompareUtils:
    keys = []
    values = []

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
        json1_data = json.loads(res1.text)
        json2_data = json.loads(res2.text)
        return JsonCompareUtils.ordered(json1_data) == JsonCompareUtils.ordered(json2_data)

    # @staticmethod
    # def read_json(read_file):
    #     with open(read_file) as file:
    #         json_data = json.load(file)
    #     return json_data

    @staticmethod
    def search_values_in_response(json_obj, user_key):
        """
        This is the method to search the particular value based on the user provided key
        :Args:
            json_obj : Json Data
            user_ey : Key to search in the json data
        :Returns:
            List of values matched to user key
        """
        return nested_lookup(user_key, json_obj)

    @staticmethod
    def get_single_node_value(res, key):
        """
        This method can be used to get a value for a particular key from json response.

        :Args:
            res: api response data
            key: Key item to search in the response data
        :Returns:
            List of Values for key provided
        """
        json_response = json.loads(res.text)
        if isinstance(json_response, list):
            res = defaultdict(list)
            for sub in json_response:
                for key in sub:
                    res[key].append(sub[key])
            return jsonpath.jsonpath(res, key)
        else:
            return jsonpath.jsonpath(json_response, key)

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
