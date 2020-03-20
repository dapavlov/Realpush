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

url = 'http://xml.80xmedia.com/search'
params = {
    "feed": "222483",
    "auth": "msPFMF",
    "subid": random_sid,
    "query": "best+deals",
    "user_ip": random_ip,
    "ua": user_agent,
    "url": ""
}
query_string = urllib.parse.urlencode(params)
full_url = url + "?" + query_string
print(full_url)
req = urllib.request.Request(full_url)
try:
    res = urllib.request.urlopen(req, timeout=10)
    respData = res.read().decode('utf-8')
    print(respData)
    print("Status Code:", res.getcode())
    if res.getcode() in response_codes:
        print(response_codes[res.getcode()])
except Exception as exc:
    print(exc)
