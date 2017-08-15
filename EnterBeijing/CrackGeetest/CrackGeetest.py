import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

import time

#使用chrome driver 打开网页
options = webdriver.ChromeOptions()
options.add_argument('--window-position="0,0"')
options.add_argument('--window-size=1080,800')

chromeDriverPath = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

#使用os.environ 可修改环境变量
os.environ["webdriver.chrome.driver"] = chromeDriverPath


driver = webdriver.Chrome(executable_path=chromeDriverPath,chrome_options=options)
driver.get("http://dun.163.com/trial/jigsaw")

#动作模拟类，模拟各种web 上的行为
#最后需要调用perform才能执行
action = ActionChains(driver)

verifyDive = driver.find_element_by_class_name("yidun_control")

action.move_to_element(verifyDive).perform()

slider = driver.find_element_by_class_name("yidun_slider")
action.click_and_hold(slider)

totalOffset = 0
for i in range(100):
    action.move_by_offset(2,0).perform();
    time.sleep(0.2)

#links = driver.find("//a[@href]")
#for link in links:
#   action.move_to_element(link).click().perform()

WebDriverWait(driver,30).until()