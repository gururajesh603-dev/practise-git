import tkinter as tk
# Create main window
root = tk.Tk()
root.title("Motivation Boost 💪")
root.geometry("400x200")
root.config(bg="black")
# Add a label
label = tk.Label(
    root,
    text="மரகதவல்லி பட்டீஸ்வரர் கருணை",
    font=("Latha", 16, "bold"),
    fg="yellow",
    bg="black"
)
label.pack(expand=True)
# Run the app
root.mainloop()
