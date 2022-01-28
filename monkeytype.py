import threading as thread
import keyboard as k
from selenium import webdriver
import re
import time as t

driver = webdriver.Chrome('/Users/siavash/github/Python/chromedriver')
driver.get("http://monkeytype.com")

def html():
    result = driver.page_source.partition("""class="word active""")[2].partition("""class="keymap hidden""")[0]
    result = re.sub("""class="word""", '> <', result)
    x = re.findall(r"\>([a-z ])\<", result)
    x.append(' ')
    return x

def main():
    for i in range(0, 6):
        list = html()
        webdriver.ActionChains(driver).send_keys(''.join(list)).perform()

if k.is_pressed(['tab', 'shift']):
    main()

main()
t.sleep(2)
driver.save_screenshot("screenshot.png")
#driver.quit()
