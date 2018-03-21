#Project Euler

def main():
	selections = {
		"problem_1" : problem_1,
		"termCMD" : False,
		}

	printHeader()

	while True:
		selection = userSelection()
		if selections[selection]:
			selections[selection] ()
		else:
			print ("TERMINATING COMMAND LINE...")
			break

#INTERFACE

def printHeader():
	print ("Project Euler")
	print ("...")

eulerProblems = [
	"problem_1",
	"termCMD",
	]

def userSelection():
	for problem in eulerProblems:
		print (problem)
	return input("Enter command here: ")

#PROBLEMS

def problem_1():
	print("running problem 1")
	print (sum(i for i in range(1000) if not (i % 3 and i % 5))) # this method of solving the problem works with the interface
	# for i in range(1000):	#however this method does not
	# 	if not i % 3 or not i % 5:
	# 		yield i # when i changed this to return the entire function works, but the results are not printed
	# print (sum(i))
main()