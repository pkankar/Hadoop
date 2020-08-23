import sys
import string

l_u_id = None
name = "-"


for line in sys.stdin:
	line = line.strip()
	id,s,c,p,n = line.split("\t")

	if not l_u_id or l_u_id != id:
		l_u_id = id
		s=s
		c=c
		p=p
		name=n
	elif id=l_u_id:
		n=name
		print ('%s\t%s\t%s\t%s\t%s' %(id,s,c,p,n))




