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

class TestBookSearch():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_bookSearch(self):
    # Test name: Book Search
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://library.nitrkl.ac.in/")
    # 2 | setWindowSize | 1552x880 | 
    self.driver.set_window_size(1552, 880)
    # 3 | click | id=masthead_search | 
    self.driver.find_element(By.ID, "masthead_search").click()
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | select | id=masthead_search | label=ISBN
    dropdown = self.driver.find_element(By.ID, "masthead_search")
    dropdown.find_element(By.XPATH, "//option[. = 'ISBN']").click()
    # 6 | click | id=transl1 | 
    self.driver.find_element(By.ID, "transl1").click()
    # 7 | type | id=transl1 | 9789388028028
    self.driver.find_element(By.ID, "transl1").send_keys("9789388028028")
    # 8 | click | id=searchsubmit | 
    self.vars["window_handles"] = self.driver.window_handles
    # 9 | storeWindowHandle | root | 
    self.driver.find_element(By.ID, "searchsubmit").click()
    # 10 | selectWindow | handle=${win7176} | 
    self.vars["win7176"] = self.wait_for_window(2000)
    # 11 | assertText | xpath=//span[@property="author"]/span | R Mall
    self.vars["root"] = self.driver.current_window_handle
    # 12 | close |  | 
    self.driver.switch_to.window(self.vars["win7176"])
    assert self.driver.find_element(By.XPATH, "//span[@property=\"author\"]/span").text == "R Mall"
    self.driver.close()
  
