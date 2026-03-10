import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from datetime import datetime
import threading

r = sr.Recognizer()
filename = f"notes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Function to start recording
def start_listening():
    def record():
        with sr.Microphone() as source:
            messagebox.showinfo("Voice Note", "Speak anything... Say 'stop' to end.")
            r.adjust_for_ambient_noise(source)

            while True:
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio).strip().lower()
                    print(f"You said: {text}")

                    if "stop" in text:
                        messagebox.showinfo("Voice Note", "Stopping note taking...")
                        break

                    with open(filename, "a") as f:
                        f.write(text + "\n")

                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError:
                    print("Error with internet connection")
    # Run listening in a separate thread so GUI stays responsive
    threading.Thread(target=record).start()

# GUI setup
root = tk.Tk()
root.title("Voice-to-Text Note Maker")
root.geometry("300x200")

label = tk.Label(root, text="Click to Start Voice Note", font=("Arial", 12))
label.pack(pady=20)

start_button = tk.Button(root, text="Start Recording", command=start_listening, font=("Arial", 12))
start_button.pack(pady=10)

root.mainloop()
