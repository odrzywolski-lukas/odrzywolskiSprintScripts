#this document is for testing each Euler problem individually 

def problem_1():
	print ("runing problem_1")
	n = sum(i)
	for i in range(1000):
		if not i % 3 or not i % 5:
			yield i
	print (n)

problem_1()