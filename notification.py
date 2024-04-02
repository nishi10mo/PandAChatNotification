# coding: utf-8

import time
import requests
from selenium import webdriver
import chromedriver_binary

# input your username of PandA
USERNAME = ""

# input your password of PandA
PASSWORD = ""

messages= ""

# input your token of Line Notify
token = ""
api = 'https://notify-api.line.me/api/notify'
headers = {'Authorization': f'Bearer {token}'}

try: 
    driver = webdriver.Chrome()
    driver.get("https://panda.ecs.kyoto-u.ac.jp/cas/login?service=https%3A%2F%2Fpanda.ecs.kyoto-u.ac.jp%2Fsakai-login-tool%2Fcontainer")
    driver.maximize_window()
    #try:
    username_input = driver.find_element_by_id("username")
    username_input.send_keys(USERNAME)
    time.sleep(1)

    password_input = driver.find_element_by_id("password")
    password_input.send_keys(PASSWORD)
    time.sleep(1)

    log_btn = driver.find_element_by_class_name("btn-submit")
    log_btn.click()
    time.sleep(1)

    menu_btn = driver.find_element_by_css_selector("#viewAllSites > i")
    menu_btn.click()
    time.sleep(1)

    sakura_btn = driver.find_element_by_css_selector("#otherSitesCategorWrap > div.moresites-right-col > div:nth-child(2) > ul > li:nth-child(1) > div > a")
    sakura_btn.click()
    time.sleep(1)

    chat_btn = driver.find_element_by_css_selector("#toolMenu > ul > li:nth-child(9) > a > div.Mrphs-toolsNav__menuitem--title")
    chat_btn.click()
    time.sleep(1)

    count = len(driver.find_elements_by_css_selector("#topForm\:chatList > li"))
    
    if count < 5:
        for i in range(1, count+1):
            message = driver.find_element_by_css_selector("#topForm\:chatList > li:nth-child(" + str(i) + ")")
            messages = messages + message.text + "\n\n"
    
    else:
        for i in range(5):
            num = count - 4 + i
            message = driver.find_element_by_css_selector("#topForm\:chatList > li:nth-child(" + str(num) + ")")
            messages = messages + message.text + "\n\n"
        
except Exception:
    messages = "エラーが発生しました"

print(messages)

data = {'message': f'message: {messages}'}
requests.post(api, headers = headers, data = data)

time.sleep(3)
driver.quit()

