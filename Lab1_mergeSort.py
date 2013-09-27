#!/usr/bin/python

def merge(left, right):
	result = []

	if len(left) > len(right):
		bigger = left
		smaller = right
	else:
		bigger = right
		smaller = left

	index = 0
	
	for i in bigger:
		while index <= len(smaller):

			if i < smaller[index]:
				result.append(i)
				
				index += 1
				break
				
			if i > smaller[index]:
				result.append(smaller[index])
				
				index += 1
				break
		

		
			

		
	return result

if __name__ == "__main__":
    
	sorted = merge([3, 18, 1], [2, 4, 9])
	print (sorted)

	
