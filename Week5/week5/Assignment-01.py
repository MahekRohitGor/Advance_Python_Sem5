import hashlib
import logging

logging.basicConfig(level=logging.INFO, filename='user_system.log', format='%(asctime)s - %(levelname)s - %(message)s')

def hashed_password(password):
    hasher = hashlib.sha256()
    hasher.update(password.encode('utf-8'))
    return hasher.hexdigest()

def register_user(username, password):
    h_password = hashed_password(password)
    try:
        with open("user_details.txt", "a") as f:
            f.write(f"{username}:{h_password}\n")
            logging.info("User registered successfully !")
        return True
    except Exception as e:
        logging.error(f"Some error occurred during Registration of user {username}: {e}")  
        return False

def login_user(username, password):
    h_password = hashed_password(password)
    try:
        with open("user_details.txt", "r") as f:
            for line in f:
                stored_username, stored_password = line.strip().split(":") 
                if stored_username == username and stored_password == h_password:
                    logging.info("Login was successful!")
                    return True
            logging.warning("Login failed") 
            return False

    except Exception as e:
        logging.error(f"Some error occurred while logging: {e}")
        return False

if __name__ == "__main__":
    while True:
        print("Enter your choice:\n1. Login\n2. Register\n3. Quit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            uname = input("Enter username: ")
            password = input("Enter password: ")
            if login_user(uname, password):
                print("Login was successful !")
            else:
                print("Login Failed ! Please try again and check login details")

        elif choice == "2":
            uname = input("Enter username: ")
            password = input("Create password: ")
            if register_user(uname, password):
                print("Registration was successful !")
            else:
                print("Registration Failed ! Please try again")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
