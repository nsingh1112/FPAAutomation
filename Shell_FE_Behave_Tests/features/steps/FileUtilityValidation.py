from behave import Given, When, Then

from Shell_FE_Selenium_Core.Utilities.FileUtilities import FileUtilities


@When('user reads the values available in excel by cell value')
def step_impl(context):
    name = FileUtilities.read_cell_value_from_excel("TestData1.xlsx", "PersonDetails", "B2")
    age = FileUtilities.read_cell_value_from_excel("TestData1.xlsx", "PersonDetails", "C2")
    phone = FileUtilities.read_cell_value_from_excel("TestData1.xlsx", "PersonDetails", "D2")
    dob = FileUtilities.read_cell_value_from_excel("TestData1.xlsx", "PersonDetails", "E2")
    print("NAME: " + name)
    print("AGE: " + str(age))
    print("PHONE: " + str(phone))
    print("DOB: " + str(dob))


@When('user reads the values available in excel by rowname')
def step_impl(context):
    value_dict = FileUtilities.read_excel_by_row_name("TestData1.xlsx", "PersonDetails", "Testcase3")
    print("NAME: " + value_dict["Name"] + ", AGE: " + str(value_dict["Age"]) + ", PHONE: " + str(value_dict[
                                                                                                     "Phonenumber"]) + ", DOB: " + str(
        value_dict["DOB"]))


@When('user reads the values from json file')
def step_impl(context):
    value_dict = FileUtilities.read_json_file_as_dictionary("TestData2.json")
    print("NAME: " + value_dict["Name"] + ", AGE: " + str(value_dict["Age"]) + ", PHONE: " + str(
        value_dict["Phonenumber"]) + ", DOB: " + str(value_dict["DOB"]))


@When('user reads the values from json string')
def step_impl(context):
    person_json = '{"Name": "Michael", "Age": "31", "Phonenumber": 9987676631, "DOB": "28-09-1989"}'
    value_dict = FileUtilities.read_json_string_as_dictionary(person_json)
    print("NAME: " + value_dict["Name"] + ", AGE: " + str(value_dict["Age"]) + ", PHONE: " + str(
        value_dict["Phonenumber"]) + ", DOB: " + str(value_dict["DOB"]))


@When('user converts dictionary into json string')
def step_impl(context):
    value_dict = {"Name": "Michael", "Age": "31", "Phonenumber": 9987676631, "DOB": "28-09-1989"}
    json_str = FileUtilities.convert_dictionary_to_json_string(value_dict)
    print("JSON_STRING: \n" + json_str)


@When('user writes into json file')
def step_impl(context):
    # value_dict = {"Name": "Walter White", "Age": "51", "Phonenumber": 9991976631, "DOB": "28-09-1971"}
    value_dict = {"Name": "Hank Schrader", "Age": "46", "Phonenumber": 9923476631, "DOB": "28-09-1976"}
    FileUtilities.write_into_json(value_dict, "NewJson.json")


@When('user writes into existing excel sheet')
def step_impl(context):
    value_dict = {"Name": "Ada", "Age": "30", "Phonenumber": 9923476123, "DOB": "28-09-1991"}
    FileUtilities.write_into_existing_excel_file(value_dict, "TestData1.xlsx", "PersonDetails", "Testcase3")


@When('user writes into new excel sheet')
def step_impl(context):
    # value_dict = {"Name": "Polly Gray", "Age": "45", "Phonenumber": 9921236123, "DOB": "28-09-1976"}
    value_dict = {"Name": "Michael Gray", "Age": "20", "Phonenumber": 9932146123, "DOB": "28-09-2001"}
    FileUtilities.write_into_new_excel_file(value_dict, "TestData3.xlsx", "TestDetails")


@When('user writes into excel by cellname')
def step_impl(context):
    FileUtilities.write_into_excel_via_cell_name("TestData1.xlsx", "PersonDetails", "B2", "Tommy")


@When('user reads the values available in csv by rowname')
def step_impl(context):
    dicti = FileUtilities.read_csv_by_row_name("TestData41.csv", "Testcase_id", "Testcase3")
    print(dicti)

# @When('user writes a dictionary into a csv file')
# def step_impl(context):
#     value_dict = {"Name": "Gina Gray", "Age": "20", "Phonenumber": 9932146123, "DOB": "28-09-2001"}
#     FileUtilities.write_into_new_csv_file(value_dict, "TestData5.csv")