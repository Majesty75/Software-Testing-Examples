from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import time

url = 'https://www.amazon.in/'

def getBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('detach', True)
    return webdriver.Chrome(options=options)

def search():
    try:
        browser = getBrowser()
        browser.get(url)

        ActionChains(browser)\
            .click(browser.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox'))\
            .send_keys('macbook pro')\
            .click(browser.find_element(By.ID, 'nav-search-submit-button'))\
            .perform()
        
        result = wait(browser, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//span[contains(text(),"macbook pro")]'))
        )

        assert result != None and result != False, 'Search failed'

        print('Test Passed')
    except Exception as err:
        print('Test Failed')
        raise
    finally:
        ActionBuilder(browser).clear_actions()
        browser.quit()

if __name__ == '__main__':
    search()
