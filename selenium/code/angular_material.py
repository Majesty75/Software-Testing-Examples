from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import time
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

url = 'https://material.angular.io/cdk/drag-drop/examples'
# url = 'https://devhints.io/xpath'

def getBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('detach', True)
    return webdriver.Chrome(options=options)

def dragDrop():
    try:
        browser = getBrowser()
        browser.get(url)

        browser.find_element(By.CSS_SELECTOR, 'app-cookie-popup button').click()

        todo = browser.find_element(By.XPATH, '//div[@id="cdk-drop-list-0"]')
        tile = todo.find_element(By.XPATH, 'div[contains(text(), "Pick up groceries")]')
        done = browser.find_element(By.XPATH, '//div[@id="cdk-drop-list-1"]')

        scroll = ScrollOrigin.from_element(browser.find_element(By.CSS_SELECTOR, '.docs-component-sidenav-content'))

        ActionChains(browser, 30)\
            .scroll_from_origin(scroll ,0, 1200)\
            .pause(5)\
            .perform()\
        
        time.sleep(5)

        ActionChains(browser, 30)\
            .click_and_hold(tile)\
            .pause(5)\
            .release(done)\
            .pause(5)\
            .perform()
        
        done = browser.find_element(By.XPATH, '//div[@id="cdk-drop-list-1"]')

        movedTile = done.find_elements(By.XPATH, 'div[contains(text(), "Pick up groceries")]')

        assert len(movedTile), 'Drag & drop failed'

        print('Test Passed')
    except Exception as err:
        print('Test Failed')
        raise
    finally:
        ActionBuilder(browser).clear_actions()
        browser.quit()

if __name__ == '__main__':
    dragDrop()
    