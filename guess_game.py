import numpy as np
import db

# Function to play the number guess game
def play_game(username):
    random_number = np.random.randint(1, 101)  # NumPy for random number
    attempts = 0
    win = False

    print("Welcome to the Number Guess Game!")
    print("Guess the number between 1 and 100.")

    while not win:
        try:
            player_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        if player_guess < random_number:
            print("Too low! Try again.")
        elif player_guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            win = True
            db.add_game_history(username, attempts, "win")

# Function to show game history of a user
def show_game_history(username):
    history = db.get_game_history(username)
    if not history:
        print("No game history found.")
    else:
        for game in history:
            print(f"Attempts: {game['attempts']}, Status: {game['status']}")

# Function to show leaderboard
def show_leaderboard():
    leaderboard = db.get_leaderboard()
    if not leaderboard:
        print("No leaderboard data available.")
    else:
        print("🏆 Leaderboard:")
        for rank, player in enumerate(leaderboard, 1):
            print(f"Rank {rank}: {player['_id']} - Avg Attempts: {player['avg_attempts']:.2f}")

# Function to show player stats using NumPy
def show_stats(username):
    history = db.get_game_history(username)
    attempts_list = [game['attempts'] for game in history]

    if not attempts_list:
        print("No stats to display.")
        return

    attempts_array = np.array(attempts_list)
    print(f"\n📊 Stats for {username}")
    print(f"Total Games: {len(attempts_array)}")
    print(f"Average Attempts: {np.mean(attempts_array):.2f}")
    print(f"Best Score (Least Attempts): {np.min(attempts_array)}")
    print(f"Worst Score (Most Attempts): {np.max(attempts_array)}")

# Main function to handle the game
def start_game():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if db.authenticate_user(username, password):
            print(f"Welcome back, {username}!")
            while True:
                print("\nChoose an option:")
                print("1. Play Game")
                print("2. Show Game History")
                print("3. Show Leaderboard")
                print("4. Show Stats")
                print("5. Exit")

                choice = input("Enter your choice (1/2/3/4/5): ")

                if choice == '1':
                    play_game(username)
                elif choice == '2':
                    show_game_history(username)
                elif choice == '3':
                    show_leaderboard()
                elif choice == '4':
                    show_stats(username)
                elif choice == '5':
                    print("Goodbye!")
                    return
                else:
                    print("Invalid choice. Please choose again.")
        else:
            print("Invalid credentials. Please try again.")
