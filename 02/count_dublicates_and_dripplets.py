from pprint import pprint
import sys
from collections import defaultdict
path='./strings.txt'
count_twice=0
count_dripplets=0

txt=open(path, 'r')
for line in txt.readlines():
	chars = defaultdict(int)
	print(line)
	for char in line:
		chars[char]+=1
	c2=0
	c3=0
	for c in chars:
		if chars[c] == 2 and c2 == 0:
			count_twice += 1
			c2 = 1
			print("2 " + c)
			pass
		elif chars[c] == 3 and c3 == 0:
			print("3 " + c)
			c3 = 1
			count_dripplets += 1
			pass

print(count_twice)
print(count_dripplets)
print(count_twice * count_dripplets)
sys.exit()