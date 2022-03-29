from Shell_FE_Selenium_Core.Utilities.RandomTestDataUtilities import RandomTestDataGenerator
from behave import when


@when(u'user get current datetime')
def step_impl(context):
    current_date_time = RandomTestDataGenerator.get_current_datetime("Australia/Lindeman")
    print(current_date_time)




@when(u'user get first name')
def step_impl(context):
    first_name = RandomTestDataGenerator.get_name("first_name")
    print("First Name: " + first_name)


@when(u'user get full name')
def step_impl(context):
    full_name = RandomTestDataGenerator.get_name("full_name")
    print(full_name)


@when(u'user get address')
def step_impl(context):
    print(RandomTestDataGenerator.get_address("en_IN"))


@when(u'user get date')
def step_impl(context):
    d=RandomTestDataGenerator.get_date_time("date")
    print(d)


@when(u'user get date and time')
def step_impl(context):
    data_time = RandomTestDataGenerator.get_date_time("datetime")


@when(u'user get email')
def step_impl(context):
    email = RandomTestDataGenerator.get_email("shell.com",10)
    print(email)


@when(u'user get phone number')
def step_impl(context):
    ph = RandomTestDataGenerator.get_phone_number("US")
    print(ph)


@when(u'user get ID')
def step_impl(context):
    ID = RandomTestDataGenerator.get_id("alpha_numeric")
    print(ID)


@when(u'user gets password')
def step_impl(context):
    pwd = RandomTestDataGenerator.get_random_password(13)
    print(pwd)
