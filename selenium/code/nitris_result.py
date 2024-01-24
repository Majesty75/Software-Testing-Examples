from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
import keyring
import base64

url = "https://eapplication.nitrkl.ac.in/nitris/Login.aspx"
path = "c://users//yash//downloads//"

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



def downloadResult(username, password):
    try:
        browser = getBrowser()
        browser.get(url)

        # if not already login
        if url == browser.current_url:
            if not login(browser, username, password):
                return False
        
        # click on academic
        browser.find_element(By.ID, "Academic").click()

        # wait for examination button to be interactable
        wait(browser, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//header/nav[1]/div[2]/ul[1]/li[2]/div[1]/div[1]/div[1]/a[5]"))
        )

        # click on examination button
        browser.find_element(By.XPATH, "//header/nav[1]/div[2]/ul[1]/li[2]/div[1]/div[1]/div[1]/a[5]").click()

        # wait for new page to open by waiting for examination result element to be present in DOM
        wait(browser, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//body/form[@id='form1']/div[@id='main-wrapper']/aside[1]/div[1]/nav[1]/ul[1]/li[3]/a[1]"))
        )

        # click on examination result 
        browser.find_element(By.XPATH, "//body/form[@id='form1']/div[@id='main-wrapper']/aside[1]/div[1]/nav[1]/ul[1]/li[3]/a[1]").click()

        # wait for view grade to be interactable
        wait(browser, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//body/form[@id='form1']/div[@id='main-wrapper']/aside[1]/div[1]/nav[1]/ul[1]/li[3]/ul[1]/li[2]/a[1]"))
        )

        # click on grade card
        browser.find_element(By.XPATH, "//body/form[@id='form1']/div[@id='main-wrapper']/aside[1]/div[1]/nav[1]/ul[1]/li[3]/ul[1]/li[2]/a[1]").click()

        # wait for grade card window to open
        wait(browser, 30).until(
            expected_conditions.number_of_windows_to_be(2)
        )

        # switch to new window
        browser.switch_to.window(browser.window_handles[-1])

        params = {
            'outputFormat': 'pdf',
            'printBackground': True,
            'marginTop': 0,
            'marginBottom': 0,
            'marginLeft': 0,
            'marginRight': 0,
        }

        # execute chrome dev tools print command
        content = browser.execute_cdp_cmd('Page.printToPDF', params)

        # convert data to binary
        pdf_data = base64.b64decode(content['data'])

        # save data as pdf
        with(open(f'{path}{username}.pdf', 'wb')) as pdf_file:
            pdf_file.write(pdf_data)

        print(f'result downloaded to {path}{username}.pdf')
    except Exception as err:
        print(err)
    finally:
        browser.quit()

if __name__ == "__main__":
    username = "223CS3149"
    password = keyring.get_password("nitris", username)
    downloadResult(username, password)