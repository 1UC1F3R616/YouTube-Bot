"""
# Note:
- No Proxy is used in this file (Completly purged, reasons told on Attached YouTube Video)
- Using Same IP can get your ip banned or restrictions will be applied from YouTube
- To know how you can setup proxy, check-out pro_youtube_bot.py

# Configuration settings has to be configured accordingly
# It's thoroughly tested by 1UC1F3R616 on 21-10-2020
"""

import os
import threading
from time import sleep
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType


# Logging
filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bot.log')
logging.basicConfig(filename=filename, filemode='w', format='%(levelname)s - %(asctime)s - %(message)s')
logger=logging.getLogger()
logger.setLevel(logging.INFO)

# Configuration
CHROME_BINARY_PATH = 'chromedriver.exe' # If in the same directory as of this script
INSTANCES = 1 # Views that you will be getting | This is the number of Threads keep this in mind
INSTANCE_MULTIPLIER = 2 # Views = INSTANCE_MULTIPLIER * INSTANCES
URL = 'https://www.youtube.com/watch?v=AhYOtVVSKfo'
VIDEO_LENGTH = 80 # In Seconds


def view_increase(url=None):
    """
    :args:
    url: URL of the YouTube video
    """
    if not (url):
        print('[!] URL is missing')
        return

    chrome_options = Options()

    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')   
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--mute-audio")

    driver = webdriver.Chrome(executable_path=os.path.abspath(CHROME_BINARY_PATH), chrome_options=chrome_options)
    actions = ActionChains(driver) # To start the video by sending shortcut-key 'k'

    driver.get(url)
    driver.implicitly_wait(2)
    actions.send_keys('k')
    sleep(1)
    actions.perform()
    sleep(VIDEO_LENGTH)
    driver.close()

count = 1
for iteration in range(INSTANCE_MULTIPLIER):
    for instance in range(INSTANCES):
        try:
            threading.Thread(target=view_increase, args=(URL,)).start()
            print('[-] Success for instance {}'.format( count ))
            logger.info('[-] Success for instance {}'.format( count ))
        except Exception as e:
            print('[!] Instance {} has failed'.format( count ))
            logger.info('[!] Instance {} has failed'.format( count ))
            logger.error(str(e))
        
        count += 1  
        sleep(1)
    
    if threading.active_count() > 2: # 1 is main thread
        sleep(VIDEO_LENGTH)
    
