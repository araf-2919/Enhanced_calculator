import tkinter as tk
import math
def calculate(operation):
    try:

        if operation =="Add":
            result = float (entry1.get())+float (entry2.get())
        elif operation =="Subtract":
            result = float (entry1.get())-float (entry2.get())
        elif operation =="Multiply":
            result = float (entry1.get())*float (entry2.get())
        elif operation =="Divide":
            num2 = float (entry2.get())
            if num2 == 0:
                result = "Cannot divide by zero!"
            else: 
                result = float(entry1.get())/num2
        elif operation =="Square root":
            result = math.sqrt(float(entry1.get()))
        elif operation =="Power":
            result = float(entry1.get())**float(entry2.get())
        elif operation =="Logarithm":
            result = math.log(float(entry1.get()))
        else:
            result = "Invalid operation!"
        result_label.config(text="Result:"+str(result))
    except ValueError:
        result_label.config(text ="Invalid input!")

root = tk.Tk()
root.title("Enhanced Calculator")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
operations =[
    "Add",
    "Subtract",
    "Multiply",
    "Divide",
    "Square root",
    "Power",
    "Logarithm"
]
row_val = 2
for operation in operations:
    operation_button = tk.Button(root, text=operation, command=lambda op=operation: calculate(op))
    operation_button.grid(row=row_val, column=0, columnspan=2, padx=5, pady=5)
    row_val +=1
result_label = tk.Label(root)
result_label.grid(row = row_val, column = 0, columnspan = 2)

root.mainloop()
