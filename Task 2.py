import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        # User ne jo operation select kiya hai usko le rahe hain
        operation = operation_var.get()

        # Logic apply kar rahe hain based on selected operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("¬_¬ Error", "Division by zero!")
                print("¬_¬ Error: Division by zero attempted.")
                return
            result = num1 / num2
        else:
            # Agar koi galat operation ho toh error popup
            messagebox.showerror("¬_¬ Error", "Invalid operation selected!")
            print("¬_¬ Error: Invalid operation selected.")
            return
        
        # Final result GUI par dikhate hain
        result_label.config(text=f"Result: {result}")

        # Console mein print kar dete hain sab details
        print(f"First Number: {num1}")
        print(f"Second Number: {num2}")
        print(f"Operation: {operation}")
        print(f"Result: {result}")

    except ValueError:
        # Agar user ne numbers ke jagah kuch aur enter kiya ho
        messagebox.showerror("~_~ Error", "Please enter valid numbers!")
        print("~_~ Error: Invalid input entered.")

# GUI setup kar rahe hain
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")
root.resizable(False, False)  #  Resize disable kar diya

# First number input ke liye label aur entry box
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

# Second number input ke liye label aur entry box
tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Operation select karne ka dropdown menu
tk.Label(root, text="Select operation:").pack(pady=5)
operation_var = tk.StringVar(root)
operation_var.set("+")  # Default operation "+"
tk.OptionMenu(root, operation_var, "+", "-", "*", "/").pack()

# Calculate button click hone par result dikhega
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result display ke liye label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Application ko start karte hain
root.mainloop()