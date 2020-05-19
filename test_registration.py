def test_registration(browser):
    # link = "https://realpush.net"
    link = "https://pushlead.net"
    # link = "http://pushlead.net/signup?ref=gJtWUoy"
    browser.get(link)

    button1 = browser.find_element_by_link_text("Sign Up").click()
    input1 = browser.find_element_by_id("registration_email")
    input1.send_keys("test@test.com")
    input2 = browser.find_element_by_id("registration_name")
    input2.send_keys("Name")
    input3 = browser.find_element_by_id("registration_password")
    input3.send_keys("adwirk2020")
    input4 = browser.find_element_by_id("registration_password_confirmation")
    input4.send_keys("adwirk2020")
    input5 = browser.find_element_by_css_selector("[value='publisher']").click()
    input6 = browser.find_element_by_id("registration_country")
    input6.send_keys("Russia")
    input7 = browser.find_element_by_id("select2-messengerSelector-container").click()
    input8 = browser.find_element_by_css_selector("[value='Skype']").click()
    input9 = browser.find_element_by_id("registration_messenger_login")
    input9.send_keys("qwerty12345")
    input10 = browser.find_element_by_id("registration_website")
    input10.send_keys("www.adwirk.com")

    option1 = browser.find_element_by_class_name("form__custom-checkbox").click()
    # button2 = browser.find_element_by_id("signupButton").click()
