import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Define character pools
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = letters + digits + symbols

    # Ensure password has at least one letter, digit, and symbol
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_chars, k=length - 3)

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Prompt user for input
try:
    user_length = int(input("Enter desired password length: "))
    password = generate_password(user_length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
