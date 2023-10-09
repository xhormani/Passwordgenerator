import random
import string
def generate_password(length):
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    complexity = ""
    while not complexity:
        choice = input("Select complexity (l for lowercase, u for uppercase, d for digits, s for special characters, or any combination thereof): ")
        if 'l' in choice:
            complexity += lower_chars
        if 'u' in choice:
            complexity += upper_chars
        if 'd' in choice:
            complexity += digits
        if 's' in choice:
            complexity += special_chars
    password = ''.join(random.choice(complexity) for _ in range(length))
    return password
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Password length should be greater than 0.")
    else:
        password = generate_password(length)
        print("Generated Password: ", password)
except ValueError:
    print("Invalid input! Please enter a valid integer for password length.")
