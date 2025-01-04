class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores: list = None):
        self.scores = scores if scores else []
        super().__init__(firstName, lastName, idNumber)

    def calculate(self):
        avg = self.calculate_avg(self.scores)
        grade = self.calculate_grade(avg)

        return grade

    @staticmethod
    def calculate_avg(scores: list):
        return sum(scores) / len(scores)

    @staticmethod
    def calculate_grade(average: float):
        if 90 <= average <= 100:
            return "O"
        elif 80 <= average < 90:
            return "E"
        elif 70 <= average < 80:
            return "A"
        elif 55 <= average < 70:
            return "P"
        elif 40 <= average < 55:
            return "D"
        else:
            return "T"


if __name__ == "__main__":
    line = input().split()
    # line = "Heraldo Memelli 8135627".split()

    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input())  # not needed for Python
    # numScores = 2  # not needed for Python
    scores = list(map(int, input().split()))
    # scores = list(map(int, "100 80".split()))
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())
