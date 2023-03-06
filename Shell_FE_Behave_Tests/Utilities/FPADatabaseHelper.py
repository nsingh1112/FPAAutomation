import os
import mysql.connector
import pyodbc
import pandas as pd
from configparser import ConfigParser
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase


class FPADatabaseHelper:
    configuration = None
    db_connection = None
    sql_connection = None
    current_working_directory = os.path.dirname(os.getcwd())
    excel_report = current_working_directory + "\\Shell_FE_Behave_Tests\\TestResults\\"

    # region MYSQL Integration
    @staticmethod
    def create_mysql_connection():
        """This  is used to create the connection for the database"""
        FPADatabaseHelper.configuration = SeleniumBase.read_config()
        FPADatabaseHelper.db_connection = mysql.connector.connect(
            host=FPADatabaseHelper.configuration['database']['host'],
            user=FPADatabaseHelper.configuration['database']['user'],
            password=FPADatabaseHelper.configuration['database']['password'],
            database=FPADatabaseHelper.configuration['database']['database']
        )
        return FPADatabaseHelper.db_connection

    @staticmethod
    def fetchalldata(dbquery):
        """This is used to fetch all the data from the table
           :args:
                -dbquery- MYSQL query to fetch the data
           Returns : It will return the data in the dictionary format
        """
        dbcursor = FPADatabaseHelper.db_connection.cursor()
        dbcursor.execute(dbquery)
        dbdata = dbcursor.fetchall()
        return dbdata

    @staticmethod
    def fetchone(dbquery):
        """This is used to fetch the first row of the table
        :args:
              -dbquery- MYSQL query to fetch the data
         Returns : It will return the data in the dictionary format
        """
        dbcursor = FPADatabaseHelper.db_connection.cursor()
        dbcursor.execute(dbquery)
        dbdata = dbcursor.fetchone()
        return dbdata

    @staticmethod
    def closeconnection():
        """This is used to close MYSQL server connection"""
        FPADatabaseHelper.db_connection.close()

    # endregion

    # region SQL Integration
    @staticmethod
    def create_sql_connection():
        """This method is used to create the connection from the database"""
        FPADatabaseHelper.configuration = SeleniumBase.read_config()
        FPADatabaseHelper.sql_connection = pyodbc.connect(
            Driver=FPADatabaseHelper.configuration['database']['driver'],
            Server=FPADatabaseHelper.configuration['database']['SQL_Server'],
            Database=FPADatabaseHelper.configuration['database']['SQL_database'],
            Trusted_Connection=FPADatabaseHelper.configuration['database']['Trusted_Connection'],
            UID=FPADatabaseHelper.configuration['database']['sql_server_Username'],
            PWD=FPADatabaseHelper.configuration['database']['sql_server_Password'],
            AUTHENTICATION=FPADatabaseHelper.configuration['database']['authentication_type']
        )
        return FPADatabaseHelper.sql_connection

    @staticmethod
    def execute_sql_command(sql_query):
        """This helps to execute the sql query
           :args:
                - sql_query : SQL query needs to perform
        """

        sql_cursor = FPADatabaseHelper.sql_connection.cursor()
        sql_values = sql_cursor.execute(sql_query)
        return sql_values

    @staticmethod
    def close_sql_connection():
        """This will close the sql connection"""
        FPADatabaseHelper.sql_connection.close()

    @staticmethod
    def get_drivers():
        """This will help you find the drivers available in the system"""
        driver_list = pyodbc.drivers()
        return driver_list

    @staticmethod
    def export_datas_to_excel(sql_query, file_name):
        """This will export the datas to excel directly
           :args:
               - sql_query : SQL query to fetch the data
               - file_name : name of the file to be stored
        """
        df = pd.read_sql(sql=sql_query, con=FPADatabaseHelper.sql_connection)
        df.to_excel(FPADatabaseHelper.excel_report + file_name + ".xlsx")

        # region SQL Integration

    @staticmethod
    def create_sql_connection1():
        """This method is used to create the connection from the database"""

        FPADatabaseHelper.sql_connection = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
                    "Server=lcf-procurementd.database.windows.net;"
                    "Database=feedstockprocurement-dev;"
                    "UID=feedstockadmin;"
                    "PWD=Feedst0ckp@ssword;"
        )
        return FPADatabaseHelper.sql_connection



    # endregion
