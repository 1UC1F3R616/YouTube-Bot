"""
# Setting Up the Proxy:
- Current setup is fetching proxy from fastProxy file
    - You may pipe-in your own proxies or setup tor proxy on http protocol using pproxy and use that (Refer related video on YouTube)
- Uncomment chrome_options for proxy
- Comment the proxies just above url so to feed proxy
# Use youtube_bot.py if you are not understanding this code
    - it will be using ur ip (No Proxy Minimal Setup)
# Use proxy_youtube_bot.py for minimal proxy setup (Not included, maybe in future)
"""


import os
import threading
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

def view_increase(url=None, proxy=None):
    if not (url and proxy):
        print('[!] URL or PROXY is missing')
        return

    chrome_options = Options()

    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')   
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--mute-audio")
    #chrome_options.add_argument('--proxy-server={}'.format(proxy))

    driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver.exe'), chrome_options=chrome_options)
    actions = ActionChains(driver)


    driver.get(url)
    sleep(2)
    actions.send_keys('k')
    sleep(1)
    actions.perform()
    sleep(80)
    driver.close()

# Proxy Setup
import fastProxy as p
p.THREAD_COUNT = 56
p.REQUEST_TIMEOUT = 1
p.GENERATE_CSV = False
p.ALL_IPS = False
proxies = p.fetch_proxies()
proxies=range(5) # number of instances, this will switch to your own ip ie. No Proxy Mode
url = 'https://www.youtube.com/watch?v=AhYOtVVSKfo'
for proxy in proxies:
    try:
        proxy_feed = 'http://{}'.format(proxy)
        threading.Thread(target=view_increase, args=(url,proxy_feed)).start()
        print('[-] Success for {}'.format(proxy_feed))
    except Exception as e:
        print('[!] Chrome instance {} has failed'.format(proxy))
    sleep(1)
