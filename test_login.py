import pickle
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "https://pushlead.net"


# link = "https://realpush.net"

def test_login(browser):
    browser.get(link)
    # time.sleep(5)
    # start_point = browser.find_element_by_link_text("Sign In").click()
    # input1 = browser.find_element_by_id("session_email").send_keys("admin@adwirk.com")
    # input2 = browser.find_element_by_id("session_password").send_keys("ChD@s8g(@42++26")
    # time.sleep(3)
    # finish_point = browser.find_element_by_xpath("//button[@type='submit']").click()
    #
    # pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))
    # browser.quit()
    # cookies = pickle.load(open("cookies.pkl", "rb"))
    # print(cookies)
    # browser.get(link)
    # for cookie in cookies:
    #     if 'expiry' in cookie:
    #         del cookie['expiry']
    #     browser.add_cookie(cookie)
    time.sleep(10)
    browser.refresh()
