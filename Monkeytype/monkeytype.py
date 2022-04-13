import keyboard as k
from selenium import webdriver
import re
import time


driver = webdriver.Chrome('/Users/yura/Desktop/Python/chromedriver')
driver.get("http://monkeytype.com")

def html():
    result = driver.page_source.partition("""class="word active""")[2].partition("""</div></div></div><div id="keymap" class="hidden">""")[0]
    result = re.sub("""class="word""", '> <', result)
    x = re.findall(r"\>([a-z ])\<", result)
    x.append(' ')
    return x

def main():
    for i in range(0, 6):
        list = html()
        webdriver.ActionChains(driver).send_keys(''.join(list)).perform()
    driver.save_screenshot("screenshot.png")

def restart():
    while True:
        if k.is_pressed(['tab', 'return']):
            time.sleep(2)
            main()
            driver.save_screenshot("screenshot.png")

if __name__ == '__main__':
    try:
        main()
        restart()
    except:
        driver.quit()
