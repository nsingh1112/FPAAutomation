from behave import *

from Shell_FE_Selenium_Core.Utilities.EncryptionDecryptionUtilities import EncryptionDecryption
from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities
from Shell_FE_Requests_Core.Utilities.EncryptionDecryptionUtilities import EncryptionDecryption
from Shell_FE_Requests_Core.Utilities.AssertionUtilities import AssertionUtilities


@When('user enter the details for password to be encrypted')
def step_impl(context):
    result = EncryptionDecryption.encrypt_user_creds(env="UAT", user_role="System Administrator", username="user1", password="pass1")
    AssertionUtilities.assert_if_true(result)

@When('user enter the details for password to be decrypted')
def step_impl(context):
    result = EncryptionDecryption.decrypt_user_creds(environment = "UAT", position = "System Administrato", name = "user1")
    AssertionUtilities.assert_if_true(result)
