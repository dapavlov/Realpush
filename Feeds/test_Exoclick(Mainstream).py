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

UID = random.randrange(100000, 999999)

url = 'http://rtb.exoclick.com/rtb.php'
params = {
    "idzone": "3329496",
    "fid": "4a9595316b187a77b935e741743fdd0a2abc7aea",
    "ip": random_ip,
    "type": "push_notification",
    "remote_addr": random_ip,
    "ua": user_agent,
    "sub": random_sid,
    "export": "json",
    "user_id": "",
    "id": UID
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
