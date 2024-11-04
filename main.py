while True:
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Password must be 8 characters or longer.")
    elif not any(char.isdigit() for char in password):
        print("Password must contain at least one number.")
    elif not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
    elif not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
    elif not any(char in "!@#$%^&*" for char in password):
        print("Password must contain at least one of the special characters: !@#$%^&*")
    else:
        print("Password is valid!")
        break
