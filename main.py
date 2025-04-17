import db
import guess_game

# Function to handle user login
print("Welcome to the Number Guess Game!")

def login():
    guess_game.start_game()

def register():
    username = input('please enter username:')
    password = input('please enter password:')

    try:
        db.register_user(username=username, password=password)
        print('successfully register, please login to play game')
        print('\n')
        print('-----------------------------------------------------')
        login()
    except Exception:
        print('User already exist in system please choose different username')
        print('\n')
        print('-----------------------------------------------------')
        register()

def main():
    print("\nChoose an option:")
    print("1. Login")
    print("2. Register")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        login()
    elif choice == '2':
        register()
    else:
        print("Invalid choice. Please choose again.")
        main()

if __name__ == "__main__":
    main()
