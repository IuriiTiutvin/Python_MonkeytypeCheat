import re
import time
'''
f = open("all_groups.txt", 'r+')
x = f.readlines()
x.sort()
f.truncate(0)
f.write(''.join(x))
f.close()
'''


'''
f = open("all_groups.txt", 'r')
x = f.read()
x = x.lower()
x = re.sub(" ", '', x).split('\n')
y = list(set(x))
y.sort()
print(len(x))
print(len(y))
print(len(x)-len(y))

for element in y:
    if element in x:
        x.remove(element)
print(x)
f.close()
'''
#gets rid of copies
'''
f = open("kpop_g3.txt", 'r+')
x = f.readlines()
x = list(set(x))
x.sort()

f.truncate(0)
time.sleep(0.1)

f.write(''.join(x))

f.close()
'''
#combining lists
'''
f = open("all_groups.txt", 'w')
f1 = open("kpop_g1.txt", 'r+')
f2 = open("kpop_g2.txt", 'r+')
f3 = open("kpop_g3.txt", 'r+')

x1 = f1.readlines()
x2 = f2.readlines()
x3 = f3.readlines()
x = x1+x2+x3
#print(len(x))
x = list(set(x))
x.sort()
#print(len(x))

f.write(''.join(x))

f.close()
f1.close()
f2.close()
f3.close()
'''
#opens
'''
f = open("kpop_groups_popular.txt","r+")
x = f.read()
x = x.lower()
x = re.sub(" ", '', x)
print(x)
'''
#deletes notes
'''
f = open("kpop_g2.txt","r+")
x = f.read()
result = re.sub(r"\((2021 group)\)", "", x)
f.truncate(0)
time.sleep(0.1)
f.write(result)
'''
