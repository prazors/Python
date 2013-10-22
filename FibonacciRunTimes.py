import time

# This is the recursive solution for the nth
# Fibonacci number
def fib(n):

    if n == 0:
        return 0
    elif n == 1:
    	return 1
    else:
    	
        return fib(n - 2) + fib(n - 1)

# This is the iterative solution for the nth 
# Fibonacci number
def fib2(n):
	
	i = 0
	j = 1
	k = 1
	iterate = 1			##count the number of iterations
	
	if n == i:
		return i
	elif n == j:
		return j

	# this loop will go through each iteration necessary
	# the i, j and k are holders that function in the same way as (n - 1) + (n - 2)
	# you want the loop to end when you are n - 1 iteration from the k value
	while ( iterate + 1  < n ):
		
		i = j
		j = k
		k = i + j
		iterate += 1			
		

	return k

if __name__=="__main__":
	n = 1
	while (n < 36):
		

		start = time.time()   
		r = fib( n )			#run the recursive fibonacci
		end = time.time()	
		print ("(Recursive solution) The %s" %n+" Fibonacci number, %s" % r +" is computed in %.10f seconds" % (end - start))

		start = time.time()		
		i = fib2( n )			#run the iterative fibonacci
		end = time.time()
		print ("(Iterative solution) The %s" %n+" Fibonacci number, %s" % i +" is computed in %.10f seconds" % (end - start))

		print
		n += 1