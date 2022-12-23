# Python 3 program to find factorial of given number
def factorial(n):
	if n < 0:
		return 0
	elif n == 0 or n == 1:
		return 1
	else:
		fact = 1
		while(n > 1):
			fact *= n   
            # fact *= n => fact = fact *n
            # fact = 120, n =1
			n -= 1  
            # n -= 1 -> n = n -1
		return fact
        
# Driver Code
num = 7;
print("Factorial of",num,"is",
factorial(num))

