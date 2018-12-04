from pprint import pprint
import sys
path='./number.txt'
cur=0
test=[]
test.append(cur)
found_double = False

while found_double == False:
	txt=open(path, 'r')
	print('----')
	for line in txt.readlines():
		print(line)
		print(cur)
		cur = cur + int(line)
		if cur in test:
			print(str(cur) + 'is double')
			found_double = True
			sys.exit()
		else:
			test.append(cur)
