import ast

class SymbolicParser:
    def __init__(self, expression): #ast.parse turns the string into a tree structure
        self.tree = ast.parse(expression, mode='eval')

    def analyze(self):#goes down each branch for every part of the function to create the tree

        for node in ast.walk(self.tree):
            if isinstance(node, ast.BinOp): #binop is binary operator, like +, *, **
                print(f"Operation: {type(node.op).__name__}")

            elif isinstance(node, ast.Constant): #this grabs the constant number
                print(f"Constant Value: {node.value}")

            elif isinstance(node, ast.Name): #this grabs the variable which should be X
                print(f"Variable: {node.id}")

