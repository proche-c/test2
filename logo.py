from operator import truediv
import behave
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('we launch chrome browser')
def step_impl(context):
    PATH = "//Users/paula/Desktop/selenium/selenium/chromedriver"
    context.driver = webdriver.Chrome(PATH)


@when('we open intra.42.fr homepage')
def step_impl(context):
    context.driver.get("https://profile.intra.42.fr")


@then('verify that the logo is present onthe page')
def step_impl(context):
    test = context.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/img").is_displayed()
    assert test is True

@then('close browser')
def step_impl(context):
    context.driver.quit()