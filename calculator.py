#_______________________________________________________Main File_______________________________________________________

#import dependancies
from config import *

#_______________________________________________________Get Input_______________________________________________________

#what kind of calculation are we doing?
calcType = input("What kind of calculation would you like to preform? (S)cientific, (G)raphing, (C)aclulus, (C)AS or (P)hysical Motion:   ")

if calcType == "S" or calcType == "s": #Calls the scientific calculator
    from scientific import sCalc
    sCalc()

if calcType == "G" or calcType == "g": #Calls the graphing calculator
    from graphing import gCalc
    gCalc()


