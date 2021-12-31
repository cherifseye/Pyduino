from sympy import *
from sympy.plotting import plot

n = symbols('n')

eq1 = factorial(n) + n 
eq2 = n**n 

p1 = plot(eq1)
p2 = plot(eq2)

p1.append(p2[0])
p1.show()