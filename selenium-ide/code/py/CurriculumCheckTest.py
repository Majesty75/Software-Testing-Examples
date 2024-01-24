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

class TestCurriculumCheck():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_curriculumCheck(self):
    # Test name: Curriculum Check
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.nitrkl.ac.in/")
    # 2 | setWindowSize | 1552x880 | 
    self.driver.set_window_size(1552, 880)
    # 3 | click | linkText=Academics | 
    self.driver.find_element(By.LINK_TEXT, "Academics").click()
    # 4 | click | id=submenu-engineering | 
    self.driver.find_element(By.ID, "submenu-engineering").click()
    # 5 | runScript | window.scrollTo(0,696) | 
    self.driver.execute_script("window.scrollTo(0,696)")
    # 6 | click | css=.item:nth-child(5) h5 | 
    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(5) h5").click()
    # 7 | click | css=#tmenu-academic .submenu-indicator-chevron | 
    self.driver.find_element(By.CSS_SELECTOR, "#tmenu-academic .submenu-indicator-chevron").click()
    # 8 | click | id=submenu-curiculum | 
    self.driver.find_element(By.ID, "submenu-curiculum").click()
    # 9 | click | css=tr:nth-child(4) a | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) a").click()
    # 10 | click | css=#flush-heading-2 > .accordion-button | 
    self.driver.find_element(By.CSS_SELECTOR, "#flush-heading-2 > .accordion-button").click()
    # 11 | click | css=#flush-2 tr:nth-child(3) a | 
    self.driver.find_element(By.CSS_SELECTOR, "#flush-2 tr:nth-child(3) a").click()
    # 12 | close |  | 
    self.driver.close()
  
