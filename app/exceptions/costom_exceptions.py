class TaskNotFoundException(Exception):
    def __init__(self):
        self.message="task not found"

class UserNotFoundException(Exception):
    def __init__(self):
        self.message="user not found"

class InvalidCredentialsException(Exception):
    def __init__(self):
        self.message = "Invalid credentials"

class EmailAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "Email already registered"

class UsernameAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "Username already taken"