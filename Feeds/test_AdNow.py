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

url = 'http://dsp-proxy-new.prod.news-host.pw/a'
params = {
    "Id": "729093",
    "widget_id": "13234",
    "d_ip": random_ip,
    "d_page": "",
    "node": "adnow_realpush",
    "out": "xml",
    "sub_id": random_sid,
    "d_user_agent": user_agent
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