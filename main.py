from sympy import symbols, exp, diff, Eq, solve
import numpy as np
from scipy.integrate import quad

# Define symbolic variables
x1, x2, x3 = symbols('x1 x2 x3')

# Define the function
f = exp(x1 - 3*x2 + 3) + exp(3*x2 - 2*x3 - 2) + exp(2*x3 - x1 + 2)

def argmin_xi(x):
    if x == x1:     
        f_x1 = f.subs({x2: 3, x3: 2})
        df_dx1 = diff(f_x1, x1)
        sol_x1 = solve(Eq(df_dx1, 0), x1)
        return [s.evalf() for s in sol_x1]
    elif x == x2:
        f_x2 = f.subs({x1: 4, x3: 2})
        df_dx2 = diff(f_x2, x2)
        sol_x2 = solve(Eq(df_dx2, 0), x2)
        return [s.evalf() for s in sol_x2]
    elif x == x3:
        f_x3 = f.subs({x1: 4, x2: 3})
        df_dx3 = diff(f_x3, x3)
        sol_x3 = solve(Eq(df_dx3, 0), x3)
        return [s.evalf() for s in sol_x3]

print("argmin x1:", argmin_xi(x1))
print("argmin x2:", argmin_xi(x2))
print("argmin x3:", argmin_xi(x3))