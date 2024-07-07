import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random


class NumberGuessGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x300")
        self.master.configure(bg="#f0f0f0")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.master, text="Guess the Number!", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.instruction_label = tk.Label(self.master, text="Enter a number between 1 and 100:", bg="#f0f0f0")
        self.instruction_label.pack(pady=5)

        self.entry = ttk.Entry(self.master, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        self.guess_button = ttk.Button(self.master, text="Guess", command=self.check_guess, style="TButton", width=10)
        self.guess_button.pack(pady=5)

        self.reset_button = ttk.Button(self.master, text="Reset", command=self.reset_game, style="TButton", width=10)
        self.reset_button.pack(pady=5)

        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", font=("Helvetica", 12, "bold"))
        style.map("TButton", background=[("active", "#666666")], foreground=[("active", "white")])

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.attempts += 1

            if user_guess < self.secret_number:
                messagebox.showinfo("Result", "Too low! Try again.")
            elif user_guess > self.secret_number:
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number {self.secret_number}!\n"
                                                        f"It took you {self.attempts} attempts to win.")
                self.reset_game()

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    game = NumberGuessGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
