import behave
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I launch Chrome browser')
def step_impl(context):
    PATH = "//Users/paula/Desktop/selenium/selenium/chromedriver"
    context.driver = webdriver.Chrome(PATH)


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


@then('The user will see the profile page "{web}"')
def step_impl(context, web):
    test = True
    print("******")
    print(context.driver.current_url)
    if context.driver.current_url != web:
        test = False
    assert test is True

@then('will see the profile picture')
def step_impl(context):
    test = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/span/a/div").is_displayed()
    assert test is True
    context.driver.quit()
    