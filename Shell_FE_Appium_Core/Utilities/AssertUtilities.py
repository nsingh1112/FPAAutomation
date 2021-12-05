import unittest

from Shell_FE_Appium_Core.AppiumBase import AppiumBase


class AssertUtilities:

    @staticmethod
    def assert_equals(actual_value, expected_value):
        if actual_value is None or actual_value is None:
            assert False, "Either Actual or Expected Value is Null"
        assert actual_value == expected_value, "Actual value is not equals to the expected value"
        # self.assertEqual(actualValue,expectedValue,msg="Actual value and expected value are not same")

    @staticmethod
    def assert_not_equals(actual_value, expected_value):
        if actual_value is None or expected_value is None:
            assert False, "Either Actual or Expected Value is Null"
        assert actual_value != expected_value, "Actual Value is equals to the expected value"

    @staticmethod
    def assert_value_in_list(value_to_be_in_list, list_value):
        if value_to_be_in_list is None or list_value is None:
            assert False, "Either Actual or Expected Value is Null"
        assert value_to_be_in_list in list_value, "Expected value is not in the list"
