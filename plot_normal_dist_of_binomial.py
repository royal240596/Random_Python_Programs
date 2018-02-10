#plotting a normal distribution of binomial distribution

import matplotlib.pyplot as plt 
import seaborn as sn
sn.set()


class plot_bio_norm:
	def __init__(self,n,p):
		self.n=n
		self.p=p
		self.va=[]
		self.xa=[]
		


	
	def fact(self,fac):

		a=1
		if fac==1:
			return fac
		else:
			while fac>0:
				a=a*fac
				fac=fac-1	
			return a


	def binomial_calc(self,*args):
		for x in args:
			self.xa.append(x)
			self.va.append((self.fact(self.n)*(self.p**x)*((1-self.p)**(self.n-x)))/(self.fact(x)*self.fact(self.n-x)))
		return self.va

	
	


