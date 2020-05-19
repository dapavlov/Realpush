import time
import urllib.parse
import urllib.request
from urllib.error import HTTPError, URLError

from http_response_status import response_codes


def fetch(url, params):
    query_string = urllib.parse.urlencode(params)
    full_url = url + "?" + query_string
    print(full_url)
    req = urllib.request.Request(full_url)
    max_attempts = 5
    delay_before_retry = 3
    for _ in range(max_attempts):
        try:
            res = urllib.request.urlopen(req)
        # except Exception as exc:
        #     print(exc)
        except HTTPError as e:
            print('HTTP Error code: ', e.code)
            if e.code == 403 or e.code == 404:
                time.sleep(delay_before_retry)
                continue
            raise
        except URLError as e:
            print('URL Error: ', e.reason)
            raise
        else:
            response_data = res.read().decode('utf-8', 'replace')
            if res.getcode() == 200:
                print(response_data)
                print("Status Code:", res.getcode())
                print(response_codes[res.getcode()])
                break
            if res.getcode() == 204:
                print("Status Code:", res.getcode())
                print(response_codes[res.getcode()])
                time.sleep(delay_before_retry)
                continue
