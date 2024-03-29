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

class TestBasicOperations():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_basicOperations(self):
    # Test name: Basic Operations
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.google.com/")
    # 2 | setWindowSize | 1536x864 | 
    self.driver.set_window_size(1536, 864)
    # 3 | click | id=APjFqb | 
    self.driver.find_element(By.ID, "APjFqb").click()
    # 4 | type | id=APjFqb | calculator
    self.driver.find_element(By.ID, "APjFqb").send_keys("calculator")
    # 5 | click | name=btnK | 
    self.driver.find_element(By.NAME, "btnK").click()
    # 6 | click | css=.XH1CIc | 
    self.driver.find_element(By.CSS_SELECTOR, ".XH1CIc").click()
    # 7 | click | css=tr:nth-child(3) > td:nth-child(2) > .A2W7l > .XRsWPe | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(2) > .A2W7l > .XRsWPe").click()
    # 8 | click | css=tr:nth-child(3) > td:nth-child(1) > .A2W7l > .XRsWPe | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(1) > .A2W7l > .XRsWPe").click()
    # 9 | click | css=tr:nth-child(3) > td:nth-child(1) > .A2W7l > .XRsWPe | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(1) > .A2W7l > .XRsWPe").click()
    # 10 | doubleClick | css=tr:nth-child(3) > td:nth-child(1) > .A2W7l > .XRsWPe | 
    element = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(1) > .A2W7l > .XRsWPe")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 11 | click | css=tr:nth-child(4) > td:nth-child(1) > .A2W7l > .XRsWPe | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(1) > .A2W7l > .XRsWPe").click()
    # 12 | click | css=td:nth-child(4) .XRsWPe:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(4) .XRsWPe:nth-child(2)").click()
    # 13 | click | css=tr:nth-child(3) > td:nth-child(1) > .A2W7l > .XRsWPe | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(1) > .A2W7l > .XRsWPe").click()
    # 14 | click | css=tr:nth-child(4) > td:nth-child(1) > .A2W7l > .XRsWPe | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(1) > .A2W7l > .XRsWPe").click()
    # 15 | click | css=tr:nth-child(2) .mF5fo > .XRsWPe | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) .mF5fo > .XRsWPe").click()
    # 16 | click | css=tr:nth-child(2) > td:nth-child(1) > .A2W7l > .XRsWPe | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(1) > .A2W7l > .XRsWPe").click()
    # 17 | click | css=tr:nth-child(2) > td:nth-child(2) > .A2W7l > .XRsWPe | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(2) > .A2W7l > .XRsWPe").click()
    # 18 | click | css=tr:nth-child(2) > td:nth-child(3) > .A2W7l > .XRsWPe | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(3) > .A2W7l > .XRsWPe").click()
    # 19 | click | css=.UUhRt | 
    self.driver.find_element(By.CSS_SELECTOR, ".UUhRt").click()
    # 20 | close |  | 
    self.driver.close()
  
