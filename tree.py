noi=int(input('No of nodes'))
a=[]
for x in range(noi):
	nodes=input('>>>')
	a.append(nodes)

del_elem=int(input('del'))

length=len(a)



count =0
def count_leaf_odd(a):
	count =0

	for x in range(len(a)):
		try:
			if not a[2*x+1] is None:
				pass
			elif not a[2*x+2] is None:
				pass	
			else:
				count=count+1
		except IndexError:
			count=count+1

							

	return count		
def count_leaf_even(a):
	count =0

	for x in range(len(a)):
		try:
			if not a[2*x+1] is None:
				pass
			elif not a[2*x+2] is None:
				pass	
			else:
				count=count+1
		except IndexError:
			count=count+1

							

	return count-1		
l=a
def dele(d):
	del l[2*d+2]
	del l[2*d+1]
	del l[d]
	
	return l



dele(del_elem)

if length%2==0:

	print(count_leaf_even(l))
else:
	print(count_leaf_odd(l))
