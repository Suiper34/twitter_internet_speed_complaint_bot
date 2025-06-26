import os
from time import sleep, time

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

options = ChromeOptions.add_experimental_option('detach', True)
complaint_bot_driver = webdriver.Chrome(options=options)


try:
    # internet speed tester
    complaint_bot_driver.get('https://www.speedtest.net/')

    # start test
    start_test = WebDriverWait(complaint_bot_driver, 30).until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[aria-label="start speed test - connection type multi"]')))
    start_test.click()

    # download value in mbps
    download_mbps = WebDriverWait(complaint_bot_driver, 200).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'span.result-data-value.download-speed'))
    )
    download_speed = download_mbps.text
    if not download_speed:
        raise ValueError('Download speed not found or empty.')

    # upload value in mbps
    upload_mbps = WebDriverWait(complaint_bot_driver, 5).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'span.result-data-value.upload-speed')
        )
    )
    upload_speed = upload_mbps.text
    if not upload_speed:
        raise ValueError('Upload speed not found or empty.')

except Exception as e:
    print('Speed Test Failed:', e)
    # None to prevents UnboundLocalError
    download_speed = None
    upload_speed = None


sleep(10)
complaint_bot_driver.get('https://x.com/i/flow/login')

# execute if login ui is present
try:
    # username
    username = WebDriverWait(complaint_bot_driver, 15).until(
        expected_conditions.presence_of_element_located((By.NAME, 'text')))
    username.send_keys(os.environ.get('USERNAME'), Keys.ENTER)
    sleep(2)

except Exception as e:
    print('Already logged in or username invalid...Exception:', e)

else:
    try:
        # password
        password = WebDriverWait(complaint_bot_driver, 7).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        password.send_keys(os.environ.get('PASSWORD'), Keys.ENTER)
    except Exception as e:
        print('Incorrect password...Exception:', e)


try:
    # tweet and post
    tweet_button = WebDriverWait(complaint_bot_driver, 10).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="Post"]')))
    tweet_button.click()

    sleep(2)
    tweet_area = complaint_bot_driver.find_element(
        By.CSS_SELECTOR, 'div[aria-label="Post text"] .public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
    tweet_area.click()
    tweet_area.send_keys('Slow internet @telecel')

    sleep(2)
    post_tweet = complaint_bot_driver.find_element(
        By.CSS_SELECTOR, 'button[data-testid="tweetButton"]')
    post_tweet.click()

except Exception as e:
    print('Tweet/post failed:', e)
