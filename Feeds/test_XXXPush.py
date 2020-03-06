import datetime
import urllib.parse
import urllib.request

from termcolor import colored

from db_actions import *
from http_responses import response_codes
from ipv4_generator import *

random_ip, ip_data = gen_ipv4_from_subnet()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, random_token = db_connection()

url = 'https://api.3xpush.com/'
params = {
    "key": "908a653e67827313993dc9a97f19dc856e3881bb",
    "action": "get_ads",
    "sid": "178",
    "ua": user_agent,
    "ip": random_ip,
    "subid": random_sid,
    "lang": random_lang,
    "date": datetime.datetime.today().strftime('%Y-%m-%d'),
    "uid": ""
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
