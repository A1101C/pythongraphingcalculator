from config import *

from syntaxcleaner import cleaner
from syntaxcleaner import simplify
from evaluator import evaluate
from constants import *
from derivatives import derive
from parser import SymbolicParser

import ast


def cCalc(deriveIntegrate, messyFunction):

    function = cleaner(messyFunction) #clean the user input into a clean function

    if deriveIntegrate == "d" or deriveIntegrate == "D":
        from derivatives import derive

        parsedTree = SymbolicParser(function)

        parsedTree.analyze()

        derivativeTree = derive(parsedTree.tree.body)

        solution = ast.unparse(simplify(derivativeTree))

        return solution

