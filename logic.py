import math

if __name__ == "__main__":
    print("It's a computation file, please run \'main.py\'")


def leftSideModSolve():
    worker = Worker(1)
    worker.chooseMode()
    del worker


def rightSideModSolve():
    worker = Worker(2)
    worker.chooseMode()
    del worker


def mediumModeSolve():
    worker = Worker(3)
    worker.chooseMode()
    del worker


class Worker:
    type_mode = 0
    type_equations = 0
    x1 = 0
    x2 = 0
    accuracy = 0

    def __init__(self, type_mode):
        self.type_mode = type_mode

    def chooseMode(self):
        if self.type_mode == 1:
            print("Mode: Left side")
        elif self.type_mode == 2:
            print("Mode: Right side")
        elif self.type_mode == 3:
            print("Mode: Medium")
        else:
            getReadyAnswer(2)
            return
        self.select_variant()

    def select_variant(self):
        print("Please choose a equations:\n" +
              "\t1. 1/sqrt(x)\n" +
              "\t2. 8x + x^2 - x^3/3\n" +
              "\t3. x/sqrt(x^4 + 16)\n" +
              "\t4. sin(x)/(cos(x)^2 + 1\n" +
              "\t5. e^2x\n")
        while 1:
            try:
                answer = int(input("Number of equations: "))
                if answer == 1:
                    self.type_equations = 1
                    break
                elif answer == 2:
                    self.type_equations = 2
                    break
                elif answer == 3:
                    self.type_equations = 3
                    break
                elif answer == 4:
                    self.type_equations = 4
                    break
                elif answer == 5:
                    self.type_equations = 5
                    break
                else:
                    getReadyAnswer(2)
                    continue
            except TypeError:
                getReadyAnswer(3)
                continue
            except ValueError:
                getReadyAnswer(3)
                continue
        while 1:
            try:
                limits = list(input("Please input a limits of integration in format x1 x2: ").split(" "))
                print(limits)
                if len(limits) == 2:
                    self.x1 = float(limits[0].strip())
                    self.x2 = float(limits[1].strip())
                    break
                else:
                    getReadyAnswer(3)
                    continue
            except TypeError:
                getReadyAnswer(3)
                continue
        while 1:
            try:
                answer = input("Please input a accuracy of integration: ")
                self.accuracy = float(answer)
                if self.accuracy <= 0:
                    getReadyAnswer(3)
                    continue
                break
            except TypeError:
                getReadyAnswer(3)
                continue
        self.startOfCalculation()
        del answer, limits

    def startOfCalculation(self):
        calculator = Calculator(self.type_equations, self.x1, self.x2, self.accuracy)
        calculator.calculate()


class Calculator:
    type_equations = 0
    x1 = 0
    x2 = 0
    swap = 1
    accuracy = 0
    solvable = 1

    def __init__(self, type_equations, x1, x2, accuracy):
        self.type_equations = type_equations
        self.accuracy = accuracy
        if x1 > x2:
            self.swap *= -1
            self.x1 = x2
            self.x2 = x1
        else:
            self.x1 = x1
            self.x2 = x2

    def calculate(self):
        i = 0
        while i <= 10000:
            if self.solvable:
                print("ss")
            else:
                getReadyAnswer(4)
                return
            i += 1

    def returnEquation(self, x):
        if self.type_equations == 1:
            if self.x1 <= 0 or self.x2 <= 0:
                getReadyAnswer(1)
                self.solvable = 0
                return
            return 1 / math.sqrt(x)
        elif self.type_equations == 2:
            return 8 * x + x ^ 2 - (x ^ 3) / 3
        elif self.type_equations == 3:
            return x / math.sqrt(x ^ 4 + 16)
        elif self.type_equations == 4:
            return math.sin(x) / (math.pow(math.cos(x), 2) + 1)
        elif self.type_equations == 5:
            return math.pow(math.e, 2 * x)
        else:
            self.solvable = 0
            getReadyAnswer(2)


def getReadyAnswer(type_answer):
    if type_answer == 1:
        print("This segment is outside the scope of the function.")
    elif type_answer == 2:
        print("Unknown type.")
    elif type_answer == 3:
        print("Incorrect input.")
    elif type_answer == 4:
        print("No solution.")
    else:
        getReadyAnswer(2)
