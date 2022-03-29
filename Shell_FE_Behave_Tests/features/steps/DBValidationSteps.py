from behave import *
from Shell_FE_Appium_Core.Utilities.DbUtilities import DbUtilities


@given('Creating the connection with the DB')
def create_connection(context):
    db_status = DbUtilities.create_mysql_connection()
    print(db_status)


@when('Fetching all the values from the DB')
def fetch_all(context):
    db_values = DbUtilities.fetchalldata("Select * from FEteam")
    print(db_values)


@when('Fetching single value from the DB')
def fetch_one(context):
    selected_value = DbUtilities.fetchone("Select emp_name from FEteam where Emp_id =2")
    print(selected_value)
