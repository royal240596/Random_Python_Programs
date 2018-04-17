def fibb(n):
	a=1
	b=1
	x=[1,1]
	c=0	
	while len(x)!=int(n):

		c=a+b
		b=a
		a=c
		x.append(c)
	return x	

def fib(n):
	a=1
	b=1
	x=[1,1]
	c=0	
	while c<=int(n):

		c=a+b
		b=a
		a=c
		x.append(c)
	if x[-1]>int(n):
		x.pop(-1)	
	return x


wyd=int(input(''' >>Enter 1 to have the program generate the Fibonacci sequence to your specified number
 >>Enter 2 to have the program generate the Fibonacci sequence having specified number of elements
    '''  
	))



if wyd==1:
	a=input('Enter the number of Fibbonaci number you want to print')
	print(fibb(a))

elif wyd==2:
	a=input('Enter the number till which you want to generate Fibbonaci sequence')
	print(fib(a))








