
from selenium import webdriver
from behave import *

PATH = "//Users/paula/Desktop/selenium/selenium/chromedriver"

@given ('I write "{web}" on the browser')
def step_impl(context):
    context.driver = webdriver.Chrome(PATH)
    context.driver.get("web")

@when ('I look up the title')
def step_impl(context):
    title_w = context.driver.title

@then ('I get {title}')
def step_impl(context, title):
    test = True
    if context.driver.title != title:
        test = False
    context.driver.quit()
    assert test is True 