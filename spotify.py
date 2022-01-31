from selenium import webdriver
import re

driver = webdriver.Chrome('https://www.google.com/search?q=ateez+kpop+songs&rlz=1C5CHFA_enUS914US914&oq=ateez+kpop+songs&aqs=chrome..69i57.13084j0j7&sourceid=chrome&ie=UTF-8')
driver.get("http://monkeytype.com")


def html():
    result = driver.page_source.partition("""class="word active""")[2].partition("""class="keymap hidden""")[0]
    result = re.sub("""class="word""", '> <', result)
    x = re.findall(r"\>([a-z ])\<", result)
    x.append(' ')
    return x
