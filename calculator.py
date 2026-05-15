#_______________________________________________________Main File_______________________________________________________

#import dependancies
from config import *

#_______________________________________________________Get Input_______________________________________________________

#what kind of calculation are we doing?
calcType = input("What kind of calculation would you like to preform? (S)cientific, (G)raphing, (C)aclulus, C(A)S or (P)hysical Motion:   ")

if calcType == "S" or calcType == "s": #Calls the scientific calculator
    from scientific import sCalc

    print("Scientifit Calculator.")
    messyExpression = input("What expression would you like evaluated? Input without equal sign, ex... 2^3+3*4/7. Allowed Operators, (), ^, *, /, +, -:   ")

    solution = sCalc(messyExpression)

    print(messyExpression, "=", solution)

if calcType == "G" or calcType == "g": #Calls the graphing calculator
    from graphing import gCalc
    # Get the Function as input
    print("Graphing Calculator. Known Constants: e, pi. Known Functions and their syntax. All trig functions such as sinx, cosx, cotx. or sin(x) ect ect. Logarithms: log(x, base) for example log(x, 10). lnx or ln(x)")
    messyFunction = str(input("Enter a function of x: "))

    #Get parameters as input, else use default.
    xmin = input("What is the minimum x value to calculate? Hit enter to use the default of -10.   ")
    if xmin == "":
        xmin = -10

    xmax = input("What is the maximum x value to calculate? Hit enter to use the default of 10.   ")
    if xmax == "":
        xmax = 10

    xcount = input("How many values of x should be calculated? hit enter for the default of 10267.   ")
    print(xcount)
    if xcount == "":
        xcount = "10267"    #any odd number ensures that asymptotes at 0 are caught with the linspace array, 10267 is a prime number close to but greater than 1000

    ymin = input("What is the minimum y value to show on the graph? Hit enter to use the default of -10.   ")
    if ymin == "":
        ymin = -10

    ymax = input("What is the maximum y value to show on the graph? Hit enter to use the default of 10.   ")
    if ymax == "":
        ymax = 10
    gCalc(messyFunction, xmin, xmax, xcount, ymin, ymax)

if calcType == "C" or calcType == "c": #Calls the calculus calculator
    from calculus import cCalc

    deriveIntegrate = input("Are we (D)eriving a function, or (I)ntegrating a function?  ")

    messyFunction = input("Please enter the function:    ")

    solution = cCalc(deriveIntegrate, messyFunction)

    print(f"The derivative of {messyFunction} is {solution}")
