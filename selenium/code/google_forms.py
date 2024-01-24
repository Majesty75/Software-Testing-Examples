from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import time

url = 'https://docs.google.com/forms/d/e/1FAIpQLSeI8_vYyaJgM7SJM4Y9AWfLq-tglWZh6yt7bEXEOJr_L-hV1A/viewform?formkey=dGx0b1ZrTnoyZDgtYXItMWVBdVlQQWc6MQ'

def getBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('detach', True)
    return webdriver.Chrome(options=options)

def fillForm():
    try:
        browser = getBrowser()
        browser.get(url)

        ActionChains(browser)\
            .move_to_element(browser.find_element(By.CSS_SELECTOR, '.whsOnd'))\
            .send_keys('This is selenium testing')\
            .move_to_element(browser.find_element(By.CSS_SELECTOR, '.KHxj8b'))\
            .send_keys('By selenium testing we can test website response to user commands and verify if it is working properly. This test is conducted by selenium IDE.')\
            .click(browser.find_element(By.ID, 'i16'))\
            .click(browser.find_element(By.ID, 'i27'))\
            .click(browser.find_element(By.CSS_SELECTOR, '.ry3kXd .KKjvXb'))\
            .perform()
        
        time.sleep(1)

        ActionChains(browser)\
            .click(browser.find_element(By.CSS_SELECTOR, '.OA0qNb .KKjvXb .vRMGwf'))\
            .click(browser.find_element(By.XPATH, '//div[@class="N9Qcwe"]//div[@data-value="4"]'))\
            .click(browser.find_element(By.XPATH, '//form[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/div/div[2]/span/div[3]/div/div/div[3]/div'))\
            .click(browser.find_element(By.XPATH, '//form[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/div/div[4]/span/div[4]/div/div/div[3]/div'))\
            .click(browser.find_element(By.XPATH, '//form[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/div/div[6]/span/div[4]/div/div/div[3]/div'))\
            .click(browser.find_element(By.XPATH, '//form[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/div/div[8]/span/div[3]/div/div/div[3]/div'))\
            .click(browser.find_element(By.CSS_SELECTOR, '.Y5sE8d > .l4V7wb'))\
            .perform()
        
        submission = wait(browser, 30).until(
            expected_conditions.visibility_of_element_located((By.LINK_TEXT, 'Submit another response'))
        )

        assert submission != None and submission != False, 'Form submission failed'

        print('Test Passed')
    except Exception as err:
        print('Test Failed')
        raise
    finally:
        ActionBuilder(browser).clear_actions()
        browser.quit()

if __name__ == '__main__':
    fillForm()
