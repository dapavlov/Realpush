import urllib.parse
import urllib.request

from termcolor import colored

from db_actions import *
from http_responses import response_codes
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, random_token = db_connection()

url = 'http://xml.admozartppc.com/search'
params = {
    "feed": "229502",
    "auth": "pvBZfu",
    "subid": random_sid,
    "ua": user_agent,
    "user_ip": random_ip,
    "query": "",
    "url": "",
    "count": "1",
    "image_size":  "150x150",
    "image_required": "1",
    "icon_size": "50x50",
    "icon_required": "1"
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