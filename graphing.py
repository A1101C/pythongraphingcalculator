
from config import *

import math
import matplotlib.pyplot as mplot
import numpy as np

from syntaxcleaner import cleaner
from evaluator import evaluate
from constants import *

def gCalc():
    #_______________________________________________________Get Input_______________________________________________________
    # Get the Function as input
    print("Known Constants: e, pi. Known Functions and their syntax. All trig functions such as sinx, cosx, cotx. or sin(x) ect ect. Logarithms: log(x, base) for example log(x, 10). lnx or ln(x)")
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

    #printing for troubleshooting
    if ts == 1:
        print("before float convert.")
        print(xmin)
        print(xmax)
        print(xcount)

    xround = len(xcount)    #xround will be used to round floats later to the same number of significant figures as are contained in xcount
    xmin = float(xmin)  #these values all need to be floats for evaluate to properly calculate them
    xmax = float(xmax)
    xcount= float(xcount)
    ymin = float(ymin)
    ymax = float(ymax)

#_______________________________________________________initialize lists arrays and start calculating values for y_______________________________________________________

    function = cleaner(messyFunction) #clean the user input into a clean function

    if ts == 1: #if troubleshooting print the cleaned function
        print(function)

    xValue = xmin #we want to start at our xmin value so for our first point x is xmin
    linecounter = 0 #this counter keeps track of how many lines we have due to discontinuities, counting of course starts at 0.
    allCoords = {} #this is the master list for groups of coordinates for seperate lines
    allCoords["coords0"] = [] #this initializes the first coord list in our master list
    wasComplex = False #this is to track the change from complex to real numbers
    hasComplex = False #this variable is to label the Y axis when we graph complex/ imaginary numbers

    #set up the loop to calculate the y values for our x values with a linspace array
    xDomain = np.linspace(xmin, xmax, int(xcount))

    for n in xDomain:   #for every value n, in the array xDomain do the loop
        n = round(float(n), xround) #round the float of n to the  same significant figures as are in xcount
        constantsDictionary["x"] = n    #put n in the dictionary so evaluate can use its value in the evaluator

        yValue, imaginary, discontinuity = evaluate(function)   #evalutate function of x and since I  defined constants and various math functions in a dictionary we need to tell it to look in there for those.

        xValue = n  #now we have our (x,y) which is the value of (n, y value rounded)

        isComplex = isinstance(yValue, complex) #this says the current value is complex is true or false

        if isComplex == True:
            wasComplex = True
            yValue = round(float(abs(yValue.imag)), xround)
            hasComplex = True

        if wasComplex == True and isComplex == False:
            wasComplex = False
            yValue = round(float(abs(yValue.imag)), xround)
            allCoords[f"coords{linecounter}"].append((xValue, yValue))
            linecounter = linecounter + 1
            allCoords[f"coords{linecounter}"] = []
            allCoords[f"coords{linecounter}"].append((xValue, yValue))

        if discontinuity == 0:  #if the evaluator does not return a calculation error then we dont have a discontinuity
            allCoords[f"coords{linecounter}"].append((xValue, yValue)) #put the x value we just used and the y value we just calculated into the coords list for the current line we are on

        elif discontinuity == 1: #if we get a calculation error that means we have a discontinutiy, this exception handles that error so it doesnt crash
            print(f"Skipping x={xValue}: Undefined at this point") #this prints that there is a discontinutity at this x value
            linecounter = linecounter + 1 #this increases the linecounter so our sets of x and y values get stored in seperate arrays to make seperate lines so we see asymptotes when they occur
            allCoords[f"coords{linecounter}"] = [] #this creates a new array for our next lines coords to be stored with the new linecounter number

    if pv == 1: #if you want to print all the values then you can see each (x,y) and what line they are on
            print(f"({xValue},",  f"{yValue})", f"Linecounter = {linecounter}")

    #printing for troubleshooting
    if ts == 1:
        print("after Calculation Loop.")
        print(xmin)
        print(xmax)
        print(xcount)
        print(linecounter)

    #_______________________________________________________Put The Values in arrays for matplotlib_______________________________________________________

    allxValues = {} #Create Master Lists for our coordinate groups
    allyValues = {}


    for n in range(linecounter + 1): #this creates a xval and yval array for every line from the linecounter
        allxValues[f"xValue{n}"] = [] #initilize the smaller lists inside our master lists
        allyValues[f"yValue{n}"] = []

        for xValue, yValue in allCoords[f"coords{n}"]:   #this defines the first value of each tuple in each numbered list as xvalue and the second value of each tuple as yvalue,

            allxValues[f"xValue{n}"].append(xValue) #append xvalue list number n to the master lists
            allyValues[f"yValue{n}"].append(yValue) #append yvalue list number n to the master lists

            if pv == 1:  #enable or disable printing to the terminal for troubleshooting.
                print(f"({xValue},",  f"{yValue})", f"Linecounter = {n}")
                if xValue == xmax:
                    print("End Linecounter Loop")

            mplot.plot(allxValues[f"xValue{n}"], allyValues[f"yValue{n}"])


    print("F(x)=",function) #print the function to be verrified

    mplot.ylim(ymin, ymax) #forces the y-axis to stay in our specified range
    mplot.xlim(xmin, xmax) #forces the x axis to stay in our domain
    mplot.grid(True)
    mplot.xlabel("X")

    if hasComplex == True:
        mplot.ylabel("Y, Values for -x on the first line are imaginary.")

    else:
        mplot.ylabel("Y")

    mplot.show() #show us the plotted data









