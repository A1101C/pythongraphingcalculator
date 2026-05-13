# pythongraphingcalculator

A modular Python based calculator capable of handling scientific expressions and generating graphs with support for discontinuities and complex numbers.

Features

Scientific Calculator: Evaluates complex math expressions using a custom parsing engine.

Graphing Engine: Uses matplotlib and numpy to plot functions over a custom domain.

Syntax Cleaning: Automatically converts human syntax (like 2x^3) into Python code (2*(x)**3).

Asymptote Handling: Detects ZeroDivisionError and ValueError to split plots at discontinuities, preventing messy vertical lines.

Complex Number Support: Detects and flags imaginary results.



Project Structure

calculator.py: The main entry point and user menu.

graphing.py: Logic for coordinate generation and plotting.
 
scientific.py: Logic for standard expression evaluation. 

evaluator.py: The core engine that safely evaluates mathematical strings.

constants.py: A dictionary mapping mathematical strings (like sin, pi, ln) to math module functions.

syntaxcleaner.py: Standardizes user input for the evaluator.

config.py: Global toggles for troubleshooting (ts) and value printing (pv).



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
Fix known bugs, detect all discontinuities correctly
Optimize with vectorized math for graphing
impliment CAS, Calculus, and Physical Motion Calculators

Long Term Goals:
Build my own evaluator, AST, ect ect... and stop relying on numpy and math modules.
