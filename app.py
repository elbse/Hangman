import tkinter as tk
import random

# --- Game setup ---
WORDS = [
    # Programming / Tech
    "python", "developer", "variable", "function", "compiler", "algorithm", "debugger", "keyboard",
    "internet", "software", "hardware", "database", "interface", "framework", "computer", "hangman",

    # Animals
    "elephant", "giraffe", "kangaroo", "alligator", "tiger", "penguin", "dolphin", "chameleon",
    "rhinoceros", "flamingo", "chimpanzee", "porcupine", "zebra", "koala",

    # Countries
    "australia", "brazil", "canada", "denmark", "egypt", "france", "germany", "hungary",
    "india", "japan", "kenya", "mexico", "nepal", "portugal", "sweden", "turkey", "vietnam",

    # Food
    "pizza", "sandwich", "pancake", "spaghetti", "hamburger", "sushi", "omelette", "chocolate",
    "cupcake", "biscuit", "lasagna", "taco", "doughnut",

    # Random nouns
    "rainbow", "mountain", "adventure", "journey", "umbrella", "notebook", "fireworks", "sunshine",
    "diamond", "whisper", "clock", "island", "forest", "river", "castle", "camera", "airplane"
]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x500")
        self.root.config(bg="#222")

        self.word = ""
        self.guessed_letters = set()
        self.lives = 6

        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="🎯 Hangman", font=("Arial", 20, "bold"), bg="#222", fg="white")
        self.title_label.pack(pady=10)

        self.word_label = tk.Label(self.root, text="", font=("Consolas", 24), bg="#222", fg="yellow")
        self.word_label.pack(pady=20)

        self.status_label = tk.Label(self.root, text="", font=("Arial", 14), bg="#222", fg="white")
        self.status_label.pack(pady=10)

        # Letter buttons
        self.buttons_frame = tk.Frame(self.root, bg="#222")
        self.buttons_frame.pack()

        self.buttons = {}
        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            btn = tk.Button(
                self.buttons_frame,
                text=letter,
                width=4,
                height=2,
                command=lambda l=letter: self.guess_letter(l.lower()),
                bg="#444", fg="white"
            )
            btn.grid(row=i//7, column=i%7, padx=3, pady=3)
            self.buttons[letter] = btn

        # Reset button
        self.reset_button = tk.Button(self.root, text="🔁 Reset", command=self.reset_game, bg="#555", fg="white", font=("Arial", 12))
        self.reset_button.pack(pady=20)

    def reset_game(self):
        self.word = random.choice(WORDS)
        self.guessed_letters = set()
        self.lives = 6
        self.update_display()
        self.status_label.config(text=f"Lives: {self.lives}")
        for btn in self.buttons.values():
            btn.config(state=tk.NORMAL, bg="#444")

    def guess_letter(self, letter):
        self.guessed_letters.add(letter)
        self.buttons[letter.upper()].config(state=tk.DISABLED, bg="#666")

        if letter not in self.word:
            self.lives -= 1
            self.status_label.config(text=f"❌ Wrong! Lives: {self.lives}")
        else:
            self.status_label.config(text=f"✅ Correct! Lives: {self.lives}")

        self.update_display()

        if all(l in self.guessed_letters for l in self.word):
            self.status_label.config(text="🎉 You won!")
            self.disable_all_buttons()
        elif self.lives == 0:
            self.status_label.config(text=f"💀 You lost! Word was: {self.word}")
            self.disable_all_buttons()

    def update_display(self):
        display = " ".join([l.upper() if l in self.guessed_letters else "_" for l in self.word])
        self.word_label.config(text=display)

    def disable_all_buttons(self):
        for btn in self.buttons.values():
            btn.config(state=tk.DISABLED)

# --- Run app ---
root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
