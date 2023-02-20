#!/bin/python
import requests
import datetime

# 1.
# url = input("URL: ")
url = "http://python.org/"
# url = "https://www.youtube.com"


# 2.
# Πραγματοποιηση αιτηματος 
with requests.get(url) as response:  # το αντικείμενο response
    # 3.
    headers = response.headers
    # more(headers)
    print(f'Headers: {headers}')

    # 4.
    print(f'\nSoftware of the server: {headers["Server"]}\n')

    if "set-cookie" in headers.keys():
        # cookies_keys = response.cookies.keys
        cookies = response.cookies
        for cookie in cookies:
            print(f"\nThe site uses cookie.\nName: {cookie.name}\nValue: {cookie.value}\nExpiration Date: {datetime.datetime.fromtimestamp(float(cookie.expires)) if cookie.expires is not None else 'Does Not Expire'}")        
    else:
        print('\nThe site does not use cookies')




