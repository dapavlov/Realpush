import datetime
import urllib.parse
import urllib.request

from termcolor import colored

from db_actions import *
from http_responses import response_codes
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, random_token, random_ua = db_connection()

UID = random.randrange(1, 1000)

url = 'http://pushism.com/b'
params = {
    "feedId": "453",
    "ip": random_ip,
    "ua": random_ua,
    "source": UID,
    "subscriber_id": random_sid,
    "lang": "en",
    "user_age": datetime.datetime.today().strftime('%Y-%m-%d'),
    "user_age_group": "0"

}
query_string = urllib.parse.urlencode(params)
url = url + "?" + query_string
print(url)
try:
    res = urllib.request.urlopen(url)
except Exception as exc:
    print(exc)
else:
    response_data = res.read().decode('utf-8', 'replace')
    print(response_data)
    print("Status Code:", res.getcode())
    if res.getcode() in response_codes:
        print(response_codes[res.getcode()])