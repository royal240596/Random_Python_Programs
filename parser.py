dicti={'E':'TB/B','B':'+TB','T':'FY','Y':'*FY','F':'id/(E)'}
op=['+','-','+','*']
var=[i for i in dicti.keys()]

def first(x):
	if dicti[x][0] in op:
			return dicti[x][0]

				

	elif '/' in dicti[x] and dicti[x][0].isupper():
		a=[]
		some=dicti[x]
		s2=some.index('/')
		if some[s2+1].isupper():
			a.append(first(some[s2+1]))
			a.append(first(dicti[x][0]))
			return a
		else:
			a.append(some[s2+1])
			a.append(dicti[x][:s2])
			return a


			
			

		# some2=dicti[x]
		# some3=some2.index(some2)
		# if some2[some3].isupper():
		# 	pass
		# else:
		# 	while not some2[some3].isupper() and some2[some3].isalpha():
		# 		a.append(some2[some3])
		# 		some3+=1
		# 	return ''.join(a)	

				
	elif '/' in dicti[x] and not dicti[x][0].isupper():
		a=[]
		some=dicti[x]
		s2=some.index('/')
		if some[s2+1].isupper():
			a.append(first(some[s2+1]))
			a.append(first(dicti[x][0]))
			return a
		else:
			a.append(some[s2+1])
			a.append(dicti[x][:s2])
			return a


			
			

		# some2=dicti[x]
		# some3=some2.index(some2)
		# if some2[some3].isupper():
		# 	pass
		# else:
		# 	while not some2[some3].isupper() and some2[some3].isalpha():
		# 		a.append(some2[some3])
		# 		some3+=1
		# 	return ''.join(a)	
	
	elif not dicti[x][0].isupper():
		# a=[]
		# for i in range(len(dicti[x])-1):
		# 	print('entered')
		# 	if not dicti[x][i].isupper():
		# 		print(dicti[x][i])
		# 		a.append(dicti[x][i])
		# 	return ''.join(a)
				
		# a=[]
		# some2=dicti[x]
		# some3=some2.index(some2)
		# print(len(some2))
		i=0
		a=[]
		try:
			while not dicti[x][i].isupper() and(dicti[x][i].isalpha()):
				
				a.append(dicti[x][i])
				i+=1
		except IndexError:
			    pass			
		return a	 			 	
		
	else:
		a=dicti[x][0]
		return first(a)
fir={}
l=[]
for i in var:
	fir[i]=first(i)
	# l.append(first(i))

print(fir)	
