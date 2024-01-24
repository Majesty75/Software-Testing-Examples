from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder

url = "https://www.nitrkl.ac.in/"

def getBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=options)

def getCourseDetail():
    try:
        browser = getBrowser()
        browser.get(url)

        # mouse over on academics
        ActionChains(browser)\
            .move_to_element(browser.find_element(By.LINK_TEXT, 'Academics'))\
            .click(browser.find_element(By.ID, 'submenu-engineering'))\
            .perform()
        
        # get cse deptartment link
        cse = browser.find_element(By.CSS_SELECTOR, '.department .item:nth-child(5) a')
        
        # scroll to cse 
        ActionChains(browser)\
            .scroll_by_amount(0, int(cse.rect['y']))\
            .perform()
        
        # wait for cse then click
        cse.click()

        # click curriculum & syllabus
        ActionChains(browser)\
            .move_to_element(browser.find_element(By.CSS_SELECTOR, '#tmenu-academic .submenu-indicator-chevron'))\
            .click(browser.find_element(By.ID, 'submenu-curiculum'))\
            .perform()

        # click software engineering
        ActionChains(browser)\
            .scroll_by_amount(0, 400)\
            .pause(0.5)\
            .click(browser.find_element(By.CSS_SELECTOR, 'tr:nth-child(4) a'))\
            .perform()

        # click 2nd sem syllabus
        ActionChains(browser)\
            .scroll_by_amount(0, 700)\
            .pause(0.5)\
            .click(browser.find_element(By.ID, 'flush-heading-2'))\
            .pause(0.5)\
            .click(browser.find_element(By.CSS_SELECTOR, '#flush-2 tbody tr:nth-child(3) a'))\
            .perform()

        assert browser.find_element(By.CSS_SELECTOR, '.item-left .row:nth-child(2) .col-md-12 > p:nth-child(1)').text == 'Subject {L-T-P / C} : CS6404 : Software Testing { 3-0-0 / 3}', 'Invalid course name'

        print('Test Passed')
    except Exception as err:
        print('Test Failed')
        raise
    finally:
        ActionBuilder(browser).clear_actions()
        browser.quit()

if __name__ == "__main__":
    getCourseDetail()
