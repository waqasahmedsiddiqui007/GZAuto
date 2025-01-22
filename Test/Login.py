from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from elements_manager import *
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.mark.sanity
def test_logingz():
  driver = webdriver.Chrome()
  driver.get('https://dev-greenzone.azurewebsites.net/account/login/')
  # to click on the element(The Username field i...) found
  driver.find_element(By.XPATH, '//*[@id="UserName"]').send_keys('abid.farooqi@cloud.thinkdigitally.com')
  # press Enter key
  driver.switch_to.active_element.send_keys(Keys.ENTER)
  # to type content in input field
  driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys('123456789')
  # to click on the element(Login) found
  driver.find_element(By.XPATH,'//*[@id="btnSubmit"]').click()
  sleep(7)
  assert driver.find_element(By.XPATH, '//*[contains(text(),"Welcome!")]').text == "Welcome!"
  driver.close()
