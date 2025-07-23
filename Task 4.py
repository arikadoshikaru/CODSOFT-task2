import tkinter as tk
import random

# Main window ko initialize kar rahe hain
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x450")
root.config()

# Global variables - Score track karne ke liye
user_score = 0
comp_score = 0

# Options jo user aur computer choose kar sakte hain
options = ['Rock', 'Paper', 'Scissors']

def play(user_choice):
    global user_score, comp_score

    # Computer ki random choice generate kar rahe hain
    comp_choice = random.choice(options)

    # Result decide karte hain
    if user_choice == comp_choice:
        result = "¬_¬ It's a Tie!"
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
         (user_choice == 'Paper' and comp_choice == 'Rock') or \
         (user_choice == 'Scissors' and comp_choice == 'Paper'):
        user_score += 1
        result = "^_^ hurrah...You Win!"
    else:
        comp_score += 1
        result = ":) sad...You Lose!"

    # Labels ko update karte hain user aur computer ke choices ke saath
    user_label.config(text=f"Your choice: {user_choice}")
    comp_label.config(text=f"Computer's choice: {comp_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")

    # Terminal pe bhi print karein
    print(f"User chose: {user_choice}")
    print(f"Computer chose: {comp_choice}")
    print(f"Result: {result}")
    print(f"Score -> You: {user_score}, Computer: {comp_score}")
    print("-" * 40)

def reset_game():
    global user_score, comp_score

    # Game ko reset karte hain – scores aur labels ko fresh bana dete hain
    user_score = 0
    comp_score = 0
    user_label.config(text="Your choice: ")
    comp_label.config(text="Computer's choice: ")
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0")

    # Terminal reset info
    print("Game Reset!")
    print("Score -> You: 0, Computer: 0")
    print("=" * 40)

# Game ka UI layout design kar rahe hain
tk.Label(root, text="Choose Rock, Paper, or Scissors", font=('Helvetica', 14)).pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Rock", width=12, command=lambda: play('Rock')).grid(row=0, column=0, padx=10, pady=10)
tk.Button(btn_frame, text="Paper", width=12, command=lambda: play('Paper')).grid(row=0, column=1, padx=10, pady=10)
tk.Button(btn_frame, text="Scissors", width=12, command=lambda: play('Scissors')).grid(row=0, column=2, padx=10, pady=10)

user_label = tk.Label(root, text="Your choice: ", font=('Helvetica', 12))
user_label.pack(pady=5)

comp_label = tk.Label(root, text="Computer's choice: ", font=('Helvetica', 12))
comp_label.pack(pady=5)

result_label = tk.Label(root, text="", font=('Helvetica', 16, 'bold'), fg='blue')
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=('Helvetica', 12))
score_label.pack(pady=5)

tk.Button(root, text="Reset Game", command=reset_game, bg="red", width=15).pack(pady=20)

# Application ko chalu karte hain
root.mainloop()