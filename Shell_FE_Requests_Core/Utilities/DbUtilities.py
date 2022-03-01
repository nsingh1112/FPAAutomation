import os
import mysql.connector
from configparser import ConfigParser


class DbUtilities:
    root_dir = os.path.dirname(os.path.dirname(os.getcwd()))
    configfile = root_dir + '/Shell_FE_Behave_Tests/behave.ini'
    configuration = ConfigParser()
    configuration.read(configfile)
    dbconnection = None

    @staticmethod
    def create_mysql_connection():
        """This  is used to create connection with the database"""

        DbUtilities.dbconnection = mysql.connector.connect(
            host=DbUtilities.configuration['database']['host'],
            user=DbUtilities.configuration['database']['user'],
            password=DbUtilities.configuration['database']['password'],
            database=DbUtilities.configuration['database']['database']
        )
        return DbUtilities.dbconnection

    @staticmethod
    def fetchalldata(dbquery):
        """This is used to fetch all the data from the table
           :args:
                -dbquery- MYSQL query to fetch the data
           Returns : It will return the data in the dictionary format
        """
        dbcursor = DbUtilities.dbconnection.cursor()
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
        dbcursor = DbUtilities.dbconnection.cursor()
        dbcursor.execute(dbquery)
        dbdata = dbcursor.fetchone()
        return dbdata

    @staticmethod
    def closeconnection():
        """This is used to close MYSQL server connection"""
        DbUtilities.dbconnection.close()



