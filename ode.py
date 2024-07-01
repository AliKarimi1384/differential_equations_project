import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
def create_window_1():
    def submit():
        global ode_input
        ode_input = text_box1.get()
        global y0
        y0 = text_box2.get()
        global y_prime_0
        y_prime_0 = text_box3.get()
        window.destroy()
    window = tk.Tk()
    window.title("ode solver")
    label = tk.Label(window, text="made by Ali Karimi \np(x,y) = 0\ny\" = ddy, y\' = dy")
    label.pack(pady=15)
    label1 = tk.Label(window, text="Enter the p(x,y):")
    label1.pack(pady=0)
    text_box1 = tk.Entry(window)
    text_box1.pack(pady=10)
    label2 = tk.Label(window, text="Enter the y(0)")
    label2.pack(pady=0)
    text_box2 = tk.Entry(window)
    text_box2.pack(pady=10)
    label3 = tk.Label(window, text="Enter the y\'(0)")
    label3.pack(pady=0)
    text_box3 = tk.Entry(window)
    text_box3.pack(pady=10)
    button = tk.Button(window, text="solve", command=lambda: submit())
    button.pack(pady=20)
    window.mainloop()
    return ode_input,y0,y_prime_0
def create_window_2(g,p):
    window = tk.Tk()
    window.title("ode answer")
    label1 = tk.Label(window, text="The general solution to the ODE is:")
    label1.config(font=("Consolas", 12))
    label1.pack(pady=10)
    label2 = tk.Label(window, text=g)
    label2.config(font=("Consolas", 12))
    label2.pack(pady=10)
    label3 = tk.Label(window, text="The particular solution to the ODE is:")
    label3.config(font=("Consolas", 12))
    label3.pack(pady=10)
    label4 = tk.Label(window, text=p)
    label4.config(font=("Consolas", 12))
    label4.pack(pady=10)
    button = tk.Button(window, text="show plot", command=lambda: window.destroy())
    button.pack(pady=20)
    window.mainloop()
def main():
    ode_input,y0,y_prime_0 = create_window_1()
    x = sp.symbols('x')
    y = sp.Function('y')
    ode_input = ode_input.replace("y","y(x)").replace("ddy(x)","Derivative(y(x),x,x)").replace("dy(x)","Derivative(y(x),x)")
    ode = sp.sympify(ode_input)
    y0 = float(y0)
    y_prime_0 = float(y_prime_0)
    result = sp.dsolve(ode, y(x))
    C1, C2 = sp.symbols('C1 C2')
    constants = sp.solve([result.rhs.subs(x, 0) - y0,
                          result.rhs.diff(x).subs(x, 0) - y_prime_0], (C1, C2))
    particular_solution = result.subs(constants)
    create_window_2(sp.pretty(result.rhs),sp.pretty(particular_solution.rhs))
    sol = particular_solution.rhs
    f_sol = sp.lambdify(x, sol, 'numpy')
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_sol(x_vals)
    plt.plot(x_vals, y_vals, label=f'Solution: {particular_solution}')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.title('Plot of the ODE Solution')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()