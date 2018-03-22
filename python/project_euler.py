# Project Euler found here: https://projecteuler.net/archives
# many problems can be found here:
# https://github.com/nayuki/Project-Euler-solutions/tree/master/python
# i plan on using this as a reference if i get stuck while working on a problem

def main():
	selections = {
		"problem_1" : problem_1,
		"problem_2" : problem_2,
		"problem_4" : problem_4,
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
	"termCMD",
	]

def userSelection():
	for problem in eulerProblems:
		print (problem)
	return input("Enter command here: ")

#PROBLEMS

def problem_1():
	print("running problem 1")
	ans = sum(i for i in range(1000) if not (i % 3 and i % 5)) # this method of solving the problem works with the interface
	return str(ans)
	# for i in range(1000):	#however this method does not
	# 	if not i % 3 or not i % 5:
	# 		yield i # when i changed this to return the entire function works, but the results are not printed
	# print (sum(i))


def problem_2():
	print ("running problem 2")
	ans = 0
	x = 1
	y = 2
	while x <= 4000000:
		if x % 2 == 0:
			ans += x
		x,y = y,x+y
	return str(ans)

def problem_4():
	ans = max(i*j
		for i in range(100,1000)
		for j in range(100,1000)
		if str(i*j) == str(i*j)[ : : -1])
	return str(ans)

main()