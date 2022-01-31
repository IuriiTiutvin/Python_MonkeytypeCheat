import keyboard as k
from selenium import webdriver
import re
import time

driver = webdriver.Chrome('/Users/yura/Desktop/Python/chromedriver')
driver.get("http://monkeytype.com")

def html():
    result = driver.page_source.partition("""class="word active""")[2].partition("""class="keymap hidden""")[0]
    result = re.sub("""class="word""", '> <', result)
    x = re.findall(r"\>([a-z ])\<", result)
    x.append(' ')
    return x

def main():
    for i in range(0, 6):
        #time.sleep(0.5)
        list = html()
        webdriver.ActionChains(driver).send_keys(''.join(list)).perform()
'''
def restart():
    while True:
        if k.is_pressed(['tab', 'return']):
            print("u gau")
            main()
            driver.save_screenshot("screenshot.png")
'''

if __name__ == '__main__':
    main()
    driver.save_screenshot("screenshot.png")
    driver.quit()
