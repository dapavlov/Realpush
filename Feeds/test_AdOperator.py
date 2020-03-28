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

url = 'http://in.eu.adopexchange.com/rtb/search/push'
params = {
    "format": "xml",
    "feedId": "e958",
    "ip": random_ip,
    "suId": random_sid,
    "ua": user_agent,
    "domain": "www.realpush.net"
}
query_string = urllib.parse.urlencode(params)
full_url = url + "?" + query_string
print(full_url)
req = urllib.request.Request(full_url)
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
