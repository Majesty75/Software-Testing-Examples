from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions

url = "https://smallpdf.com/pdf-to-word"

def getBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)

def convertToPDF():
    try:
        browser = getBrowser()
        browser.get(url)

        # select file
        browser.find_element(By.ID, '__picker-input').send_keys('C:\\Users\\Yash\\Downloads\\Assignment 4 Cause Effect Graphing.docx')

        # wait for conversion
        wait(browser, 30).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.kHOHNI .r5zwp6-3:nth-child(2)'))
        )

        # click convert button
        browser.find_element(By.CSS_SELECTOR, '.kHOHNI .r5zwp6-3:nth-child(2)')

        print('Test Passed')

    except Exception as err:
        print('Test Failed')
        print(err)
    finally:
        browser.quit()

if __name__ == "__main__":
    convertToPDF()
