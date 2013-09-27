

def merge(left, right):
	

	result = left + right
	i = 0
	j = 1
	

	
	while j < len(result):

		if result[i] > result[j]:
			k = result[i]
			result[i] = result[j]
			result[j] = k
			i = 0
			j = 1
			
		else:
			i += 1
			j += 1
	
			
	return result
		
