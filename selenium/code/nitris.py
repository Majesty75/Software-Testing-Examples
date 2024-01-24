from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
import keyring

url = "https://eapplication.nitrkl.ac.in/nitris/Login.aspx"

def getBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)

def login(browser, username, password):
    try:
        # enter username
        browser.find_element(By.ID, "txtUserName").send_keys(username)

        #enter password
        browser.find_element(By.ID, "txtPassword").send_keys(password)

        # click login
        browser.find_element(By.ID, "btnLogin").click()

        #wait for login to complete
        wait(browser, 30).until(
            expected_conditions.title_contains("NITRIS")
        )
    except:
        return False

    return True

def downloadAttachment(username, password):
    try:
        browser = getBrowser()
        browser.get(url)

        # if not already login
        if url == browser.current_url:
            if not login(browser, username, password):
                return False

        # click on notification icon
        browser.find_element(By.CSS_SELECTOR, '.mdi-comment-processing').click()

        # wait for notifications panel
        wait(browser, 30).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.message-item:nth-child(2) > .mail-contnet'))
        )

        # click notification
        browser.find_element(By.CSS_SELECTOR, '.message-item:nth-child(2) > .mail-contnet').click()

        # wait for notification loading
        wait(browser, 30).until(
            expected_conditions.element_to_be_clickable((By.ID, 'ContentPlaceHolder2_hypPreview'))
        )

        # click attachment
        browser.find_element(By.ID, 'ContentPlaceHolder2_hypPreview').click()

        print('Test Passed')
    except Exception as err:
        print('Test Failed')
        print(err)
    finally:
        browser.quit()

if __name__ == "__main__":
    username = "223CS3149"
    password = keyring.get_password("nitris", username)
    downloadAttachment(username, password)
