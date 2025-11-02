# 🎯 Hangman (Tkinter)

A simple and fun **Hangman** game built with **Python** and **Tkinter**. Players guess letters to uncover a hidden word. This repository includes a clean dark-themed GUI and is easy to extend.

---

## 🧩 Features

* 🖥️ Graphical user interface using Tkinter
* 🎲 Random word selection from multiple categories
* 🔤 On-screen alphabet buttons (A–Z)
* 💬 Real-time feedback for correct and wrong guesses
* 🔁 Reset button to start a new game instantly
* ⚙️ Easy to extend with more words or categories

---

## 📦 Requirements

* Python **3.8+**
* Tkinter (usually included with Python)

To verify Tkinter is installed, run:

```bash
python -m tkinter
```

If a small window opens, you’re ready to go! ✅

---

## 🧠 How to Play

1. **Start the Game** — Launch the app; a random word will be chosen automatically.
2. **Guess Letters** — Click the letter buttons (A–Z) to guess letters in the hidden word.
3. **Track Your Progress** —

   * ✅ Correct guesses reveal the letters.
   * ❌ Wrong guesses reduce your remaining lives.
4. **Win or Lose** —

   * 🏆 Guess all letters before your lives reach zero to win.
   * 💀 If you run out of lives, the correct word will be revealed.

---

## 🛠️ Installation & Setup

### 1) Clone the repository

If you have Git installed:

```bash
git clone https://github.com/else/hangman.git
cd hangman
```

Or download a ZIP from GitHub and extract to your preferred folder.

### 2) Run the game

From the project folder run:

```bash
python hangman.py
```

The Hangman window will open — start guessing! 🎯

---

## 📁 Project Structure

```
hangman-tkinter/
├── hangman.py     # Main game code
├── README.md          # Project documentation

```

---

## ✏️ Customization

### Add more words

Edit the `WORDS` list inside `hangman.py` or load words dynamically from `words.txt`:

```python
with open("words.txt") as f:
    WORDS = [line.strip().lower() for line in f if line.strip()]
```

Example default list:

```python
WORDS = ["python", "developer", "keyboard", "umbrella", "zebra", "pizza"]
```

### Change the theme

Adjust colors or fonts in the `create_widgets()` method (or equivalent) in `hangman_gui.py`:

```python
self.root.config(bg="#333")         # Background color
self.word_label.config(fg="cyan")   # Text color
```

---


## 🤝 Contributing

Contributions are welcome!

1. Fork this repository
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature"`
4. Push to your branch: `git push origin feature-name`
5. Open a Pull Request

Please follow the project style and include descriptive commit messages.

---

## 📸 Screenshots

Add screenshots or GIFs to the repo (e.g. `/assets/screenshot.png`) and reference them here:

`![Gameplay screenshot](assets/screenshot.png)`

---

## 👨‍💻 Author

**Your Name**
📧 [charissepriego0140@gmail.com](mailto:charissepriego0140@gmail.com)
🌐 [GitHub Profile](https://github.com/elbse)



*Generated and formatted for a GitHub `README.md`.*
