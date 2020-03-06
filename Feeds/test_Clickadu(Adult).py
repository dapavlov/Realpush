import time
import urllib.parse
import urllib.request

from termcolor import colored

from db_actions import *
from http_responses import response_codes
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, random_token = db_connection()

url = 'http://realpush.pn.dsp.wtf/custom/1.0/REALPUSH1' \
      '/4b7498022dd6519e6e3d3a001c04b003f9d5c4bcb8ca42b796f49eaa2b9ce339'
params = {
    "ua": user_agent,
    "user_id": "",
    random_ip: "en-US",
    "ip": random_ip,
    "sd": int(time.time()),
    "var": random_sid
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
