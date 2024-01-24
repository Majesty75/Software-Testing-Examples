# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestEmailReading():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_emailReading(self):
    # Test name: Email Reading
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://mail.nitrkl.ac.in/")
    # 2 | setWindowSize | 845x864 | 
    self.driver.set_window_size(845, 864)
    # 3 | click | css=#zlif__CLV-main__-2408__su > span:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, "#zlif__CLV-main__-2408__su > span:nth-child(1)").click()
    # 4 | selectFrame | index=1 | 
    self.driver.switch_to.frame(1)
    # 5 | click | linkText=https://app.inspiredstudy.com/register | 
    self.driver.find_element(By.LINK_TEXT, "https://app.inspiredstudy.com/register").click()
    # 6 | close |  | 
    self.driver.close()
  
