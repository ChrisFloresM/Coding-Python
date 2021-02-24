#Christian Flores 21/02/2021

class Person:


	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber


	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):


    def __init__(self, firstName, lastName, idNumber, scores):
        """Constructor method"""
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores


    def calculate(self):
        self.average = sum(scores)/len(scores)
        if self.average < 40:
            self.char = "T"
        elif self.average < 55:
            self.char = "D"
        elif self.average < 70:
            self.char = "P"
        elif self.average < 80:
            self.char = "A"
        elif self.average < 90:
            self.char = "E"
        elif self.average <= 100:
            self.char = "O"
        return self.char


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())