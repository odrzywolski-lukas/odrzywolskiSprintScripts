# Project Euler found here: https://projecteuler.net/archives
# many problems can be found here:
# https://github.com/nayuki/Project-Euler-solutions/tree/master/python
# i plan on using this as a reference if i get stuck while working on a problem

import fractions
from eulerLib import isPrime

def main():
	selections = {
		"problem_1" : problem_1,
		"problem_2" : problem_2,
		"problem_3" : problem_3,
		"problem_4" : problem_4,
		"problem_5" : problem_5,
		"problem_6" : problem_6,
		"problem_7" : problem_7,
		"termCMD" : False,
		}

	printHeader()

	while True:
		selection = userSelection()
		if selections[selection]:
			print(selections[selection] ())
		else:
			print ("TERMINATING COMMAND LINE...")
			break

#INTERFACE

def printHeader():
	print ("Project Euler")
	print ("...")

eulerProblems = [
	"problem_1",
	"problem_2",
	"problem_3",
	"problem_4",
	"problem_5",
	"problem_6",
	"problem_7",
	"termCMD",
	]

def userSelection():
	for problem in eulerProblems:
		print (problem)
	return input("Enter command here: ")

#PROBLEMS

def problem_1():
	print("running problem 1")
	sol = sum(i for i in range(1000) if not (i % 3 and i % 5)) # this method of solving the problem works with the interface
	return str(sol)
	# for i in range(1000):	#however this method does not
	# 	if not i % 3 or not i % 5:
	# 		yield i # when i changed this to return the entire function works, but the results are not printed
	# print (sum(i))


def problem_2():
	print ("running problem 2")
	sol = 0
	x = 1
	y = 2
	while x <= 4000000:
		if x % 2 == 0:
			sol += x
		x,y = y,x+y
	return str(sol)

def problem_3():
	print ("running problem 3")
	n = 600851475143
	i = 2
	while i * i < n:
		while n % i == 0:
			n = n / i
		i = i + 1
	return n

def problem_4():
	print ("running problem4")
	sol = max(i*j
		for i in range(100,1000)
		for j in range(100,1000)
		if str(i*j) == str(i*j)[ : : -1])
	return str(sol)

def problem_5():
	print ("running problem 5")
	sol = 1
	for i in range(1, 21):
		sol *= i // fractions.gcd(i, sol)
	return str(sol)

def problem_6():
	print ("running problme 6")
	sumOfSquare = sum(i**2 for i in range(100))
	squareOfSum = (sum(i for i in range(100)))**2
	sol = squareOfSum - sumOfSquare
	return str(sol)

def problem_7():
	print ("running problem 7")
	n = 10001
	numOfPrimes = 0
	sol = 1
	while numOfPrimes < n:
		sol += 1
		if isPrime(sol):
			numOfPrimes += 1
	return str(sol)

main()