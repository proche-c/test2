import behave
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('I launch Chrome browser')
def step_impl(context):
    context.serv_obj = Service("//Users/paula/Desktop/selenium/selenium/chromedriver")
    PATH = "//Users/paula/Desktop/selenium/selenium/chromedriver"
    context.driver = webdriver.Chrome(service=context.serv_obj)


@when('I open the intra.42 homepage')
def step_impl(context):
    context.driver.get("https://profile.intra.42.fr")


@when('I enter username "{user}" and I pass a valid password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.ID, "user_login").send_keys(user)
    context.driver.find_element(By.ID, "user_password").send_keys(pwd)


@when('click on login button')
def step_impl(context):
    context.driver.find_element(By.NAME, "commit").click()

@when('I type in the nickname of a student: "{username}" on the search button')
def step_impl(context, username):
    context.driver.find_element(By.NAME, "query").send_keys(username)

@when('I press enter')
def step_impl(context):
    context.driver.find_element(By.NAME, "query").send_keys(Keys.ENTER)

@then('I will see the profile picture: "{picture}"')
def step_impl(context, picture):
    try:
        test = context.driver.find_element(By.XPATH, picture).is_displayed()
    except:
        context.driver.quit()
        assert False, "Test Failed"
    if test is True:
        assert True, "Test Passed"
        context.driver.quit()


