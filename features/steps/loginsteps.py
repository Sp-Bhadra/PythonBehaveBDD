from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given('I launch chrome browser')
def launchBrowser(context):
    service_obj = Service("C:\\File D\\chromedriver.exe")
    context.driver = webdriver.Chrome(service=service_obj)


@when('I open orangeHRM homepage')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")


@when('I enter username "{user}" and password "{password}"')
def enterDetail(context, user, password):
    wait = WebDriverWait(context.driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//img[@alt='company-branding']")))
    context.driver.find_element(By.NAME, "username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(password)


@when('I clicked on submit button')
def submit(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('then user must successfully logged into dashboard page')
def dashboard(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".oxd-text.oxd-text--h6")))
    Dashboard = context.driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--h6").is_displayed()
    assert Dashboard is True



