import random
from scientific import sCalc
from graphing import gCalc
from calculus import cCalc

def testSuite(testIterations):
    print(f"Test: {testIterations} testIterations\n")

    for i in range(testIterations):
        print(f"--- Test Run {i+1} ---")

        #test scientific
        num1 = random.randint(-100, 100)
        num2 = random.randint(1, 100)
        ops = ['+', '-', '*', '/', '**']
        expr = f"{num1} {random.choice(ops)} {num2}"

        try:
            sci_res = sCalc(expr)
            print(f"[SCI] {expr} = {sci_res}")
        except Exception as e:
            print(f"[SCI ERROR] Failed on {expr}: {e}")

        #test calculus
        funcs = ['sin', 'cos', 'tan', 'ln', 'sec', 'csc', 'cot']
        poly = f"x**{random.randint(1, 5)}"
        calcExpr = f"{random.choice(funcs)}({poly})"

        try:
            #passing d for derivation and the random function
            calc_res = cCalc('d', calcExpr)
            print(f"[CALC] d/dx {calcExpr} = {calc_res}")
        except Exception as e:
            print(f"[CALC ERROR] Failed on {calcExpr}: {e}")

            # test graphing with random Bounds and random fractional
        if i % 2 == 0:
            #randomly choose between a trig function or x
            term = random.choice([f"{random.choice(funcs)}(x)", "x"])
            gfunc = f"x * {term}"
        else:
            # for top and bottom we add x as a possible choice alongside the trig functions
            possible_parts = [str(random.randint(1, 10)), "x", f"{random.choice(funcs)}(x)"]

            top = random.choice(possible_parts)
            bottom = random.choice(possible_parts)

            gfunc = f"({top}) / ({bottom})"

            # generate random bounds
        xmin, xmax = -random.randint(5, 20), random.randint(5, 20)
        ymin, ymax = -random.randint(5, 20), random.randint(5, 20)
        xcount = random.randint(10, 2000)

        print(f"[GRAPH] plotting {gfunc} from {xmin} to {xmax}")
        print("Close the graph window to continue the test.")
        try:
            #this will open a window, you'll have to close it to continue the test
            gCalc(gfunc, xmin, xmax, xcount, ymin, ymax)
        except Exception as e:
            print(f"[GRAPH ERROR] Failed on {gfunc}: {e}")

        print("\n")

if __name__ == "__main__": #this prevents the script from being imported and run in another script as it must be run as main
    testSuite(5) #defines how many tests to run
