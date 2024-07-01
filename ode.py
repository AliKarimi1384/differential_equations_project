#Ali Karimi-ode-farabi
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

def create_input_window():
    def submit():
        global ode_input
        ode_input = text_box1.get()
        global y0
        y0 = text_box2.get()
        global y_prime_0
        y_prime_0 = text_box3.get()
        window.destroy()

    window = tk.Tk()
    window.title("ODE Solver")

    label = tk.Label(window, text="Made by Ali Karimi \np(x,y) = 0\ny\" = ddy, y' = dy")
    label.pack(pady=15)

    label1 = tk.Label(window, text="Enter the p(x,y):")
    label1.pack(pady=0)
    text_box1 = tk.Entry(window)
    text_box1.pack(pady=10)

    label2 = tk.Label(window, text="Enter the y(0):")
    label2.pack(pady=0)
    text_box2 = tk.Entry(window)
    text_box2.pack(pady=10)

    label3 = tk.Label(window, text="Enter the y'(0):")
    label3.pack(pady=0)
    text_box3 = tk.Entry(window)
    text_box3.pack(pady=10)

    button = tk.Button(window, text="Solve", command=submit)
    button.pack(pady=20)

    window.mainloop()
    return ode_input, y0, y_prime_0

def create_output_window(general_solution, particular_solution):
    window = tk.Tk()
    window.title("ODE Answer")

    label1 = tk.Label(window, text="The general solution to the ODE is:")
    label1.config(font=("Consolas", 12))
    label1.pack(pady=10)

    label2 = tk.Label(window, text=general_solution)
    label2.config(font=("Consolas", 12))
    label2.pack(pady=10)

    label3 = tk.Label(window, text="The particular solution to the ODE is:")
    label3.config(font=("Consolas", 12))
    label3.pack(pady=10)

    label4 = tk.Label(window, text=particular_solution)
    label4.config(font=("Consolas", 12))
    label4.pack(pady=10)

    button = tk.Button(window, text="Show Plot", command=window.destroy)
    button.pack(pady=20)

    window.mainloop()

def main():
    ode_input, y0, y_prime_0 = create_input_window()

    x = sp.symbols('x')
    y = sp.Function('y')

    ode_input = ode_input.replace("y", "y(x)").replace("ddy(x)", "Derivative(y(x), x, x)").replace("dy(x)", "Derivative(y(x), x)")
    ode = sp.sympify(ode_input)

    y0 = float(y0)
    y_prime_0 = float(y_prime_0)
    general_solution = sp.dsolve(ode, y(x))

    constants = [symbol for symbol in general_solution.free_symbols if symbol != x]

    initial_conditions = [general_solution.rhs.subs(x, 0) - y0]
    if len(constants) > 1:
        initial_conditions.append(general_solution.rhs.diff(x).subs(x, 0) - y_prime_0)

    constants_values = sp.solve(initial_conditions, constants)

    particular_solution = general_solution.subs(constants_values)

    create_output_window(sp.pretty(general_solution.rhs), sp.pretty(particular_solution.rhs))

    sol = particular_solution.rhs
    f_sol = sp.lambdify(x, sol, 'numpy')

    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_sol(x_vals)

    plt.plot(x_vals, y_vals)
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.title('Plot of the ODE Solution')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()