import requests
import re
import time

file = open("level_info.txt", 'r')
all_words = file.read().split('\n')
all_words = ','.join(all_words)
list = list(set(all_words.split(',')))
list.sort()
file.close()

file = open('new_dict.txt', 'a')
for i in list:
    file.write(i.lower()+'\n')

file.close()



#get answers
"""
file = open('all_levels.txt', 'a')

lvl_num = 1
for i in range(0, 500):
    url = f"https://wordscapes.yourdictionary.com/answers/_/_/{lvl_num}/"
    r = str(requests.get(url, allow_redirects=True).content)
    r = r.partition(r'\\"words\\":')[2].partition(r',\\"words_def\\":')[0]

    regex = re.compile('[^A-Z,]')
    r = regex.sub('', r)
    print(r)
    file.write(r+'\n')
    lvl_num+=1
    time.sleep(0.01)

file.close()
"""

#other wordscape websites
#https://wordscapeshelp.com/





#websites for a really big dictionary
'''
url1 = 'https://johnresig.com/files/dict/ospd4.txt'
url2 = 'https://www-personal.umich.edu/~jlawler/wordlist'
url3 = 'http://www.mieliestronk.com/corncob_lowercase.txt'
url4 = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
r1 = requests.get(url1, allow_redirects=True).content
r2 = requests.get(url2, allow_redirects=True).content
r3 = requests.get(url3, allow_redirects=True).content
r4 = requests.get(url4, allow_redirects=True).content
string = str(r1).split('\\n')
string.remove("'")
'''
