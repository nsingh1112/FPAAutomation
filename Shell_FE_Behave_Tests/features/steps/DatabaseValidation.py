import threading
import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities
from behave import *

from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.CommonPageFunctions import \
    CommonPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonFunctions.DatabaseValidationFunctions import \
    DatabaseValidationFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.DocumentsPageFunctions import \
    DocumentsPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.ActualProcessingPageFunctions import \
    ActualProcessingPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.HomePageFunctions import HomePageFunctions
from Shell_FE_Behave_Tests.Utilities.FPADatabaseHelper import FPADatabaseHelper


@when('The user Clicks on documentItems "{documentsItems}" and validates record from database')
def step_impl(context, documentsItems=None):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.databaseValidationFunctions = DatabaseValidationFunctions(SeleniumBase.driver)
    context.documentsPageFunctions = DocumentsPageFunctions(SeleniumBase.driver)
    context.commonPageFunctions = CommonPageFunctions(SeleniumBase.driver)
    sql_db_connection = FPADatabaseHelper.create_sql_connection1()
    if (documentsItems == "Terminal Report"):
       context.homePage_functions.click_terminalReport()
       query = "select count(*) from FILE_SOURCE where Document_Category ='TERMINAL'"
       documentType = "TERMINAL"
    else:
        context.homePage_functions.click_invoices()
        query = "select count(*) from FILE_SOURCE where Document_Category ='INVOICE'"
        documentType = "INVOICE"

    totalnoOfRows =  context.databaseValidationFunctions.get_rowCount(query, sql_db_connection)
    totalnoOfRowsfromUI = context.commonPageFunctions.get_totalNoOfRecords()
    dataFromDB = context.databaseValidationFunctions.get_documentRecordsfromDB(documentType)
    context.documentsPageFunctions.validate_data(dataFromDB)
    AssertionUtilities.assert_equals(totalnoOfRows, totalnoOfRowsfromUI)

@when('The user Clicks on LogsItems "{logsItems}" and validates record from database')
def step_impl(context, logsItems=None):
    context.homePage_functions = HomePageFunctions(SeleniumBase.driver)
    context.databaseValidationFunctions = DatabaseValidationFunctions(SeleniumBase.driver)
    context.commonPageFunctions = CommonPageFunctions(SeleniumBase.driver)
    sql_db_connection = FPADatabaseHelper.create_sql_connection1()
    if (logsItems == "Reconciliation Errors"):
       context.homePage_functions.click_reconciliationErrors()
       query = "select count(*) from error_log where Error_msg in('Failed','Resolved')  "
    else:
        context.homePage_functions.click_actualErrors()
        query = "select count(*) from error_log where Error_msg not in('Failed','Resolved')"

    totalnoOfRows = context.databaseValidationFunctions.get_rowCount(query, sql_db_connection)
    totalnoOfRowsfromUI = context.commonPageFunctions.get_totalNoOfRecords()
    #dataFromDB = context.databaseValidationFunctions.get_documentRecordsfromDB(documentType)
    #context.documentsPageFunctions.validate_data(dataFromDB)
    AssertionUtilities.assert_equals(totalnoOfRows, totalnoOfRowsfromUI)

@when('The user varifies the aggregated data columns in database')
def step_impl(context):
    context.databaseValidationFunctions = DatabaseValidationFunctions(SeleniumBase.driver)
    context.actualProcessingPageFunctions = ActualProcessingPageFunctions(SeleniumBase.driver)
    sql_db_connection = FPADatabaseHelper.create_sql_connection1()
    query="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'AGGREGATED_DATA'"
    xx = context.databaseValidationFunctions.get_records(query)
    context.actualProcessingPageFunctions.validate_colunmheaders(xx)









