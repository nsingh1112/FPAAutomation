import unittest
class AssertUtilities():
    def __init__(self,driver):
        self.driver = driver


    def assertEquals(self ,actualValue ,expectedValue):
       if actualValue is  None or expectedValue is  None:
           assert False ,"Either Actual or Expected Value is Null"
       assert actualValue == expectedValue , "Actual value is not equals to the expected value"
       #self.assertEqual(actualValue,expectedValue,msg="Actual value and expected value are not same")

    def assertNotEquals(self,actualValue,expectedValue):
        if actualValue is None or expectedValue is None:
            assert False, "Either Actual or Expected Value is Null"
        assert actualValue != expectedValue, "Actual Value is equals to the expected value"

    def assertValueInList(self,valueToBeInList,listValue):
        if valueToBeInList is None or listValue is None:
            assert False, "Either Actual or Expected Value is Null"
        assert valueToBeInList in listValue, "Expected value is not in the list"







