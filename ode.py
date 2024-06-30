import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
X = sp.symbols('x')
Y = sp.symbols('y')
d = sp.simplify(input(":"))
f = sp.lambdify([X,Y],d)
x = np.linspace(-5,5,1000)
y = list(map(f,x))
plt.plot(x,y)
plt.show()