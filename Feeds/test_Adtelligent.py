import urllib.parse
import urllib.request

from termcolor import colored

from db_actions import *
from global_param import user_agent
from http_responses import response_codes
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, random_token = db_connection()

url = 'https://501455.xmlfeed.adtelligent.com/'
params = {
    "lang": "en",
    "uip": random_ip,
    "ua": user_agent,
    "subid": random_sid,
    "uid": ""
}
query_string = urllib.parse.urlencode(params)
url = url + "?" + query_string
try:
    res = urllib.request.urlopen(url)
except Exception as exc:
    print(exc)
else:
    response_data = res.read().decode('utf-8', 'replace')
    print(response_data)
    print(url)
    print("Status Code:", res.getcode())
    if res.getcode() in response_codes:
        print(response_codes[res.getcode()])