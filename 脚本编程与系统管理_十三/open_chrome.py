from selenium import webdriver
import os

# 不同版本的chrome对应不同版本的chromedriver且chrome.exe与chromedriver.exe放在同一路径下
chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
os.environ['webdriver.chrome.driver'] = chrome_path
drive = webdriver.Chrome(chrome_path)
drive.get( 'http://10.1.1.32:9000/jenkins/')
