import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from datetime import datetime
import threading

r = sr.Recognizer()
filename = f"notes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"


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

                    # Save to file
                    with open(filename, "a") as f:
                        f.write(text + "\n")

                    # Show in text box
                    text_area.insert(tk.END, text + "\n")
                    text_area.see(tk.END)  # auto-scroll

                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError:
                    print("Error with internet connection")

    threading.Thread(target=record).start()


root = tk.Tk()
root.title("Voice-to-Text Note Maker")
root.geometry("400x300")

label = tk.Label(root, text="Click to Start Voice Note", font=("Arial", 12))
label.pack(pady=10)

start_button = tk.Button(root, text="Start Recording", command=start_listening, font=("Arial", 12))
start_button.pack(pady=10)

text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 10), height=10)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
