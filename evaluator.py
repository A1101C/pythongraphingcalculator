from config import *
from constants import constantsDictionary

def evaluate(function):
    discontinutiy = 0

    try: #the try and except is to allow it to continue if we get a /0 error like in 1/x or the inverse trig functions
        solution = eval(function, {"__builtins__": {}}, constantsDictionary)   #evalutate the expression with our defined constants

        if isinstance(solution, complex): #if we get imaginary numbers I want to know so I can handle that later
            imaginaryRoots = 1

        else:
            imaginaryRoots = 0

    except (ZeroDivisionError, ValueError): #if we get a calculation error that means we have a discontinutiy, this exception handles that error so it doesnt crash
        solution = 0
        imaginaryRoots = 0
        discontinutiy = 1

    return solution, imaginaryRoots, discontinutiy
