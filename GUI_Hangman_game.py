import tkinter as tk
import random

# Load words
with open("words.txt", "r") as f:
    words = f.read().splitlines()

# Function to start/reset game
def new_game():
    global word, attempts
    
    word = random.choice(words)
    attempts = 3
    
    # Reset UI
    attempts_label.config(text=f"Attempts: {attempts}")
    result_label.config(text="")
    hint_label.config(text="")
    entry.delete(0, tk.END)
    submit_btn.config(state="normal")
    
    update_word_display()

# Show word format like A _ _ _ Z
def update_word_display():
    middle = " _ " * (len(word) - 2)
    display = f"{word[0]} {middle} {word[-1]}"
    word_label.config(text=display)

# Check guess
def check_guess():
    global attempts
    
    user_input = entry.get().strip()
    
    if len(user_input) != len(word) - 2:
        result_label.config(text="⚠ Enter correct number of letters!", fg="orange")
        return
    
    final_word = word[0] + user_input + word[-1]
    
    if final_word == word:
        result_label.config(text=f"🎉 CORRECT! Word: {word}", fg="#00ff88")
        submit_btn.config(state="disabled")
    else:
        attempts -= 1
        attempts_label.config(text=f"Attempts: {attempts}")
        result_label.config(text="❌ Wrong Guess!", fg="red")
        
        if attempts == 1:
            hint_label.config(text=f"💡 Hint: 2nd letter is '{word[1]}'")
        
        if attempts == 0:
            result_label.config(text=f"💀 Game Over! Word was '{word}'", fg="white")
            submit_btn.config(state="disabled")

# ---------------- UI ---------------- #

root = tk.Tk()
root.title("🔥 Word Guess Game")
root.geometry("500x400")
root.config(bg="#1e1e2f")

# Title
tk.Label(root, text="WORD GUESS GAME", 
         font=("Arial", 20, "bold"),
         fg="#00ffcc", bg="#1e1e2f").pack(pady=15)

# Word display
word_label = tk.Label(root, text="", 
                      font=("Courier", 22, "bold"),
                      fg="white", bg="#1e1e2f")
word_label.pack(pady=10)

# Input box
entry = tk.Entry(root, font=("Arial", 16), justify="center",
                 bg="#2b2b3c", fg="white", insertbackground="white")
entry.pack(pady=10)

# Buttons frame
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

submit_btn = tk.Button(btn_frame, text="Submit", command=check_guess,
                       bg="#00cc66", fg="black", font=("Arial", 12, "bold"),
                       width=10)
submit_btn.grid(row=0, column=0, padx=10)

restart_btn = tk.Button(btn_frame, text="Restart", command=new_game,
                        bg="#3399ff", fg="white", font=("Arial", 12, "bold"),
                        width=10)
restart_btn.grid(row=0, column=1, padx=10)

# Attempts
attempts_label = tk.Label(root, text="", 
                          font=("Arial", 12),
                          fg="#ffcc00", bg="#1e1e2f")
attempts_label.pack()

# Hint
hint_label = tk.Label(root, text="", 
                      font=("Arial", 12),
                      fg="#66ccff", bg="#1e1e2f")
hint_label.pack()

# Result
result_label = tk.Label(root, text="", 
                        font=("Arial", 14, "bold"),
                        bg="#1e1e2f")
result_label.pack(pady=15)

# Start first game
new_game()

root.mainloop()