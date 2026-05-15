
from config import *
import math
import ast

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

def simplify(node):
    if isinstance(node, ast.BinOp): # if it's a binary operation like + - * /
        left = simplify(node.left) # first, recursively simplify the left and right sides
        right = simplify(node.right)

        if isinstance(node.op, ast.Add): # check for addition identities
            #adding 0 does nothing and can be removed
            if isinstance(left, ast.Constant) and left.value == 0: # if left is 0 just return the right side
                return right
            if isinstance(right, ast.Constant) and right.value == 0: # if right is 0 just return the left side
                return left

        if isinstance(node.op, ast.Mult): #multipling by one can be simplified away
            if isinstance(left, ast.Constant) and left.value == 1: # if left is 1 just return the right side
                return right
            if isinstance(right, ast.Constant) and right.value == 1: # if right is 1 just return the left side
                return left

        return ast.BinOp(left=left, op=node.op, right=right) #if no identity was matched, return the node with simplified children
    return node #fallback for constants, names, and calls
