	
#dict
#d={1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday"}
#def return_day(x):
#    return d[x]

import re
from collections import defaultdict

f = open("test.vcf", "rt")
#print(f.readline())
arr=[]
dic={}
print(type(dic))
for line in f:
	arr=re.split("\t",line)
	#print(arr[0])


	if "#CHR" in arr[0]:
		print("X")
	else:
		print(line.strip())

	
f.close()

