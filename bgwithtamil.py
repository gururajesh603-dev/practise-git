import tkinter as tk
from PIL import Image, ImageTk
# Create main window
root = tk.Tk()
root.title("Motivation Boost 💪")
root.geometry("1500x1300")
# Load image
img = Image.open("shivasakthi.png")
img = img.resize((1500, 850))
bg_image = ImageTk.PhotoImage(img)
# Add a label for the image (background)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# Add a label
label = tk.Label( root,
    text="மரகதவல்லி பட்டீஸ்வரர் கருணை",
    font=("Latha", 16, "bold"),
    fg="yellow",
    bg="black"
)
label.pack(expand=True)
# Run the app
root.mainloop()
