import urllib.parse
import urllib.request

from termcolor import colored

from db_actions import *
from global_param import *
from http_responses import response_codes
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_id, random_token = db_connection()

pid_dict = ['258', '429']
secret_dict = ['f05931430fe362c6f7ebe96a8cb87ae7', 'f56932eeff6a0906cbfebcf723d7bfc4']
result_dict = dict(zip(pid_dict, secret_dict))
random_key = random.choice(list(result_dict.keys()))
random_value = result_dict[random_key]

url = 'http://eu1.kadam.net/pushcpcfeed'
params = {
    "sid": random_key,
    "skey": random_value,
    "ip": random_ip,
    "ua": user_agent_mobile,
    "pid": "846826",
    "uid": random_id,
    "limit": "1",
    "lang": "en"
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