import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error):
        print("Strong password.")
    else:
        print("Weak password. Ensure it has:")
        if length_error: print("- At least 8 characters")
        if digit_error: print("- At least one number")
        if uppercase_error: print("- At least one uppercase letter")
        if lowercase_error: print("- At least one lowercase letter")
        if symbol_error: print("- At least one special symbol")

password = input("Enter your password: ")
check_password_strength(password)
