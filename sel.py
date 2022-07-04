from selenium import webdriver
from behave import *

PATH = "//Users/paula/Desktop/selenium/selenium/chromedriver"
driver = webdriver.Chrome(PATH)
@given ('I want to go to a website')
def step_impl(context):
    pass

@when ('I write the website address on the browser')
def step_impl(context):
    driver.get("https://profile.intra.42.fr")
    print(dir(driver))

@then ('the website loads')
def step_impl(context):
    assert context.failed is False