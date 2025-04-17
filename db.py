import pymongo

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["number_guess_game"]
users_collection = db["users"]
game_history_collection = db["game_history"]

# Function to register a user
def register_user(username, password):
    if users_collection.find_one({"username": username}):
        raise "Username already exists."
    users_collection.insert_one({"username": username, "password": password})
    return "User registered successfully."

# Function to authenticate a user
def authenticate_user(username, password):
    user = users_collection.find_one({"username": username, "password": password})
    return user is not None

# Function to add a game to the history
def add_game_history(username, attempts, status):
    game_history_collection.insert_one({"username": username, "attempts": attempts, "status": status})

# Function to get game history of a user
def get_game_history(username):
    return list(game_history_collection.find({"username": username}))

# Function to get leaderboard
def get_leaderboard():
    pipeline = [
        {"$group": {"_id": "$username", "avg_attempts": {"$avg": "$attempts"}}},
        {"$sort": {"avg_attempts": 1}}
    ]
    return list(game_history_collection.aggregate(pipeline))
