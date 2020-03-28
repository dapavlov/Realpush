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

url = 'http://realpush.pn.dsp.wtf/custom/1.0/REALPUSH2' \
      '/dc488a97bb650167ba3a5860c57c911f5d2142cce9277f4bf61a8a60eb49c902'
params = {
    "ua": user_agent,
    "user_id": "",
    "lang": "en",
    "ip": random_ip,
    "sd": int(time()),
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
    # print("\n")
    print(response_data)
    print("Status Code:", res.getcode())
    if res.getcode() in response_codes:
        print(response_codes[res.getcode()])
