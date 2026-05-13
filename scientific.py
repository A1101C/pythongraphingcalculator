#_______________________________________________________Scientific Calculator_______________________________________________________

from config import *
from syntaxcleaner import cleaner
from evaluator import evaluate

def sCalc():
    print("Scientifit Calculator.")
    messyExpression = input("What expression would you like evaluated? Input without equal sign, ex... 2^3+3*4/7. Allowed Operators, (), ^, *, /, +, -:   ")

    expression = cleaner(messyExpression)

    solution, imaginary, discontinuity = evaluate(expression)

    if ts == 1:
        print(messyExpression, expression, solution, imaginary, discontinuity)

    print(messyExpression, "=", solution)

