ts = 1 #troubelshooting, 1 is true 0 is false

#_______________________________________________________Import Tools_______________________________________________________
import math
import matplotlib.pyplot as mplot
import numpy as np

#_______________________________________________________Get Input_______________________________________________________
# Get the Function as input
print("Known Constants: e, pi. Known Functions and their syntax. All trig functions such as sinx, cosx, cotx. or sin(x) ect ect. Logarithms: log(x, base) for example log(x, 10). lnx or ln(x)")
functofx = str(input("Enter a function of x: "))

#Get parameters as input, else use default.
xmin = input("What is the minimum x value to calculate? Hit enter to use the default of -10.   ")
if xmin == "":
    xmin = -10

xmax = input("What is the maximum x value to calculate? Hit enter to use the default of 10.   ")
if xmax == "":
    xmax = 10

xsteps = input("What x increment to use for the calculations? Hit enter to use the default of .01.   ")
print(xsteps)
if xsteps == "":
    xsteps = float(.01)

#printing for troubleshooting
if ts == 1:
    print("before float convert.")
    print(xmin)
    print(xmax)
    print(xsteps)

xmin = float(xmin)
xmax = float(xmax)
xsteps= float(xsteps)

#_______________________________________________________Clean Up the Input_______________________________________________________

#Convert functofx into a format python can evaluate because python cant just evaluate 2x or x^2 or (x+1)x

#create a loop based on a the number of n numbers that could exist as a co-efficient or really just next to x
for n in range(10):
    oldsyntax = str(n) + "x"
    newsyntax = str(n) + "*x"
    functofx = functofx.replace(oldsyntax, newsyntax)
    #print(functofx)

#if the function has trig values, logs, e, or pi we need to be able to handle those too
co_trig = lambda f, x: 1/ f(x)      #this will be used to define our inverse trig functions later
naturallog = lambda f, x: math.log(x, math.e)   #this defines the naturallog function

#we need to replace any trig functions like sinx with sin(x) for the logic in the dictionary to work with the math tool
functofx=functofx.replace("x","(x)")
functofx = functofx.replace("^", "**")

constants = {
    "e": math.e,
    "pi": math.pi,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "csc": lambda x: co_trig(math.sin, x),
    "sec": lambda x: co_trig(math.cos, x),
    "cot": lambda x: co_trig(math.tan, x),
    "log": math.log,
    "ln": lambda x: naturallog(math.log, x),
    }


#_______________________________________________________Output section below this line_______________________________________________________

#initalize our first x value and empty list so we can begin to evaluate points on our graph
x = xmin
coords = []
imaginaryroots = 0

#initalize our x and y arrays for matplotlib
xpoints = []
ypoints = []

#printing for troubleshooting
if ts == 1:
    print("before while loop.")
    print(xmin)
    print(xmax)
    print(xsteps)

#set up the loop to calculate the y values for our x values
while x < xmax + 1:
    constants["x"] = x    #since I am telling eval to look at the constants dictionary I need to add x to the constants dictionary
    y = eval(functofx, {"__builtins__": {}}, constants)   # since I  defined constants and various math functions in a dictionary we need to tell it to look in there.

    if isinstance(y, complex):
        imaginaryroots = 1

    coords.append((x,y))
    x = x + xsteps

#printing for troubleshooting
if ts == 1:
    print("after while loop.")
    print(xmin)
    print(xmax)
    print(xsteps)

#Print the coordinate pairs, print(coords) just prints them on one line, so to get a nice pair I can use a for loop and define the tuples
#print(coords)
if imaginaryroots == 1:
    print("Values for negative x are complex numbers with an imagniary component. a + bi.")

for xval, yval in coords:   #this defines the first value of each index as xval and the second value of each index as yval,
    if isinstance(yval, complex):
        print(f"{xval}, {yval.real} + {yval.imag}i") #this is to replace the j component of the imaginary component of the complex number with i becuase as a physicsist I work with i more than j.
    if ts == 0:  #enable or disable printing to the terminal for troubleshooting.
        print(xval, yval)       #then for every pair of xval and yval we print them
    xpoints.append(xval)
    ypoints.append(yval)

print("F(x)=",functofx) #print the function to be verrified

mplot.plot(xpoints, ypoints)
mplot.show()

