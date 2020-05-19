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