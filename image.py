import os
import sys
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# File Name
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/screen.png")

# set driver and url
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
url = 'https://www.google.com/search?q=%E8%AA%BF%E5%B8%83+%E5%A4%A9%E6%B0%97&rlz=1C5CHFA_enJP928JP928&oq=%E8%AA%BF%E5%B8%83%E3%80%80%E5%A4%A9%E6%B0%97&aqs=chrome..69i57j0i512l9.4015j1j7&sourceid=chrome&ie=UTF-8'
driver.get(url)

# get width and height of the page
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")

# set window size
driver.set_window_size(w,h)

# Get Screen Shot
driver.save_screenshot(FILENAME)

# Close Web Browser
driver.quit()
