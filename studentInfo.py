import random
import math
def main():
  students = [
    Student("Larsson", "Halsted", 37, 185),
    Student("BonJovi", "Jon", 55, 170),
    Student("Odrzywolski", "Lukas", 16, 145)
  ]

  printHeader()
  selection = getUserSelection()
  if selection == 0:
    printStudentsByAge(students)
  elif selection == 1:
    printStudentsByLName(students)
  elif selection == 2:
    printStudentsByFName(students)
  elif selection == 3:
    printStudentsByWeight(students)
  elif selection == 4:
    printSumAge(students)
  elif selection == 5:
    printAvgAge(students)
  else:
    print ("SELECTION NOT RECOGNIZED")

class Student:
  def __init__(self, lastName, firstName, age, weight):
    self.lastName = lastName
    self.age = age
    self.firstName = firstName
    self.weight = weight
    self.assignRandomAge()
    self.assignRandomWeight()

  def assignRandomName(self):
    pass

  def assignRandomAge(self):
    self.age = random.randint(0,100)

  def assignRandomWeight(self):
    self.weight = random.randint(80,185)

  def assignRandomHeight(self, isMetric):
    pass

inputQuestions = [ 
  "For STUDENTS BY AGE, type 0",
  "For STUDENTS BY LAST NAME, type 1",
  "For STUDENTS BY FIRST NAME, type 2",
  "For STUDENTS BY WEIGHT, type 3",
  "For SUM of STUDENT AGES type 4",
  "For AVERAGE of STUDENT AGES type 5",
]

def getUserSelection():
  for inputQuestion in inputQuestions:
    print (inputQuestion)
  return int(input("Type selection and press enter:"))

def printHeader():
    print("HEADER TEXT HERE")

def printStudentsByAge(students):
  print ("----Students By Age-----")
  sortStudents = sorted(students, key=lambda student: student.age)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age) + "y/o" + ", " + str(student.weight) + "lb")

def printStudentsByLName(students):
  print ("----Students By Last Name-----")
  sortStudents = sorted(students, key=lambda student: student.lastName)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age) + "y/o" + ", " + str(student.weight) + "lb")

def printStudentsByFName(students):
  print ("----Students By First Name-----")
  sortStudents = sorted(students, key=lambda student: student.firstName)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age) + "y/o" + ", " + str(student.weight) + "lb")

def printStudentsByWeight(students):
  print ("----Students By Weight---")
  sortStudents = sorted(students, key=lambda student: student.weight)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age) + "y/o" + ", " + str(student.weight) + "lb")

def printSumAge(students):
  print ("Answer:")
  #for student in students:

def printAvgAge(students):
  print ("Answer:")

main()