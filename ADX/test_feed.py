from global_param import user_agent
from ipv4_generator import *
from termcolor import colored
from db_actions import *
from http_responses import response_codes
import urllib.parse
import urllib.request

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, random_token = db_connection()

url = 'http://157.230.112.179:4000/api/'
params = {
    "auth_token": "thisistoken",
    "vsn": "1",
    "ip": random_ip,
    "user_agent": user_agent,
    "sub_id": random_sid
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
