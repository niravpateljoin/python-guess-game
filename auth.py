from db import users_collection
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    existing_user = users_collection.find_one({"username": username})
    
    if existing_user:
        return False, "Username already exists."

    hashed_password = hash_password(password)

    users_collection.insert_one({
        "username": username,
        "password": hashed_password
    })

    return True, "User registered successfully."

def login_user(username, password):
    hashed_password = hash_password(password)

    user = users_collection.find_one({
        "username": username,
        "password": hashed_password
    })

    if user:
        return True, "Login successful!"
    else:
        return False, "Invalid username or password."
