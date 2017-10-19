#studentDatabase.py 
#by Lukas Odrzywolski
def main():
	students = [
		Student("Odrzywolski", "Lukas", 16, 145, 68, "Blonde", "Blue"),
		Student("Pillsbury", "Silas", 16, 120, 71, "Brown", "Blue"),
		Student("Dussault", "Riley", 16, 120, 69, "Blonde", "Brown"), 
	]

	selections = {
		"sortByAge" : printSortByAge,
		"sortByLName" : printSortByLName,
		"sortByFName" : printSortByFName,
		"sortByWeight" : printSortByWeight,
		"sortByHeight" : printSortByHeight,
		"sortByHair" : printSortByHair,
		"sortByEyes" : printSortByEyes,
		"addStudent" : addStudent,
		"removeStudent" : removeStudent,
		"terminateCMD" : terminateCMD
		}

	T = True
	while T:
		printHeader()
		selection = userSelection()
		selections[selection] (students)

class Student:
	def __init__(self, lastName, firstName, age, weight, height, hair, eyes):
		self.lastName = lastName
		self.firstName = firstName
		self.age = age
		self.weight = weight
		self.height = height
		self.hair = hair
		self.eyes = eyes

def printHeader():
		print ("---LIST OF COMMANDS---")

inputQuestions = [
		"FOR STUDENTS BY AGE, type sortByAge",
		"FOR STUDENTS BY LAST NAME, type sortByLName",
		"FOR STUDENTS BY FIRST NAME, type sortByFName",
		"FOR STUDENTS BY WEIGHT, type sortByWeight",
		"FOR STUDENTS BY HEIGHT, type sortByHeight",
		"FOR STUDENTS BY HAIR COLOR, type sortByHair",
		"FOR STUDENTS BY EYE COLOR, type sortByEyes",
		"TO ADD A STUDENT, type addStudent",
		"TO REMOVE A STUDENT, type removeStudent",
		"TO TERMINATE COMMAND LINE, type terminateCMD",
	]

def userSelection():
	for inputQuestion in inputQuestions:
		print (inputQuestion)
	return input("Enter selection here and press enter:")

def terminateCMD():
	print ("TERMINATING COMAND LINE...")
	T = False
	
def addStudent(students):
	print ("<<<ADD STUDENTS>>>")
	newStudentLName = input("ENTER LAST NAME: ")
	newStudentFName = input("ENTER FIRST NAME: ")
	newStudentAge = int(input("ENTER AGE: "))
	newStudentWeight = int(input("ENTER WEIGHT: "))
	newStudentHeight = int(input("ENTER HEIGHT: "))
	newStudentHair = input("ENTER HAIR COLOR: ")
	newStudentEyes = input("ENTER EYE COLOR: ")
	students.append(Student(newStudentLName, newStudentFName, newStudentAge, newStudentWeight, newStudentHeight, newStudentHair, newStudentEyes))

def removeStudent(students):
	print ("<<<REMOVE STUDENT>>>")
	indexRemoved = int(input("ENTER INDEX OF STUDENT: "))
	print ("REMOVED " + students[indexRemoved].lastName + " FROM LIST")
	students.pop(indexRemoved)

def printSortByAge(students):
	print ("<<<STUDENTS SORTED BY AGE>>>")
	sortStudents = sorted(students, key=lambda student: student.age)
	for student in sortStudents:
		print (str(student.age) + "yr" + ", " + student.lastName + ", " + student.firstName + ", " + str(student.weight) + "lb" + ", " + str(student.height) + "in" + ", " + student.hair + " hair" + ", " + student.eyes + " eyes")

def printSortByLName(students):
	print ("<<<STUDENTS SORTED BY LAST NAME>>>")
	sortStudents = sorted(students, key=lambda student: student.lastName)
	for student in sortStudents:
		print (student.lastName + ", " + student.firstName + ", " + str(student.age) + "yr" + ", " + str(student.weight) + "lb" + ", " + str(student.height) + "in" + ", " + student.hair + " hair" + ", " + student.eyes + " eyes")

def printSortByFName(students):
	print ("<<<STUDENTS SORTED BY FIRST NAME>>>")
	sortStudents = sorted(students, key=lambda student: student.firstName)
	for student in sortStudents:
		print (student.firstName + ", " + student.lastName + ", " + str(student.age) + "yr" + ", " + str(student.weight) + "lb" + ", " + str(student.height) + "in" + ", " + student.hair + " hair" + ", " + student.eyes + " eyes")

def printSortByWeight(students):
	print ( "<<<STUDENTS SORTED BY WEIGHT>>>")
	sortStudents = sorted(students, key=lambda student: student.weight)
	for student in sortStudents:
		print (str(student.weight) + "lb" + ", " + student.lastName + ", " + student.firstName + ", " + str(student.age) + "yr" + ", " + str(student.height) + "in" + ", " + student.hair + " hair" + ", " + student.eyes + " eyes")

def printSortByHeight(students):
	sortStudents = sorted(students, key=lambda student: student.height)
	for student in sortStudents:
		print (str(student.height) + "in" + ", " + student.lastName + ", " + student.firstName + ", " + str(student.age) + "yr" + ", " + str(student.weight) + "lb" + ", " + student.hair + " hair" + ", " + student.eyes + " eyes")

def printSortByHair(students):
	sortStudents = sorted(students, key=lambda student: student.hair)
	for student in sortStudents:
		print (student.hair + " hair" + ", " + student.lastName + ", " + student.firstName + ", " + str(student.age) + "yr" + ", " + str(student.weight) + "lb" + ", " + str(student.height) + "in" + ", " + student.eyes + "eyes")

def printSortByEyes(students):
	sortStudents = sorted(students, key=lambda student: student.eyes)
	for student in sortStudents:
		print (student.eyes + " eyes" + ", " + student.lastName + ", " + student.firstName + ", " + str(student.age) + "yr" + ", " + str(student.weight) + "lb" + ", " + str(student.height) + "in" + ", " + student.hair + " hair")
	
main()