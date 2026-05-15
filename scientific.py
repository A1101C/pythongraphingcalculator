#_______________________________________________________Scientific Calculator_______________________________________________________

from config import *
from syntaxcleaner import cleaner
from evaluator import evaluate

def sCalc(messyExpression):

    expression = cleaner(messyExpression)

    solution, imaginary, discontinuity = evaluate(expression)

    if ts == 1:
        print(messyExpression, expression, solution, imaginary, discontinuity)

    return solution

