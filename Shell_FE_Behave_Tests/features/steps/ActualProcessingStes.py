from Shell_FE_Selenium_Core.Utilities.DbUtilities import DbUtilities
from behave import *


@given('Creating the connection with the DB')
def create_connection(context):
    # db_status = DbUtilities.create_mysql_connection()
    # print(db_status)
    sql_db_connection = DbUtilities.create_sql_connection()
    print(sql_db_connection)
    values = DbUtilities.execute_sql_command("select * from myemployeelist")
    for row in values:
        print(row)
    DbUtilities.export_datas_to_excel("select * from myemployeelist","my_data")


@when('Fetching all the values from the DB')
def fetch_all(context):
    db_values = DbUtilities.fetchalldata("Select * from FEteam")
    print(db_values)


@when('Fetching single value from the DB')
def fetch_one(context):
    selected_value = DbUtilities.fetchone("Select emp_name from FEteam where Emp_id =2")
    print(selected_value)


