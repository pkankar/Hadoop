from sys import stdin
import re

index = {}

for line in stdin:
	word,postings = line.split('\t')
	index.setdefault(word,{})
	index[word].setdefault(postings)

for word in index:
	postings_list=["%s" % (doc_id) for doc_id in index[word]]
	postings_list = map(lambda s: s.strip(),postings_list)
	posting = ','.join(postings_list)
	print ('%s: %s' % (word,posting))

