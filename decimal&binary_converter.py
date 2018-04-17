
def binarytod(n):
	n=int(n)
	c=[]
	while n!='':
		c.append(n%10)
		n=str(n)
		if len(n)>1:
			n=int(n[:-1])
		else:
			break


	dec=0	
	for i in range(len(c)):
		dec+=(2**i)*c[i]
	return dec
	
def decimaltob(n):
	n=int(n)
	dec=[]
	if n==1 or n==0:
		return n
	while n>=1:

		
		q=n//2
		r=n%2
		n=q
		dec.append(r)
	return dec[::-1]	

wyd=int(input(''' >>Enter 1 to convert Binary to Dec
 >>Enter 2 to convert Dec to Binary
    '''  
	))



if wyd==1:
	a=input('Enter the binary number')
	print(binarytod(a))

elif wyd==2:
	a=input('Enter the DEC number')
	print(decimaltob(a))
