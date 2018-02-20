
def binary_search(arr,val):
	if (len(arr)==0) or (len(arr)==1 and arr[0]!=val):
		return False

	mid=arr[len(arr)//2]
	
	if val==mid:
		return True
	elif val>mid:
		return binary_search(arr[mid+1:],val)		
	else:
		return binary_search(arr[:mid-1],val)	

if __name__=='__main__':
  a=[1,2,3,4,5,6,7]

  print(binary_search(a,9))		
