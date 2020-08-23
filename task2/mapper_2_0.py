import nltk
import re
import sys
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer() 
punctuations = '’“”`^-|,!()-[]{};:\\,<>.?@#$%^&*-=+~_—\'\"'
result=[]
trigrams=[]
stop_words = set(stopwords.words('english'))
for line in sys.stdin:
	words=line.strip().lower().split()
	for word in words:
		for x in word:
			if x in punctuations:
				word=word.replace(x,"")
		if word in stop_words:
			continue
		word = lemmatizer.lemmatize(word)
		if word == 'science':
			trigrams.append('*1')
		elif word == 'fire':
			trigrams.append('*2')
		elif word == 'sea':
			trigrams.append('*3')
		else:
			trigrams.append(word)

triDict = {'*1': 'science', '*2': 'fire', '*3': 'sea'}
for k in range(0, len(trigrams)):
	if k+3 >= len(trigrams):
		break;
	trigram = str(trigrams[k])+'_'+str(trigrams[k+1])+'_'+str(trigrams[k+2])
	if(trigram.count('*')==2):
		if '*' in str(trigrams[k]):
			trigram1 = (str(triDict[trigrams[k]])+'_'+str(trigrams[k+1])+'_' + str(trigrams[k+2]))
			trigram1 = re.sub(r'\*.','$',trigram1)
			result.append(trigram1)

		if '*' in str(trigrams[k+1]):
			trigram2 = (str(trigrams[k])+'_'+str(triDict[trigrams[k+1]])+'_'+str(trigrams[k+2]))
			trigram2 = re.sub(r'\*.','$',trigram2)
			result.append(trigram2)
		if '*' in str(trigrams[k+2]):
			trigram3 = (str(trigrams[k])+'_'+str(trigrams[k+1])+'_'+str(triDict[trigrams[k+2]]))
			trigram3 = re.sub(r'\*.','$', trigram3)
			result.append(trigram3)
	else:
		trigram4 = (str(trigrams[k])+'_'+str(trigrams[k+1])+'_'+str(trigrams[k+2]))
		trigram4 = re.sub(r'\*.', '$', trigram4)
		result.append(trigram4)

for tri_gram in result:
	if '$' in tri_gram:
		print('%s\t%s'%(tri_gram, 1))
