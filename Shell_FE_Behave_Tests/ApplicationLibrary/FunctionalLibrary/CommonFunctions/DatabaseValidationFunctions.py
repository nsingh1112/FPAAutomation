import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.PageControls.UnprocessedRecordsPageControls import \
    UnprocessedRecordsPageControls
from Shell_FE_Behave_Tests.Utilities.FPADatabaseHelper import FPADatabaseHelper


class DatabaseValidationFunctions:

    def __init__(self, driver):
        self.driver = driver


    def get_records(self,query):
        values = FPADatabaseHelper.execute_sql_command(query)
        words = []
        for row in values:
            words.append(row)
        return words

    def get_rowCount(self, query,cnxn):
        cursor = cnxn.cursor()
        cursor.execute(query)
        rowcount = cursor.fetchall()[0][0]
        return rowcount

    def get_documentRecordsfromDB(self,dashboardItems):
        documentsDBColHeader = ['Filename', 'Document_Type', 'Email_From', 'Email_Subject', 'Email_Received_Timestamp']
        words = []
        for dbitem in documentsDBColHeader:
            query = "select top 1("+dbitem+") from FILE_SOURCE where Document_Category = '"+dashboardItems+"'"
            values = FPADatabaseHelper.execute_sql_command(query)
            for row in values:
                words.append(row)
        return words

