from operator import itemgetter
import sys
from heapq import nlargest

current_word=None
current_count=0
word=None
dict1={}
dict2={}
for line in sys.stdin:
	word,count=line.split('\t')
	try:
		count=int(count)
	except ValueError:
		continue
	if current_word==word:
		current_count+=count
	else:
		if current_word:
			dict1[current_word]=current_count
		current_count=count
		current_word=word
if current_word==word:
	dict1[current_word] = current_count
trigrams = nlargest(10, dict1, key = dict1.get) 
for key in trigrams:
	print(str(key)+'\t'+str(dict1[key]))
sys.stdout.flush()
