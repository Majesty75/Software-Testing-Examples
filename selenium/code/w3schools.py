from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder

url = 'https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert'

def getBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('detach', True)
    return webdriver.Chrome(options=options)

def checkAlert():
    try:
        browser = getBrowser()
        browser.get(url)

        iframe = browser.find_element(By.ID, 'iframeResult')

        browser.switch_to.frame(iframe)

        button = browser.find_element(By.CSS_SELECTOR, 'button')
        
        button.click()
        
        alert = browser.switch_to.alert

        assert alert.text == 'Hello! I am an alert box!', 'Wrong alert'

        alert.accept()

        browser.switch_to.default_content()

        print('Test Passed')
    except Exception as err:
        print('Test Failed')
        raise
    finally:
        browser.quit()

if __name__ == '__main__':
    checkAlert()
    