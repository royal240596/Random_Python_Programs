import sys
import shlex
import csv
import pprint
import numpy as np
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    def items(self):
        return self.items    

def get_prec(element,i):
	for x in range(len(order_table[0])):
		if element=='$' and order_table[0][x]=='$':
			index_i=get_val_i(i)
			return order_table[x][index_i]
		if element=='+' and order_table[0][x]=='+':
			index_i=get_val_i(i)
			return order_table[x][index_i]
		if element=='-' and order_table[0][x]=='-':
			index_i=get_val_i(i)
			return order_table[x][index_i]
		if element=='*' and order_table[0][x]=='*':
			index_i=get_val_i(i)
			return order_table[x][index_i]
		if element=='/' and order_table[0][x]=='/':
			index_i=get_val_i(i)
			return order_table[x][index_i]
		if element=='i' and order_table[0][x]=='i':
			index_i=get_val_i(i)
			return order_table[x][index_i]
								

def get_val_i(i):
	for x in range(len(order_table[0])):
		if order_table[0][x]=='$' and order_table[0][x]==i:
			return x
		elif order_table[0][x]=='+' and order_table[0][x]==i:
			return x
		elif order_table[0][x]=='-' and order_table[0][x]==i:
			return x
		elif order_table[0][x]=='*' and order_table[0][x]==i:
			return x
		elif order_table[0][x]=='/' and order_table[0][x]==i:
			return x
		elif order_table[0][x]=='i' and order_table[0][x]==i:
			return x					



input_string = "i+i*i"
input_ind = list(shlex.shlex(input_string))

input_ind.append('$')
	
order_table=[]	
with open('order.csv', 'rU') as file2:
		order = csv.reader(file2)
		for row in order:
			order_table.append(row)
pprint.pprint(order_table)	
a='''E->E+E
|E-E
|E*E
|E/E
|i'''


matching_str=Stack()
matching_str.push('$')
	
def evalu(prec_op,i):
	if prec_op=='<':
		matching_str.push(i)
		print('shift')

	elif prec_op=='>':
		matching_str.pop()
		print('reduce')
		a=get_prec(matching_str.peek(),i)
		evalu(a,i)
	elif prec_op=='':
		pass				


for i in input_ind:
		element=matching_str.peek()
		prec_op=get_prec(element,i)
		print(matching_str.items)
		evalu(prec_op,i)
if matching_str.size()==1 and matching_str.peek()=='$':
		print('String accepted')
else:
		print('String not accepted')	

