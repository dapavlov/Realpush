# from bs4 import BeautifulSoup
# import requests
#
# url = "https://beta.10minutemail.com/"
#
# # Make a GET request to fetch the raw HTML content
# html_content = requests.get(url).text
#
# # Parse the html content
# soup = BeautifulSoup(html_content, "lxml")
# print(soup.prettify())

from websocket import create_connection

global file


class mailbox(object):
    """10 minute mailbox"""

    def __init__(self):
        super(mailbox, self).__init__()
        self.ws = create_connection("wss://dropmail.me/websocket")
        self.next = self.ws.recv
        self.close = self.ws.close
        self.email = self.next()[1:].split(":")[0]
        self.next()


def main():
    from json import loads
    from subprocess import call
    from datetime import datetime

    # call(["echo '{0}' | pbcopy".format(box.email)], shell=True)
    print(box.email)
    return box.email


if __name__ == '__main__':
    import os
    import sys

    # print("PID: {0}\nIf you can't quite, run 'kill {0}'\n".format(os.getpid()))
    try:
        box = mailbox()
        main()

    except KeyboardInterrupt:
        file.close()
        sys.exit(0)


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
