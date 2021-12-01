import unittest

from Shell_FE_Appium_Core.AppiumBase import AppiumBase


class AssertUtilities():

    #def __init__(self,driver):
        #self.driver = driver

    @staticmethod
    def assertEquals(actualValue ,expectedValue):
       if actualValue is  None or expectedValue is  None:
           assert False ,"Either Actual or Expected Value is Null"
       assert actualValue == expectedValue , "Actual value is not equals to the expected value"
       #self.assertEqual(actualValue,expectedValue,msg="Actual value and expected value are not same")

    @staticmethod
    def assertNotEquals(actualValue,expectedValue):
        if actualValue is None or expectedValue is None:
            assert False, "Either Actual or Expected Value is Null"
        assert actualValue != expectedValue, "Actual Value is equals to the expected value"

    staticmethod
    def assertValueInList(valueToBeInList,listValue):
        if valueToBeInList is None or listValue is None:
            assert False, "Either Actual or Expected Value is Null"
        assert valueToBeInList in listValue, "Expected value is not in the list"







