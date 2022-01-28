import threading
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

def restart():
    while True:
        if k.is_pressed(['p', 'o']):
            print("u gau")
            main()

thread = threading.Thread(target = restart)
thread.start()
#thread.join()

t.sleep(1)
main()
t.sleep(5)
driver.save_screenshot("screenshot.png")
#driver.quit()
