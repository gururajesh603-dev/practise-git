import tkinter as tk
# Create main window
root = tk.Tk()
root.title("Motivation Boost 💪")
root.geometry("400x200")
root.config(bg="black")
# Add a label
label = tk.Label(
    root,
    text="🚀 You are UNSTOPPABLE! 🚀",
    font=("Helvetica", 16, "bold"),
    fg="yellow",
    bg="black"
)
label.pack(expand=True)
# Run the app
root.mainloop()
