from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
import keyring

url = "https://login.nitrkl.ac.in/PortalMain"

def getBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)

def login(username, password):
    try:
        browser = getBrowser()
        browser.get(url)

        # wait for login form
        wait(browser, 30).until(
            expected_conditions.element_to_be_clickable((By.ID, 'LoginUserPassword_auth_username'))
        )

        # enter username
        browser.find_element(By.ID, "LoginUserPassword_auth_username").send_keys(username)

        #enter password
        browser.find_element(By.ID, "LoginUserPassword_auth_password").send_keys(password)

        # click login
        browser.find_element(By.ID, "UserCheck_Login_Button_span").click()

        # wait for login to complete
        wait(browser, 30).until(
            expected_conditions.visibility_of_element_located((By.ID, 'UserCheck_Logoff_Button_span'))
        )

        print('Test Passed')
    except Exception as err:
        print(err)
        print('Test Failed')
    finally:
        browser.quit()

if __name__ == "__main__":
    username = "223CS3149"
    password = keyring.get_password("nitrnet", username)
    login(username, password)
