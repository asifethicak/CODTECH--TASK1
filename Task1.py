import re

def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return "Password should be at least 8 characters long."

    # Check for both uppercase and lowercase characters
    if not re.search(r"[a-z]", password) or not re.search(r"[A-Z]", password):
        return "Password should contain both uppercase and lowercase characters."

    # Check for digits
    if not re.search(r"\d", password):
        return "Password should contain at least one digit."

    # Check for special characters
    if not re.search(r"[ !\"#$%&'()*+,-./[\\\]^_`{|}~]", password):
        return "Password should contain at least one special character."

    # Check uniqueness
    if len(set(password)) < 0.75 * len(password):
        return "Password should have a good mix of characters to enhance uniqueness."

    return "Password is strong."

# Example usage:
password = input("Enter your password: ")
strength = check_password_strength(password)
print(strength) 


