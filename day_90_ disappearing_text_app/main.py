import tkinter as tk
from tkinter import messagebox

# just 5 seconds of no typing and all text disappears
TIME_LIMIT = 5  

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Most Dangerous Writing App")
        self.root.geometry("700x500")
        self.root.config(bg="#f8f9fa")

        self.label = tk.Label(
            root,
            text="Keep typing... Stop for 5 seconds and all is lost!",
            font=("Helvetica", 14),
            bg="#f8f9fa",
            fg="#333"
        )
        self.label.pack(pady=20)

        # Text box for writing
        self.text = tk.Text(
            root,
            wrap="word",
            font=("Consolas", 14),
            width=70,
            height=20,
            bd=2,
            relief="groove"
        )
        self.text.pack(padx=20, pady=10)

        # Restart button
        self.restart_button = tk.Button(
            root,
            text="Restart",
            command=self.reset_text,
            bg="#dc3545",
            fg="white",
            font=("Helvetica", 12, "bold"),
            relief="raised"
        )
        self.restart_button.pack(pady=10)

        # Timer control
        self.timer_id = None
        self.root.bind("<Key>", self.reset_timer)

        # Start the timer as soon as app starts
        self.start_timer()

    def start_timer(self):
        """Start or restart the timer countdown"""
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.timer_id = self.root.after(TIME_LIMIT * 1000, self.delete_text)

    def reset_timer(self, event=None):
        """Reset timer whenever the user types something"""
        self.start_timer()

    def delete_text(self):
        """Triggered when time runs out"""
        self.text.delete("1.0", tk.END)
        messagebox.showwarning("Time's Up!", "You stopped typing! All progress has been deleted.")
        self.start_timer()  # restart the timer after clearing

    def reset_text(self):
        """Manually clear everything"""
        self.text.delete("1.0", tk.END)
        self.start_timer()


if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
