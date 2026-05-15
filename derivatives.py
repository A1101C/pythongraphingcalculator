
from config import *
from constants import *
from parser import SymbolicParser
import ast

def derive(functionNode):
    #_______________________________________________________define trig function derivitives_______________________________________________________

    if isinstance(functionNode, ast.Call): #handling function calls like sin(x), cos(x)
        funcName = functionNode.func.id # get the name of the function (e.g., 'sin')
        inner = functionNode.args[0] #get the argument inside the parentheses

        innerDeriv = derive(inner)#trig functions have the chain rule where the derivative of f(g(x)) is f'(g(x)) * g'(x)

        if funcName == 'sin': # rule for dx sinx (sin(x))' = cos(x) * (dx x)
            outerDeriv = ast.Call(func=ast.Name(id='cos', ctx=ast.Load()), args=[inner], keywords=[]) #create the outer derivative cos(inner)
            return ast.BinOp(left=outerDeriv, op=ast.Mult(), right=innerDeriv)

        if funcName == 'cos': # rule for cosx (cos(x))' = -sin(x) * (dx x')
            sinCall = ast.Call(func=ast.Name(id='sin', ctx=ast.Load()), args=[inner], keywords=[])
            outerDeriv = ast.BinOp(left=ast.Constant(value=0), op=ast.Sub(), right=sinCall) #create the outer derivative cos(inner)
            return ast.BinOp(left=outerDeriv, op=ast.Mult(), right=innerDeriv)

        if funcName == 'tan': #rule for tan (tan(g))' = sec(g)**2 * g'
            secCall = ast.Call(func=ast.Name(id='sec', ctx=ast.Load()), args=[inner], keywords=[]) # create the sec(inner) call
            outerDeriv = ast.BinOp(left=secCall, op=ast.Pow(), right=ast.Constant(value=2)) # raise sec(inner) to the power of 2 sec(inner)**2
            return ast.BinOp(left=outerDeriv, op=ast.Mult(), right=innerDeriv) # multiply by the inner derivative chain rule

        if funcName == 'sec': # rule (sec(g))' = sec(g) * tan(g) * g'
            secCall = ast.Call(func=ast.Name(id='sec', ctx=ast.Load()), args=[inner], keywords=[]) # create the sec(g) call
            tanCall = ast.Call(func=ast.Name(id='tan', ctx=ast.Load()), args=[inner], keywords=[]) # create the tan(g) cal
            outerDeriv = ast.BinOp(left=secCall, op=ast.Mult(), right=tanCall) # multiply them sec(g) * tan(g)
            return ast.BinOp(left=outerDeriv, op=ast.Mult(), right=innerDeriv) # multiply by innerDeriv for the chain rule

        if funcName == 'csc': # rule (csc(g))' = -csc(g) * cot(g) * g'
            cscCall = ast.Call(func=ast.Name(id='csc', ctx=ast.Load()), args=[inner], keywords=[]) # create the csc(g) and cot(g) calls
            cotCall = ast.Call(func=ast.Name(id='cot', ctx=ast.Load()), args=[inner], keywords=[])
            product = ast.BinOp(left=cscCall, op=ast.Mult(), right=cotCall) # multiply them and make it negative using 0 - (csc * cot)
            outerDeriv = ast.BinOp(left=ast.Constant(value=0), op=ast.Sub(), right=product)
            return ast.BinOp(left=outerDeriv, op=ast.Mult(), right=innerDeriv) # multiply by innerDeriv for the chain rule

        if funcName == 'cot': # rule (cot(g))' = -csc(g)**2 * g'
            cscCall = ast.Call(func=ast.Name(id='csc', ctx=ast.Load()), args=[inner], keywords=[]) # create the csc(g) call and square it
            cscSquared = ast.BinOp(left=cscCall, op=ast.Pow(), right=ast.Constant(value=2))
            outerDeriv = ast.BinOp(left=ast.Constant(value=0), op=ast.Sub(), right=cscSquared) # make it negative
            return ast.BinOp(left=outerDeriv, op=ast.Mult(), right=innerDeriv) # multiply by innerDeriv for the chain rule

        #_______________________________________________________define inverse trig function derivitives_______________________________________________________

        if funcName == 'asin': # rule (asin(g))' = g' / sqrt(1 - g**2)
            g_squared = ast.BinOp(left=inner, op=ast.Pow(), right=ast.Constant(value=2)) # build the inner part of the root 1 - g**2
            inside_root = ast.BinOp(left=ast.Constant(value=1), op=ast.Sub(), right=g_squared)
            denom = ast.Call(func=ast.Name(id='sqrt', ctx=ast.Load()), args=[inside_root], keywords=[]) # build the inner part of the root 1 - g**2
            outerDeriv = ast.BinOp(left=ast.Constant(value=1), op=ast.Div(), right=denom) # create the outer derivative 1 / sqrt(1 - g**2)
            return ast.BinOp(left=outerDeriv, op=ast.Mult(), right=innerDeriv) # multiply by innerDeriv for the chain rule

        if funcName == 'acos': # rule (acos(g))' = -g' / sqrt(1 - g**2)
            g_squared = ast.BinOp(left=inner, op=ast.Pow(), right=ast.Constant(value=2)) # the denominator is the same as asin
            inside_root = ast.BinOp(left=ast.Constant(value=1), op=ast.Sub(), right=g_squared)
            denom = ast.Call(func=ast.Name(id='sqrt', ctx=ast.Load()), args=[inside_root], keywords=[])
            fraction = ast.BinOp(left=ast.Constant(value=1), op=ast.Div(), right=denom) # create the negative outer derivative -1 / sqrt(1 - g**2)
            outerDeriv = ast.BinOp(left=ast.Constant(value=0), op=ast.Sub(), right=fraction)
            return ast.BinOp(left=outerDeriv, op=ast.Mult(), right=innerDeriv)# multiply by innerDeriv for the chain rule

        if funcName == 'atan': # rule (atan(g))' = g' / (1 + g**2)
            g_squared = ast.BinOp(left=inner, op=ast.Pow(), right=ast.Constant(value=2))# build the denominator 1 + g**2
            denom = ast.BinOp(left=ast.Constant(value=1), op=ast.Add(), right=g_squared)
            outerDeriv = ast.BinOp(left=ast.Constant(value=1), op=ast.Div(), right=denom) # create the outer derivative 1 / (1 + g**2)
            return ast.BinOp(left=outerDeriv, op=ast.Mult(), right=innerDeriv) # multiply by innerDeriv for the chain rule

        #_______________________________________________________define log function derivitives_______________________________________________________

        if funcName == 'log': # rule (log_b(g))' = g' / (g * ln(b))
            g = functionNode.args[0]# get the inner function and the base
            b = functionNode.args[1]
            ln_b = ast.Call(func=ast.Name(id='ln', ctx=ast.Load()), args=[b], keywords=[])# create the ln(b) call
            denom = ast.BinOp(left=g, op=ast.Mult(), right=ln_b) # create the denominator: g * ln(b)
            outerDeriv = ast.BinOp(left=ast.Constant(value=1), op=ast.Div(), right=denom) # create the outer derivative: 1 / (g * ln(b)
            return ast.BinOp(left=outerDeriv, op=ast.Mult(), right=innerDeriv) # multiply by innerDeriv for the chain rule

        if funcName == 'ln': # rule (ln(g))' = (1 / g) * g'
            oneNode = ast.Constant(value=1) # create the 1 / g part
            outerDeriv = ast.BinOp(left=oneNode, op=ast.Div(), right=inner)

            return ast.BinOp(left=outerDeriv, op=ast.Mult(), right=innerDeriv) # multiply by the inner derivative for the chain rule



    #_______________________________________________________apply basic calculus rules_______________________________________________________


    if isinstance(functionNode, ast.Constant): #rule 1 the derivative of a constant number is always 0
        return ast.Constant(value=0)


    if isinstance(functionNode, ast.Name): #rule 2 5the derivative of the variable 1x is 1
        if functionNode.id == 'x':
            return ast.Constant(value=1)
        return ast.Constant(value=0) #if it's a variable other than x, treat it as a constant


    if isinstance(functionNode, ast.BinOp): #rule 3 handling operations with binary operators like +, -, *, /


        if isinstance(functionNode.op, ast.Add): # sum rule (f + g)' = f' + g'
            return ast.BinOp(left=derive(functionNode.left), op=ast.Add(), right=derive(functionNode.right)) # recursively derive the left side and the right side

        if isinstance(functionNode.op, ast.Sub): # difference rule (f - g)' = f' - g'
            return ast.BinOp(left=derive(functionNode.left), op=ast.Sub(), right=derive(functionNode.right)) #recursively derive the left side and the right side

        if isinstance(functionNode.op, ast.Mult): #product rule (f * g)' = f' * g + f * g'
            f = functionNode.left #get the left part of the multiplication as f
            g = functionNode.right #get the right part as g
            df = derive(f) # Recursively find the derivative of f
            dg = derive(g) # Recursively find the derivative of g

            term1 = ast.BinOp(left=df, op=ast.Mult(), right=g) #build the first half f' * g
            term2 = ast.BinOp(left=f, op=ast.Mult(), right=dg) #build the second half f * g'

            return ast.BinOp(left=term1, op=ast.Add(), right=term2)  #return the sum (f' * g) + (f * g')

        if isinstance(functionNode.op, ast.Pow): #power rule (x**n)' = n * x**(n-1)
            n = functionNode.right.value # Extract the exponent value (n)
            newExponent = ast.Constant(value=n - 1)# Build the new exponent node (n - 1)
            newPow = ast.BinOp(left=functionNode.left, op=ast.Pow(), right=newExponent) # Construct the new power node: x**(n-1)
            return ast.BinOp(left=ast.Constant(value=n), op=ast.Mult(), right=newPow) # Multiply by the original exponent: n * x**(n-1)


        if isinstance(functionNode.op, ast.Div): #quotient rule (f / g)' = (f'g - fg') / g**2
            f = functionNode.left #get the numerator as f
            g = functionNode.right #get the denominator as g
            df = derive(f) #recursively find the derivative of f
            dg = derive(g) #recursively find the derivative of g

            term1 = ast.BinOp(left=df, op=ast.Mult(), right=g) #build the numerator terms: (f' * g) and (f * g')
            term2 = ast.BinOp(left=f, op=ast.Mult(), right=dg)

            top = ast.BinOp(left=term1, op=ast.Sub(), right=term2) #create the top half of the fraction: (f' * g - f * g')
            bottom = ast.BinOp(left=g, op=ast.Pow(), right=ast.Constant(value=2)) #create the bottom half of the fraction: g**2

            return ast.BinOp(left=top, op=ast.Div(), right=bottom) #return the full division node

        if isinstance(functionNode.op, ast.Pow): #chain rule with powers (g(x)**n)' = n * g(x)**(n-1) * g'(x)
            g = functionNode.left #this is the inner function
            n_node = functionNode.right #this is the exponent
            n = n_node.value

            newExponent = ast.Constant(value=n - 1) #part 1. derive the outer layer or exponent, n * g(x)**(n-1)
            newPow = ast.BinOp(left=g, op=ast.Pow(), right=newExponent)
            outerDeriv = ast.BinOp(left=ast.Constant(value=n), op=ast.Mult(), right=newPow)

            innerDeriv = derive(g) #part2. derive the inner layer g'(x) by recursively deriving the base

            return ast.BinOp(left=outerDeriv, op=ast.Mult(), right=innerDeriv) #part 3 Multiply them together [n * g(x)**(n-1)] * g'(x)

    #if the function encounters an operation it doesn't recognize yet
    raise ValueError("This operator is not supported in the current version of the differentiator.")

