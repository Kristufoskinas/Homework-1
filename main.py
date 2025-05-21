import sympy as sp

# Define symbolic variables
x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)


# Define the function
f = sp.exp(x1-3*x2+3) + sp.exp(3*x2-2*x3-2) + sp.exp(2*x3-x1+2)

def argmin_xi(x):
    df = sp.diff(f, x)
    argmin = sp.solve(sp.Eq(df, 0), x)[0]
    return argmin

x0 = {x1: 4, x2: 3, x3: 2}
print("argmin x1:", float(argmin_xi(x1).subs(x0)))
print("argmin x2:", float(argmin_xi(x2).subs(x0)))
print("argmin x3:", float(argmin_xi(x3).subs(x0)))
