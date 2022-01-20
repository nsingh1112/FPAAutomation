import os
import mysql.connector
from configparser import ConfigParser


class DbUtilities:
    current_dir = os.path.dirname(os.getcwd())
    root_dir = os.path.dirname(current_dir)
    configfile = root_dir + '/Shell_FE_Behave_Tests/behave.ini'
    configuration = ConfigParser()
    configuration.read(configfile)

    @staticmethod
    def creatconnection():
        """This  is used to create the connection for the database"""

        global dbconnection
        dbconnection = mysql.connector.connect(
            host=DbUtilities.configuration['DbValues']['host'],
            user=DbUtilities.configuration['DbValues']['user'],
            password=DbUtilities.configuration['DbValues']['password'],
            database=DbUtilities.configuration['DbValues']['database']
        )
        return dbconnection

    # @staticmethod
    # def executquery(query):
    #   dbcursor = DbUtilities.creatconnection().cursor()
    #   execute = dbcursor.execute(query)
    #   return execute

    @staticmethod
    def fetchalldata(dbquery):
        """This is used to fetch all the data from the table
           :args:
                -dbquery- MYSQL query to fetch the data
           Returns : It will return the data in the dictionary format
        """
        dbcursor = DbUtilities.creatconnection().cursor()
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
        dbcursor = DbUtilities.creatconnection().cursor()
        dbcursor.execute(dbquery)
        dbdata = dbcursor.fetchone()
        return dbdata

    @staticmethod
    def closeconnection():
        """This is used to close MYSQL server connection"""
        DbUtilities.creatconnection().close()


test = DbUtilities()
test.creatconnection()
data = test.fetchalldata("select * from FEteam")
print(data)
data1 = test.fetchone("select * from FEteam")
print(data1)
test.closeconnection()

