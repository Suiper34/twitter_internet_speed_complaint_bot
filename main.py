import os

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

options = ChromeOptions.add_experimental_option('detach', True)
complaint_bot_driver = webdriver.Chrome(options=options)

complaint_bot_driver.get('https://x.com/i/flow/login')
username = WebDriverWait(complaint_bot_driver, 15).until(
    expected_conditions.presence_of_element_located((By.NAME, 'text')))
username.send_keys(os.environ.get('USERNAME'), Keys.ENTER)
