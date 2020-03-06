import time


def test_domain_switch(browser):
    link = "https://realpush.net"
    # link = "https://pushlead.net"
    browser.get(link)

    button = browser.find_element_by_link_text("Sign In")
    button.click()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)
    input1 = browser.find_element_by_id("session_email")
    input1.send_keys("dpavlov@adwirk.com")
    input2 = browser.find_element_by_id("session_password")
    input2.send_keys("Qe2Gjqo")
    option = browser.find_element_by_css_selector("[type='submit']").click()

    button = browser.find_element_by_link_text("Domains")
    button.click()
    time.sleep(2)

    option1 = browser.find_element_by_css_selector("[href='#nav-dist-domains']").click()
    time.sleep(2)
    option2 = browser.find_element_by_css_selector("[href='#nav-land-domains']").click()
    time.sleep(2)
    option3 = browser.find_element_by_css_selector("[href='#nav-js-domains']").click()
    time.sleep(2)
    option4 = browser.find_element_by_css_selector("[href='#nav-js-sublimit']").click()
    time.sleep(2)
    # option5 = browser.find_element_by_class_name("custom-switch-btn").click()
