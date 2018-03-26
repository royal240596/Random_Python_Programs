noi=int(input())
a= list(map(int, input().split()))
# for _ in range(noi):
# 	nodes=input('>> ')
# 	a.append(nodes)
del_elem=int(input())
length=len(a)



count =0
def count_leaf_odd(a):
	count =0

	for x in range(len(a)):
		try:
			if not (a[2*x+1] and [2*x+2] )is None:
				pass
		except IndexError:
			if a[x]==2:
				count=count-1
			else:
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
def dele(d):
	l=a

	if len(l)>(2*d+2):
		l.pop(2*d+2)
		l.pop(2*d+1)
		l.pop(d)
	else:
		l.pop(d)	
	


dele(del_elem)

print('l'+str(a))


if length%2==0:

	print(count_leaf_even(a))
else:
	print(count_leaf_odd(a))
