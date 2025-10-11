import tkinter as tk
from tkinter import messagebox
import time
import random


texts = [
    "Python is an interpreted high-level programming language.",
    "Artificial Intelligence is changing the world rapidly.",
    "Typing fast takes practice and good focus.",
    "You can build desktop apps easily using Tkinter in Python.",
    "Learning to code is one of the best investments you can make."
]


def start_test():
    """Reset everything and start a new test."""
    global start_time, running, target_text
    running = False
    typing_entry.delete("1.0", tk.END)
    result_label.config(text="")
    target_text = random.choice(texts)
    sample_label.config(text=target_text)
    start_time = 0
    typing_entry.focus()


def on_typing(event):
    """Start timer when typing begins."""
    global start_time, running
    if not running:
        start_time = time.time()
        running = True


def calculate_wpm():
    """Check typed text and calculate words per minute."""
    if not running:
        messagebox.showinfo("Typing Test", "Please type something first!")
        return
    
    end_time = time.time()
    elapsed_time = end_time - start_time  # in seconds
    typed_text = typing_entry.get("1.0", tk.END).strip()
    
    # Calculate words per minute
    words = len(typed_text.split())
    wpm = round((words / elapsed_time) * 60)

    # Compare with sample text for accuracy
    correct_words = 0
    for i, word in enumerate(typed_text.split()):
        try:
            if word == target_text.split()[i]:
                correct_words += 1
        except IndexError:
            break

    accuracy = round((correct_words / len(target_text.split())) * 100)

    result_label.config(
        text=f"Speed: {wpm} WPM\nAccuracy: {accuracy}%\nTime: {int(elapsed_time)}s",
        fg="#007acc"
    )



window = tk.Tk()
window.title("Typing Speed Test")
window.config(padx=40, pady=40, bg="#f4f4f4")

title_label = tk.Label(window, text="⌨️ Typing Speed Test", font=("Arial", 24, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=10)

instructions = tk.Label(window, text="Type the text below as fast and accurately as you can:", font=("Arial", 12), bg="#f4f4f4")
instructions.pack()

sample_label = tk.Label(window, text="", wraplength=500, font=("Arial", 14, "italic"), bg="#f4f4f4", fg="#555")
sample_label.pack(pady=20)

typing_entry = tk.Text(window, height=6, width=60, wrap="word", font=("Arial", 14))
typing_entry.pack(pady=10)
typing_entry.bind("<KeyPress>", on_typing)

result_label = tk.Label(window, text="", font=("Arial", 16, "bold"), bg="#f4f4f4")
result_label.pack(pady=10)

buttons_frame = tk.Frame(window, bg="#f4f4f4")
buttons_frame.pack(pady=10)

start_button = tk.Button(buttons_frame, text="🔁 New Test", command=start_test, width=12, bg="#007acc", fg="white", font=("Arial", 12, "bold"))
start_button.grid(row=0, column=0, padx=10)

finish_button = tk.Button(buttons_frame, text="✅ Finish", command=calculate_wpm, width=12, bg="#28a745", fg="white", font=("Arial", 12, "bold"))
finish_button.grid(row=0, column=1, padx=10)

# Initialize
start_test()

window.mainloop()
