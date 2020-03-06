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

tid_list = ['500', '592', '593']
random_tid = random.choice(tid_list)

url = 'http://xml.ibizads.com/feed/'
params = {
    "type": "push",
    "tid": random_tid,
    "ip": random_ip,
    "ua": user_agent,
    "subid": random_sid,
    "format": "json",
    "sdate": datetime.datetime.today().strftime('%Y-%m-%d')
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