
class node:# A node class to generate new nodes f
	def __init__(self,data=None):
		self.data=data
		self.next=None#next pointer will be none because new node wont be pointing


class linked_list:
	def __init__(self):
		self.head=node() #an empty node which will act as a starting point
	def add(self,data):
		new_node=node(data) # node which will store the data
		curr=self.head # we gonna start at leaft most node and start until its none which tells its empty
		while curr.next!=None: #iterate till its reaches the next pointer of last node which is none
			curr=curr.next 
		curr.next=new_node #sets new node  in the end as curr next is at the last


	def length(self):
		curr=self.head
		total=0
		while curr.next!=None:
			total=total+1
			curr=curr.next
		return total
		
	def display(self):
		curr=self.head
		elems=[]
		while curr.next!=None:
			curr=curr.next#iterate over all the nodes
			elems.append(curr.data)#add the data to the list
		print(elems)	
			
	def get(self,index):
		if index>=self.length():
			print('Index out of range')
			return None
		
		curr_node=self.head
		curr_idx=0
		while True:
			curr_node=curr_node.next
			if curr_idx==index:
				return curr_node.data
			curr_idx+=1	
	
	def delete(self,index):
		if index>=self.length():
			print('Index out of range')
			return None
		
		curr_node=self.head
		curr_idx=0
		while True:
			last_node=curr_node 
			curr_node=curr_node.next
			if curr_idx==index:
				last_node.next=curr_node.next
				return 
			curr_idx+=1	
	# Inserts the node 'node' at index 'index'. Indices begin at 0.
	# If the 'index' is greater than or equal to the length of the linked 
	# list the 'node' will be appended.
	def insert_node(self,index,node):
		if index<0:
			print "ERROR: 'Erase' Index cannot be negative!"
			return
		if index>=self.length(): # append the node
			cur_node=self.head
			while cur_node.next!=None:
				cur_node=cur_node.next
			cur_node.next=node
			return
		cur_node=self.head
		prior_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				prior_node.next=node
				return
			prior_node=cur_node
			cur_idx+=1

	# Sets the data at index 'index' equal to 'data'.
	# Indices begin at 0. If the 'index' is greater than or equal 
	# to the length of the linked list a warning will be printed 
	# to the user.
	def set(self,index,data):
		if index>=self.length() or index<0:
			print "ERROR: 'Set' Index out of range!"
			return
		cur_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				cur_node.data=data
				return
			cur_idx+=1			

if __name__=='__main__':	
	a=linked_list()
	a.add(10)
	a.add(20)
	a.add(30)
	a.add(10)
	a.add(1000)
	a.add(90)
	a.display()
	a.delete(4)
	print(a.get(4))



			
