from scipy import misc
import math


def f(x): return 3*x**3 + 4*x**2 + 4*x + 1
def df(c): return misc.derivative(f, c)


def GenIter(x0):
    return x0-0.25*(3*x0**3 + 4*x0**2 + 4*x0 + 1)


x0 = -0.25
max = 100
tol = 0.000120
print("General Iteration Method \n")
for i in range(max):
    x1 = GenIter(x0)
    if df(x0) != 0:
        test = True
        print(
            f"Iteration {i+1}: \nInitial approximation is {round(x0,6)} \nx{i} = {round(x0,6)}\tx{i+1} = {round(x1,6)}\n")
        if abs(x1-x0) < tol:
            print(
                f"Since |x{i+1}-x{i}| = {abs(round(x1-x0,6))}<{tol}, we have reached the stopping condition \n")
            break
        else:
            pass
        x0 = x1
        if abs(f(x1)) < tol:
            print(
                f"Since |f({round(x1,6)})| = {abs(round(f(x1),6))}<{tol}, we have reached the stopping condition \n")
            break
        else:
            pass
    else:
        print(f"f'(x{i+1}) = 0, iteration is stopped. last root is {f(x1)}")
        test = False
        break

if test != False:
    print(
        f"The value of the root is {round(x1,6)} and the number of iterations required is {i+1}")
