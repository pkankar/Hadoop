import re
import sys
import string

for line in sys.stdin:
	line=line.strip()
	line=line.lower()
	word, count=line.split('\t')
	print('%s\t%s' % (word,count))
