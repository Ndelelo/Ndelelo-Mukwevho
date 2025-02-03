import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Create display
        self.display_var = tk.StringVar()
        self.display = ttk.Entry(
            root, 
            textvariable=self.display_var, 
            justify="right",
            font=('Arial', 20)
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # Initialize variables
        self.current_number = ""
        self.first_number = None
        self.operation = None
        self.start_new_number = True
        
        # Create buttons
        self.create_buttons()
        
        # Configure grid
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def create_buttons(self):
        button_config = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0, 2)  # Clear button spans 2 columns
        ]
        
        for button in button_config:
            text = button[0]
            row = button[1]
            col = button[2]
            colspan = button[3] if len(button) > 3 else 1
            
            btn = ttk.Button(
                self.root,
                text=text,
                command=lambda t=text: self.button_click(t)
            )
            btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")

    def button_click(self, value):
        if value.isdigit() or value == '.':
            if self.start_new_number:
                self.display_var.set(value)
                self.start_new_number = False
            else:
                self.display_var.set(self.display_var.get() + value)
        
        elif value in ['+', '-', '*', '/']:
            try:
                self.first_number = float(self.display_var.get())
                self.operation = value
                self.start_new_number = True
            except ValueError:
                messagebox.showerror("Error", "Invalid number")
        
        elif value == '=':
            try:
                second_number = float(self.display_var.get())
                if self.operation and self.first_number is not None:
                    result = self.calculate(self.first_number, second_number, self.operation)
                    self.display_var.set(result)
                    self.first_number = None
                    self.operation = None
                    self.start_new_number = True
            except ValueError:
                messagebox.showerror("Error", "Invalid number")
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
        
        elif value == 'C':
            self.display_var.set("")
            self.first_number = None
            self.operation = None
            self.start_new_number = True

    def calculate(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1 * n2
        elif op == '/':
            if n2 == 0:
                raise ZeroDivisionError
            return n1 / n2

def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()