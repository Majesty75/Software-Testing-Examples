from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder

url = 'https://internal.imd.gov.in/pages/city_weather_main_mausam.php'

def getBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('detach', True)
    return webdriver.Chrome(options=options)

def getWeather():
    try:
        browser = getBrowser()
        browser.get(url)

        ActionChains(browser)\
            .click(browser.find_element(By.NAME, 'id'))\
            .send_keys('42793rourkela')\
            .click(browser.find_element(By.CSS_SELECTOR, '#menu1 input[type="submit"]'))\
            .perform()
        
        # wait for grade card window to open
        wait(browser, 30).until(
            expected_conditions.number_of_windows_to_be(2)
        )

        # switch to new window
        browser.switch_to.window(browser.window_handles[-1])

        assert browser.find_element(By.CSS_SELECTOR, 'font[color="blue"]').text == 'Rourkela', 'Search failed'

        print('Test Passed')
    except Exception as err:
        print('Test Failed')
        raise
    finally:
        ActionBuilder(browser).clear_actions()
        browser.quit()

if __name__ == '__main__':
    getWeather()
    