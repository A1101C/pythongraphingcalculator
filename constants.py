#this dictionary containes defined constants and known values

#if the function has trig values, logs, e, or pi we need to be able to handle those too

from config import *

import math

coTrig = lambda f, x: 1/ f(x)      #this will be used to define our inverse trig functions later
naturalLog = lambda f, x: math.log(x, math.e)   #this defines the naturallog function

constantsDictionary = { #this dictionary containes values for constants and trig functions
    "e": math.e,
    "pi": math.pi,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "csc": lambda x: coTrig(math.sin, x),
    "sec": lambda x: coTrig(math.cos, x),
    "cot": lambda x: coTrig(math.tan, x),
    "log": math.log,
    "ln": lambda x: naturalLog(math.log, x),

        }


