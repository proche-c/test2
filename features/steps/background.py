import behave
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

@then('I click on the icon "{menu_element}"')
def step_impl(context, menu_element):
    context.driver.find_element(By.CLASS_NAME, menu_element).click()
    WebDriverWait(context.driver, 5)


@then('I will see that "{menu_page}"')
def step_impl(context, menu_page):
    test = True
    if menu_page != context.driver.current_url:
        test = False
    assert test is True


@then('the title will be "{title}"')
def step_impl(context, title):
    test = True
    print(context.driver.title)
    if title != context.driver.title:
        test = False
    assert test is True


