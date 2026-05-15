# pythongraphingcalculator

A modular, symbolic graphing calculator built in Python

Features

Scientific Calculator: Evaluates complex math expressions using a custom parsing engine.

Graphing Engine: Uses matplotlib and numpy to plot functions over a custom domain.

Syntax Cleaning: Automatically converts human syntax (like 2x^3) into Python code (2*(x)**3).

Asymptote Handling: Detects ZeroDivisionError and ValueError to split plots at discontinuities, preventing messy vertical lines.

Complex Number Support: Detects and flags imaginary results.

Full support for single variable symbolic differentiation with a symbolic parser module and custom AST trees in derivitaves.py
    Working with all trig and inverse trig functions as tested
    working with LN and LOG
    
Introduced an AST-based cleaner that simplifies resulting expressions by applying algebraic identities



Project Structure

calculator.py: Main entry point and CLI menu.

graphing.py: Coordinate generation and plotting logic.

scientific.py: Standard expression evaluation.

derivatives.py: The logic trees for symbolic differentiation.

parser.py: AST-based symbolic parsing.

evaluator.py: The core engine.

syntaxcleaner.py: Standardizes user input and hosts the AST simplifier.

testing.py: A stress-test script that hammers the engine with randomized functions.

constants.py & config.py: Global mappings and troubleshooting toggles.

Installation

1. Ensure you have Python 3 installed.

2. Install the required dependencies:
pip install matplotlib numpy

3. Run the main script:
python calculator.py


Known Issues:
Graphing Function doesn't catch every discontinuity. See 1/x for example of it working and cot(x) for example of it missing discontinuities.
Calculus, CAS, and Physical Motion Not Implimented.

Immediate Goals:
Refine Simplifier: Add rules for multiplication by zero and power identities
Impliment Integration
Symbolic Asymptote Detection. 
    Utilize the AST engine to identify denominators and undefined trig arguments to solve for undifined areas to map denominators accurately 
Fix known bugs
Impliment fully vectorized math for faster graphing.
impliment CAS, and Physical Motion Calculators

Long Term Goals:
Build my own evaluator, AST, ect ect... and stop relying on numpy and math modules.
