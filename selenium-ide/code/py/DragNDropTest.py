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

class TestDragNDrop():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_dragNDrop(self):
    # Test name: Drag N Drop
    # Step # | name | target | value
    # 1 | open | /cdk/drag-drop/examples | 
    self.driver.get("https://material.angular.io/cdk/drag-drop/examples")
    # 2 | storeXpathCount | xpath=//div[@id="cdk-drop-list-0"]//div[contains(., "Pick up groceries")] | i
    self.vars["i"] = len(self.driver.find_elements(By.XPATH, "//div[@id=\"cdk-drop-list-0\"]//div[contains(., \"Pick up groceries\")]"))
    # 3 | echo | ${i} | 
    print("{}".format(self.vars["i"]))
    # 4 | dragAndDropToObject | xpath=//div[@id="cdk-drop-list-0"]//div[contains(., "Pick up groceries")] | id=cdk-drop-list-1
    dragged = self.driver.find_element(By.XPATH, "//div[@id=\"cdk-drop-list-0\"]//div[contains(., \"Pick up groceries\")]")
    dropped = self.driver.find_element(By.ID, "cdk-drop-list-1")
    actions = ActionChains(self.driver)
    actions.drag_and_drop(dragged, dropped).perform()
    # 5 | close |  | 
    self.driver.close()
  
