
#_______________________________________________________troubleshooting Tools_______________________________________________________
ts = 0 #troubelshooting, 1 is true 0 is false
pv = 1 #print values, 1 makes it print the x and y values to the terminal

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

xcount = input("How many values of x should be calculated? hit enter for the default of 1000.   ")
print(xcount)
if xcount == "":
    xcount = "1000"

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

xmin = float(xmin)
xmax = float(xmax)
xcount= float(xcount)
ymin = float(ymin)
ymax = float(ymax)

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


#_______________________________________________________Preform the Calculations_______________________________________________________

#initalize our first x value and empty list so we can begin to evaluate points
x = xmin #we want to start at our xmin value so for our first point x is xmin
linecounter = 0 #this counter keeps track of how many lines we have due to discontinuities, counting of course starts at 0.
allcoords = {} #this is the master list for groups of coordinates for seperate lines
allcoords["coords0"] = [] #this initializes the first coord list in our master list
imaginaryroots = 0 #this creates the variable for imaginary roots so if we have imaginary roots we know

#printing for troubleshooting
if ts == 1:
    print("before while loop.")
    print(xmin)
    print(xmax)
    print(xcount)

#set up the loop to calculate the y values for our x values
x_values = np.linspace(xmin, xmax, int(xcount))

for x in x_values:
    constants["x"] = x    #since I am telling eval to look at the constants dictionary I need to add x to the constants dictionary

    try: #the try and except is to allow it to continue if we get a /0 error like in 1/x or the inverse trig functions
        y = eval(functofx, {"__builtins__": {}}, constants)   #evalutate function of x and since I  defined constants and various math functions in a dictionary we need to tell it to look in there for those.

        if isinstance(y, complex): #if we get imaginary numbers for y I want to know so I can handle that later
            imaginaryroots = 1

        allcoords[f"coords{linecounter}"].append((x, y)) #put the x value we just used and the y value we just calculated into the coords list for the current line we are on

    except (ZeroDivisionError, ValueError): #if we get a calculation error that means we have a discontinutiy, this exception handles that error so it doesnt crash
        print(f"Skipping x={x}: Undefined at this point") #this prints that there is a discontinutity at this point
        linecounter = linecounter + 1 #this increases the linecounter so our sets of x and y values get stored in seperate arrays to make seperate lines so we see asymptotes when they occur
        allcoords[f"coords{linecounter}"] = [] #this creates a new array for our next lines coords with the new linecounter number

    if pv == 1:
        print(f"{x}, " f{y})
        print (f"{linecounter}")

#printing for troubleshooting
if ts == 1:
    print("after while loop.")
    print(xmin)
    print(xmax)
    print(xcount)
    print(linecounter)

#Print the coordinate pairs, print(coords) just prints them on one line, so to get a nice pair I can use a for loop and define the tuples
#print(coords)
if imaginaryroots == 1:
    print("Values for negative x are complex numbers with an imagniary component. a + bi.")

#_______________________________________________________Put The Values in arrays for matplotlib_______________________________________________________

allxval = {} #Create Master Lists for our coordinate groups
allyval = {}


for n in range(linecounter + 1): #this creates a xval and yval array for every line from the linecounter
    allxval[f"xval{n}"] = [] #initilize the smaller lists inside our master lists
    allyval[f"yval{n}"] = []

    for xval, yval in allcoords[f"coords{n}"]:   #this defines the first value of each index in each numbered list as xval and the second value of each index as yval,

        if isinstance(yval, complex): #this is to replace the j component of the imaginary component of the complex number with i becuase as a physicsist I work with i more than j.
            print(f"{xval}, {yval.real} + {yval.imag}i")

        if pv == 1:  #enable or disable printing to the terminal for troubleshooting.
            print(xval, yval) #prints the ordered pairs (x,y)
            print(linecounter) #prints how many lines we should have plotted
        allxval[f"xval{n}"].append(xval) #append xval list number n to  the master lists
        allyval[f"yval{n}"].append(yval) #append yval list number n to  the master lists

for n in range(linecounter + 1): #this creates a new line for every set of x and y arrays paired by number n
    mplot.plot(allxval[f"xval{n}"], allyval[f"yval{n}"])



print("F(x)=",functofx) #print the function to be verrified

mplot.ylim(ymin, ymax) #forces the y-axis to stay between -10 and 10
mplot.xlim(xmin, xmax) #forces the x axis to show our range of x
mplot.grid(True)
mplot.xlabel("x")
mplot.ylabel("y")

mplot.show() #show us the plotted data

