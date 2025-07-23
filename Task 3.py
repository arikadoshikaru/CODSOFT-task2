import tkinter as tk
from tkinter import messagebox
import random
import string

# Password banane wali function define kar rahe hain
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        # Agar input galat ho, toh warning pop-up karega
        messagebox.showerror(">_< Invalid Input", "Enter a valid positive number.")
        return

    # Character pool ready kar rahe hain: letters + digits + symbols
    chars = string.ascii_letters + string.digits + string.punctuation
    # Random password generate kar rahe hain
    password = ''.join(random.choices(chars, k=length))
    # Password ko GUI mein show kar rahe hain
    password_var.set(password)
    print(f"Generated Password ({length} characters): {password}")

# GUI setup kar rahe hain
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x280")
root.resizable(False, False)  # Resize disable kar diya

tk.Label(root, text="Random Password Generator", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Enter password length:").pack()

length_entry = tk.Entry(root, justify='center')
length_entry.pack(pady=5)

tk.Button(root, text="Generate", command=generate_password).pack(pady=10)

tk.Label(root, text="Generated Password:").pack()

password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var).pack()

# App start kar rahe hain
root.mainloop()