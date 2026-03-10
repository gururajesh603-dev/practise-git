import tkinter as tk
import random

# List of motivational messages
messages = [
    "🚀 You are UNSTOPPABLE! 🚀",
    "🔥 Keep going, you’re doing GREAT! 🔥",
    "💪 Every step counts — don’t stop now! 💪",
    "🌟 Believe in yourself — You GOT this! 🌟",
    "🏆 Success is yours — Claim it! 🏆",
    "⚡ Push harder than yesterday! ⚡"
]

# Pick a random message each time
random_message = random.choice(messages)

# Create main window
root = tk.Tk()
root.title("Motivation Boost 💪")
root.geometry("450x200")
root.config(bg="black")

# Label with random message
label = tk.Label(
    root,
    text=random_message,
    font=("Helvetica", 16, "bold"),
    fg="yellow",
    bg="black",
    wraplength=400
)
label.pack(expand=True)

# Run the window
root.mainloop()
