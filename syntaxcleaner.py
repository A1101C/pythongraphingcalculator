
from config import *

import math

def cleaner(function):
    #create a loop based on a the number of n numbers that could exist as a co-efficient or really just next to x
    for n in range(10):
        oldsyntax = str(n) + "x"
        newsyntax = str(n) + "*x"
        function = function.replace(oldsyntax, newsyntax) #this should replace any number nx with n*x
        #print(function)

    #we need to replace any trig functions like sinx with sin(x) for the logic in the dictionary to work with the math tool
    #these two replace any x with (x) and ^ with **
    function=function.replace("x","(x)")
    function = function.replace("^", "**")

    return function
