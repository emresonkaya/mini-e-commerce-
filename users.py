from storage import JsonHandler

class UserManager:
    #for user registration login and session management
    def __init__(self):
        self.filename = "users.json"
        self.users = JsonHandler.load_data(self.filename)
        self.current_user = None
        #last part tracks the currently  logged user

    def register(self, username, password):
        #register a new user if walidation pass
        self.users = JsonHandler.load_data(self.filename)
        #reload data to be sure we got the latest list
        #next we will check if username allready exists
        for user in self.users:
            if user['username'] == username:
                print("Error: Username already exists.")
                return False
        #check password length min 6 characters
        if len(password) < 6:
            print("Error: Password must be at least 6 characters long.")
            return False
        #create new user dictionary 
        new_user = {
            "username": username,
            "password": password
        }

        # 5. Save to file
        self.users.append(new_user)
        if JsonHandler.save_data(self.filename, self.users):
            print("Registration successful!")
            return True
        else:
            print("Error: Could not save user.")
            return False

    def login(self, username, password):
        #authenticate a user sets self current user if succesfull
        self.users = JsonHandler.load_data(self.filename)

        for user in self.users:
            if user['username'] == username and user['password'] == password:
                self.current_user = user
                print(f"Login successful! Welcome, {username}.")
                return True
        
        print("Login failed: Invalid username or password.")
        return False

    def logout(self):
        #logs out the current user
        if self.current_user:
            print(f"Goodbye, {self.current_user['username']}!")
            self.current_user = None
        else:
            print("No user is currently logged in.")
            
    def is_logged_in(self):
        #helps and checks to user is logged in returns true if logged in false otherwise

        return self.current_user is not None