import re
import sys
import string

newword = " "
punctuations = '’“”`^-|,!()-[]{};:\,<>.?@#$%^&*-=+~_—\'\"'
for line in sys.stdin:
	line=line.strip()
	line=line.lower()
	words=line.split()	
	for word in words:
		for x in word:
			if x in punctuations:
				word=word.replace(x,"")
		if (word != ""):
			print('%s\t%s' % (word,1))
#		list.append(word)

#for word in list:	print('%s\t%s' % (word,1))
