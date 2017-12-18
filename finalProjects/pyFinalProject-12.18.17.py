#pyFinalProject-12/18/17.py 
#by Lukas Odrzywolski
def main():
	persons = [
		Person("Odrzywolski", "Lukas", 16, 145, 68, "Blonde", "Blue"),
		Person("Pillsbury", "Silas", 16, 120, 71, "Brown", "Blue"),
		Person("Dussault", "Riley", 16, 120, 69, "Blonde", "Brown"),
		Person("Palma", "Samantha", 16, 90, 60, "Brown", "Brown"),
		Person("Lorenzo", "Jacob", 16, 120, 69, "Brown", "Brown"),
	]

	selections = {
		"sortByAge" : printSortByAge,
		"sortByLName" : printSortByLName,
		"sortByFName" : printSortByFName,
		"sortByWeight" : printSortByWeight,
		"sortByHeight" : printSortByHeight,
		"sortByHair" : printSortByHair,
		"sortByEyes" : printSortByEyes,
		"addPerson" : addPerson,
		"removePerson" : removePerson,
		"terminateCMD" : False,
		}

	while True:
		printHeader()
		selection = userSelection()
		if selections[selection]:
			selections[selection] (persons)
		else:
			print ("TERMINATING COMMAND LINE...")
			break

class Person:
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
		"FOR PERSONS BY AGE, type sortByAge",
		"FOR PERSONS BY LAST NAME, type sortByLName",
		"FOR PERSONS BY FIRST NAME, type sortByFName",
		"FOR PERSONS BY WEIGHT, type sortByWeight",
		"FOR PERSONS BY HEIGHT, type sortByHeight",
		"FOR PERSONS BY HAIR COLOR, type sortByHair",
		"FOR PERSONS BY EYE COLOR, type sortByEyes",
		"TO ADD A PERSONS, type addPerson",
		"TO REMOVE A PERSONS, type removePerson",
		"TO TERMINATE COMMAND LINE, type terminateCMD",
	]

def userSelection():
	for inputQuestion in inputQuestions:
		print (inputQuestion)
	return input("Enter selection here and press enter:")

def printSortByAge(persons):
	print ("<<<PERSONS SORTED BY AGE>>>")
	sortPersons = sorted(persons, key=lambda student: person.age)
	for student in sortPersons:
		print (str(person.age) + "yr" + ", " + person.lastName + ", " + person.firstName + ", " + str(person.weight) + "lb" + ", " + str(person.height) + "in" + ", " + person.hair + " hair" + ", " + person.eyes + " eyes")

def printSortByLName(persons):
	print ("<<<PERSONS SORTED BY LAST NAME>>>")
	sortPersons = sorted(persons, key=lambda student: person.lastName)
	for student in sortPersons:
		print (person.lastName + ", " + person.firstName + ", " + str(person.age) + "yr" + ", " + str(person.weight) + "lb" + ", " + str(person.height) + "in" + ", " + person.hair + " hair" + ", " + person.eyes + " eyes")

def printSortByFName(persons):
	print ("<<<PERSONS SORTED BY FIRST NAME>>>")
	sortPersons = sorted(persons, key=lambda student: person.firstName)
	for student in sortPersons:
		print (person.firstName + ", " + person.lastName + ", " + str(person.age) + "yr" + ", " + str(person.weight) + "lb" + ", " + str(person.height) + "in" + ", " + person.hair + " hair" + ", " + person.eyes + " eyes")

def printSortByWeight(persons):
	print ( "<<<PERSONS SORTED BY WEIGHT>>>")
	sortPersons = sorted(persons, key=lambda student: person.weight)
	for student in sortPersons:
		print (str(person.weight) + "lb" + ", " + person.lastName + ", " + person.firstName + ", " + str(person.age) + "yr" + ", " + str(person.height) + "in" + ", " + person.hair + " hair" + ", " + person.eyes + " eyes")

def printSortByHeight(persons):
	print ("<<<PERSONS SORTED BY HEIGHT>>>")
	sortPersons = sorted(persons, key=lambda student: person.height)
	for student in sortPersons:
		print (str(person.height) + "in" + ", " + person.lastName + ", " + person.firstName + ", " + str(person.age) + "yr" + ", " + str(person.weight) + "lb" + ", " + person.hair + " hair" + ", " + person.eyes + " eyes")

def printSortByHair(persons):
	print ("<<<PERSONS SORTED BY HAIR COLOR")
	sortPersons = sorted(persons, key=lambda student: person.hair)
	for student in sortPersons:
		print (person.hair + " hair" + ", " + person.lastName + ", " + person.firstName + ", " + str(person.age) + "yr" + ", " + str(person.weight) + "lb" + ", " + str(person.height) + "in" + ", " + person.eyes + "eyes")

def printSortByEyes(persons):
	print ("<<<PERSONS SORTED BY EYE COLOR>>>")
	sortPersons = sorted(persons, key=lambda student: person.eyes)
	for student in sortPersons:
		print (person.eyes + " eyes" + ", " + person.lastName + ", " + person.firstName + ", " + str(person.age) + "yr" + ", " + str(person.weight) + "lb" + ", " + str(person.height) + "in" + ", " + person.hair + " hair")

def addPerson(persons):
	print ("<<<ADD PERSONS>>>")
	newStudentLName = input("ENTER LAST NAME: ")
	newStudentFName = input("ENTER FIRST NAME: ")
	newStudentAge = int(input("ENTER AGE: "))
	newStudentWeight = int(input("ENTER WEIGHT: "))
	newStudentHeight = int(input("ENTER HEIGHT: "))
	newStudentHair = input("ENTER HAIR COLOR: ")
	newStudentEyes = input("ENTER EYE COLOR: ")
	persons.append(Person(newStudentLName, newStudentFName, newStudentAge, newStudentWeight, newStudentHeight, newStudentHair, newStudentEyes))

def removePerson(persons):
	print ("<<<REMOVE STUDENT>>>")
	indexRemoved = int(input("ENTER INDEX OF STUDENT: "))
	print ("REMOVED " + persons[indexRemoved].lastName + " FROM LIST")
	persons.pop(indexRemoved)

main()