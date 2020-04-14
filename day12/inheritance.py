class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    # Write your constructor here
    def __init__(self, firstName, lastName, id, scores):
        super().__init__(firstName, lastName, id)
        self.scores = scores

    # Write your function here
    def calculate(self):
        scoreTotal = sum(self.scores)
        totalSubject = len(self.scores)
        averageMark = scoreTotal / totalSubject
        if (averageMark >= 90 and averageMark <= 100):
            grade = "O"
        elif (averageMark >= 80 and averageMark < 90):
            grade = "E"
        elif (averageMark >= 70 and averageMark < 80):
            grade = "A"
        elif (averageMark >= 55 and averageMark < 70):
            grade = "P"
        elif (averageMark >= 40 and averageMark < 55):
            grade = "D"
        elif (averageMark < 40):
            grade = "T"

        return grade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
