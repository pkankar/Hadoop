import io
import csv
import sys
count = 0




a = sys.stdin[0]

with open("a",'r',encoding='utf-8',errors='ignore') as csvfile:
	readCSV = csv.reader(csvfile,delimiter=',')

#sys.stdin.reconfigure(encodind='utf-8',errors='ignore')
#sys.setdefaultencoding('utf-8')
#data = sys.stdin.readlines()
#for row in csv.reader(data):
	for row in readCSV:
		E_id=""
		salary="-"
		country="-"
		passcode="-"
		name="-"
		len1 = len(row)
		if (len1==4):
			E_id=row[0]
			salary= row[1]
			country=row[2]
			passcode=row[3]
		else:
			E_id=row[0]
			name=row[1]
		print('%s\t%s\t%s\t%s\t%s' %(E_id, salary,country,passcode,name))
