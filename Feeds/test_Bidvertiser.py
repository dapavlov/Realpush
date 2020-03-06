import datetime
import urllib.parse
import urllib.request

from termcolor import colored

from db_actions import *
from http_responses import response_codes
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, random_token = db_connection()

url = 'http://2001237.bdv-w.bidvertiser.com/BidVertiser.dbm'
params = {
    "pid": "846826",
    "bid": "2001237",
    "Kterm": "general",
    "cip": random_ip,
    "maxcount": "1",
    "ownid": "",
    "bvref": "http://www.realpush.net",
    "xml": "1",
    "u_agnt": user_agent,
    "bvlang": "en",
    "subdate": datetime.datetime.today().strftime('%Y-%m-%d')
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