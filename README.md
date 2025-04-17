# 🎯 Python Guess Number Game

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

A fun terminal-based Python game where you guess the number between **1 and 100**. Built for learners, hobbyists, and curious coders. Comes with user login, game history, leaderboard, and player stats — powered by **NumPy** and **MongoDB**! 💥

---

## ✨ Features

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 🎮 Play Game            | Guess a randomly selected number with hints like "Too high" or "Too low".  |
| 🔐 User Authentication | Login system to track users and store data securely.                        |
| 🕓 Game History        | View how many attempts you took in past games.                              |
| 🧠 Player Stats        | See your personal performance with NumPy-based metrics.                     |
| 🏆 Leaderboard         | Compete globally! Sorted by best average attempts.                          |

---

## 📦 Requirements

- Python 3.x
- MongoDB (local or remote)
- `pip install -r requirements.txt`

---

## 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/your-username/python-guess-number-game.git
cd python-guess-number-game

# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt 

```

---

## 🕹️ How to Play

```bash
python main.py
```

1. Enter your username and password to login.
2. Choose from the menu:
- 1. Play Game – Start guessing numbers!
- 2. Show Game History – View your past attempts.
- 3. Show Leaderboard – See global rankings.
- 4. Show Player Stats – See your own performance (Powered by NumPy).
- 5. Exit – Leave the game.
3. Guess numbers until you win! The system will guide you with higher or lower hints.

---
#### 💡 Your attempts are saved and analyzed for performance tracking.

----

## 📊 Sample Stats (Powered by NumPy)
#### 👤 User: player123
#### 🎮 Games Played: 12
#### 📈 Average Attempts: 6.83
#### 🏆 Best Score: 3 attempts
#### 📉 Worst Score: 12 attempts

---
## 💡 Why This Project?

This project was created as part of our Python + NumPy. It’s designed to combine:

✅ Clean, modular Python coding 

✅ Hands-on NumPy usage in a real-world application

✅ Simple MongoDB integration

✅ Game-based learning approach 🎮

Perfect for students, educators, or devs looking to practice Python beyond “Hello World.”
