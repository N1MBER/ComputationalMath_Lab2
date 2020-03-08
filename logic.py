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
              "\t1. 1 / sqrt(x)\n" +
              "\t2. 8x + x^2 - x^3/3\n" +
              "\t3. 2x -10 \n" +
              "\t4. sin(x)/(cos(x)^2 + 1\n" +
              "\t5. e^2x\n")
        while 1:
            try:
                answer = int(input("Number of equations: ").strip())
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
                self.accuracy = float(input("Please input a accuracy of integration: ").strip())
                if self.accuracy <= 0:
                    getReadyAnswer(3)
                    continue
                break
            except TypeError:
                getReadyAnswer(3)
                continue
        calculator = Calculator(self.type_mode, self.type_equations, self.x1, self.x2, self.accuracy)
        calculator.calculate()
        del calculator, answer, limits


class Calculator:
    mode_type = 0
    type_equations = 0
    x1 = 0
    x2 = 0
    swap = 1
    step = 0
    accuracy = 0
    solvable = 1
    calculation_error = 0
    result_integral = 0

    def __init__(self, mode_type, type_equations, x1, x2, accuracy):
        self.mode_type = int(mode_type)
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
        i = 2
        while i <= 5000:
            i += 2
            if self.solvable:
                first_integral = self.getIntegral(i)
                second_integral = self.getIntegral(i*2)
                if abs(first_integral - second_integral) <= self.accuracy:
                    self.step = i
                    self.calculation_error = abs(first_integral - second_integral)
                    self.result_integral = second_integral
                    break
                if i == 5000:
                    getReadyAnswer(5)
                    self.step = 0
            else:
                getReadyAnswer(4)
                return
        if self.step > 0:
            printResult(self.result_integral, self.step, self.calculation_error)
        else:
            getReadyAnswer(4)

    def getIntegral(self, step):
        j = self.x1
        step_size = (self.x2 - self.x1) / step
        result = 0
        while j < self.x2:
            if self.mode_type == 1:
                result += self.returnEquation(j) * step_size
            elif self.mode_type == 2:
                result += self.returnEquation(j + step_size) * step_size
            elif self.mode_type == 3:
                result += self.returnEquation(j + step_size / 2) * step_size
            else:
                return
            j += step_size
        return result

    def returnEquation(self, x):
        if self.type_equations == 1:
            if self.x1 < 0 or self.x2 < 0:
                getReadyAnswer(1)
                self.solvable = 0
                return 0
            return 2 * math.sqrt(x)
        elif self.type_equations == 2:
            return 4 * math.pow(x, 2) + math.pow(x, 3) / 3 - math.pow(x, 4) / 12
        elif self.type_equations == 3:
            return 2 * math.pow(x, 2) + 10 * x
        elif self.type_equations == 4:
            return -math.atan(math.cos(x))
        elif self.type_equations == 5:
            return math.pow(math.e, 2 * x) / 2
        else:
            self.solvable = 0
            getReadyAnswer(2)
            return 0


def getReadyAnswer(type_answer):
    if type_answer == 1:
        print("This segment is outside the scope of the function.")
    elif type_answer == 2:
        print("Unknown type.")
    elif type_answer == 3:
        print("Incorrect input.")
    elif type_answer == 4:
        print("No solution.")
    elif type_answer == 5:
        print("The specified accuracy was not achieved")
    else:
        getReadyAnswer(2)


def printResult(integral, steps, accuracy):
    print("Integral value: " + str(integral) +
          "\nCount of steps: " + str(steps) +
          "\nComputational error: " + str(accuracy) + "\n")
