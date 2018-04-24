#this document is for testing each Euler problem individually 
# https://code.mikeyaworski.com/python/project_euler/problem_7 

def problem_1():
	print ("runing problem_1")
	n = sum(i)
	for i in range(1000):
		if not i % 3 or not i % 5:
			yield i
	print (n)

# problem_1()

def largest_prime_factor():
	n = int(input("Number: "))
	i = 2 
	while i * i < n:
		while n % i == 0:
			n = n / i
		i = i + 1
	print (n)

# largest_prime_factor() 

def nth_prime():
	print("working...")
	n = 6
	numOfPrimes = 0
	sol = 1
	while numOfPrimes < n:
		sol += 1
		if sol % (i for i in range(2, int(sol**0.5) + 1) == 0):
			numOfPrimes += 1
	print (str(sol))

nth_prime()

def isPrime(n):
    if n < 2: return "Neither prime, nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# returns the nth prime number
def nthPrime():
	n = input("input nth prime desired here: ")
    numberOfPrimes = 0
    prime = 1

    while numberOfPrimes < n:
        prime += 1
        if isPrime(prime):
            numberOfPrimes += 1
    return prime

# print(nthPrime())