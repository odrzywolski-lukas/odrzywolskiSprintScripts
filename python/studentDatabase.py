#studentDatabase.py 
#by Lukas Odrzywolski

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import text

engine = create_engine('sqlite:///studentDB.db', echo=True)

def main():
	conn = engine.connect()
	metadata = MetaData()
	createTables(metadata, conn)
	statement = text("INSERT INTO students (age, weight, height, hair, eyes)"
		"VALUES(Odrzywolski', 'Lukas', 16, 145, 68, 'Blonde', 'Blue')")
	conn.execute(statement)

	query = text("SELECT * from students JOIN ")
	result = conn.execute(query).fetchall()
	print (result)

	# students = [
	# 	Student("Odrzywolski", "Lukas", 16, 145, 68, "Blonde", "Blue"), 
	# ]

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
		"terminateCMD" : False
		}
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

	while True:
		printHeader()
		selection = userSelection()
		if selections[selection]:
			selections[selection] (students)
		else:
			print ("TERMINATING COMMAND LINE...")
			break

class Student:
	def __init__(self, lastName, firstName, age, weight, height, hair, eyes):
		self.lastName = lastName
		self.firstName = firstName
		self.age = age
		self.weight = weight
		self.height = height
		self.hair = hair
		self.eyes = eyes

def createTables(metadata, conn):
	students = Table('students', metadata,
		Column("lastName", String),
		Column("firstName", String),
		Column("age", Integer),
		Column("weight", Integer),
		Column("height", Integer),
		Column("hair", String),
		Column("eyes", String))
	metadata.create_all(engine)

# def initiateTables(metadata, conn):
# 	for student in students:
# 		statement = text("INSERT INTO students (age, weight, height, hair, eyes)"
# 			"VALUES(Odrzywolski', 'Lukas', 16, 145, 68, 'Blonde', 'Blue')")

def printHeader():
		print ("---LIST OF COMMANDS---")

def userSelection():
	for inputQuestion in inputQuestions:
		print (inputQuestion)
	return input("Enter selection here and press enter:")

def addStudent(students):
	pass

def removeStudent(students):
	pass

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