import os
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from shutil import copy2

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Remote(
    command_executor='http://172.17.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME,
    options=options)

with open ('urls.txt', 'r') as file:
    content = file.readlines()
content = [x.rstrip('\n') for x in content]

for url in content:
    driver.get(url)
    time.sleep(3)
    screenshot_name = url.split('https://www.')[-1].split('.com')[0]
    driver.save_screenshot('{0}.png'.format(screenshot_name))

current_directory = os.getcwd()
files_in_directory = os.listdir(current_directory)

for item in files_in_directory:
    if item.endswith(".png"):
        copy2(item, '/usr/app/screenshots/')
        os.remove(os.path.join(current_directory, item))
