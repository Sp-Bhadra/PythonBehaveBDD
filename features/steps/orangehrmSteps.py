
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given('launch chrome browser')
def launchBrowser(context):
    service_obj = Service("C:\\File D\\chromedriver.exe")
    context.driver = webdriver.Chrome(service=service_obj)

@when('open OrangeHRM homepage')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")


@then('verify logo present on orangeHRM homepage')
def verifyLogo(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//img[@alt='company-branding']")))
    status = context.driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
