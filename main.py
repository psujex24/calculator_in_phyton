import tkinter as tk

root = tk.Tk()
root.title("Kalkulator")
root.geometry("380x400")
root.resizable(False, False)

MAX_LENGTH = 15
result = 0
def validate_input(new_value):
    if len(new_value) > MAX_LENGTH:
        return False
    if new_value.isdigit() or result or new_value == "":
        return True
    return False

def click(value):
    current = entry.get()
    if len(current) < MAX_LENGTH:
        entry.insert(tk.END, value)

def set_operation(op):
    global operator
    global first_value
    first_value = entry.get()
    operator = op
    entry.delete(0, tk.END)

def evaluate_expression():
    global operator
    global first_value
    second_value = entry.get()
    if operator and first_value and second_value:
        try:
            first_value = float(first_value)
            second_value = float(second_value)
            global result
            if operator == "+":
                result = first_value + second_value
                print(first_value)
                print(second_value)
                print(result)
            elif operator == "-":
                result = first_value - second_value
            elif operator == "*":
                result = first_value * second_value
            elif operator == "/":
                if second_value == 0:
                    raise ValueError("Dzielenie przez zero")
                result = first_value / second_value
            else:
                result = "Błąd"
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Błąd")
    else:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Błąd")
    operator = None
    first_value = None

def calculate():
    evaluate_expression()

def clear():
    entry.delete(0, tk.END)

vcmd = (root.register(validate_input), '%P')

entry = tk.Entry(root, font=("Arial", 24), justify='right', bd=10, validate="key", validatecommand=vcmd)
entry.pack(padx=5, pady=5)

frame1 = tk.Frame(root)
frame1.pack(padx=5, pady=5)

button_1 = tk.Button(frame1, text="1", width=10, height=4, command=lambda: click("1"))
button_1.pack(side=tk.LEFT, padx=2, pady=2)

button_2 = tk.Button(frame1, text="2", width=10, height=4, command=lambda: click("2"))
button_2.pack(side=tk.LEFT, padx=2, pady=2)

button_3 = tk.Button(frame1, text="3", width=10, height=4, command=lambda: click("3"))
button_3.pack(side=tk.LEFT, padx=2, pady=2)

button_x = tk.Button(frame1, text="X", width=10, height=4, command=lambda: set_operation("*"))
button_x.pack(side=tk.LEFT, padx=2, pady=2)

frame2 = tk.Frame(root)
frame2.pack(padx=2, pady=2)

button_4 = tk.Button(frame2, text="4", width=10, height=4, command=lambda: click("4"))
button_4.pack(side=tk.LEFT, padx=2, pady=2)

button_5 = tk.Button(frame2, text="5", width=10, height=4, command=lambda: click("5"))
button_5.pack(side=tk.LEFT, padx=2, pady=2)

button_6 = tk.Button(frame2, text="6", width=10, height=4, command=lambda: click("6"))
button_6.pack(side=tk.LEFT, padx=2, pady=2)

button_minus = tk.Button(frame2, text="-", width=10, height=4, command=lambda: set_operation("-"))
button_minus.pack(side=tk.LEFT, padx=2, pady=2)

frame3 = tk.Frame(root)
frame3.pack(padx=2, pady=2)

button_7 = tk.Button(frame3, text="7", width=10, height=4, command=lambda: click("7"))
button_7.pack(side=tk.LEFT, padx=2, pady=2)

button_8 = tk.Button(frame3, text="8", width=10, height=4, command=lambda: click("8"))
button_8.pack(side=tk.LEFT, padx=2, pady=2)

button_9 = tk.Button(frame3, text="9", width=10, height=4, command=lambda: click("9"))
button_9.pack(side=tk.LEFT, padx=2, pady=2)

button_plus = tk.Button(frame3, text="+", width=10, height=4, command=lambda: set_operation("+"))
button_plus.pack(side=tk.LEFT, padx=2, pady=2)

frame4 = tk.Frame(root)
frame4.pack(padx=2, pady=2)

button_divide = tk.Button(frame4, text="/", width=10, height=4, command=lambda: set_operation("/"))
button_divide.pack(side=tk.LEFT, padx=2, pady=2)

button_0 = tk.Button(frame4, text="0", width=10, height=4, command=lambda: click("0"))
button_0.pack(side=tk.LEFT, padx=2, pady=2)

button_clear = tk.Button(frame4, text="C", width=10, height=4, command=clear)
button_clear.pack(side=tk.LEFT, padx=2, pady=2)

button_equals = tk.Button(frame4, text="=", width=10, height=4, command=calculate)
button_equals.pack(side=tk.LEFT, padx=2, pady=2)

operator = None
first_value = None

root.mainloop()
