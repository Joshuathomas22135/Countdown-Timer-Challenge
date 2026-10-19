""" Write a python program to build a Countdown Timer Challenge program using Python. They will use recursion to count down, count up,
demonstrate how recursive calls build and unwind, calculate factorial values, and understand why every recursive function needs a safe base case to avoid
stack overflow."""

print("Countdown from 25")
def countdown(number):
    if number == 0:
        print("Time is up")
        return

    print(number)
    countdown(number - 1)

countdown(25)
print()

print("Build and unwind")
def buildAndUnwind(level):
    if level == 0:
        print("Reached base case")
        return

    print(f"Building the level: {level}")
    buildAndUnwind(level - 1)
    print(f"Unwinding level: {level}")

buildAndUnwind(6)
print()

print("Counting w/ Recursion")

def countUp(number):
    if number > 12:
        return

    print(number)
    countUp(number + 1)

countUp(12)
print()

print("Factorial w/ Recursion")

def factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)
print(f"Factorial: {factorial(10)}")
