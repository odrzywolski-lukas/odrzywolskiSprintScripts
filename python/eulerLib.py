# euler lib is to hold functions required to conduct project euler 

import array, math, sys

def sqrt(x):
	assert x >= 0
	i = 1
	while i * i <=x:
		i *= 2
	y = 0
	while i >0:
		if (y + i)**2 <= x:
			y += i
		i //= 2
	return y

def isPrime(n):
	for i in range(2, int(n*0.5) + 1):
		if n % i == 0:
			return False
	return True