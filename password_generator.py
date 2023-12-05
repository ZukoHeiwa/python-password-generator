# password_generator.py
import string
import random

def generate_password(length=12):
    # Define character sets
    letters = string.ascii_letters
    punctuation = string.punctuation
    digits = string.digits

    # Combine character sets
    all_characters = letters + punctuation + digits

    # Ensure the password is at least length characters long
    length = max(length, 4)

    # Generate a password with at least one character from each set
    password = random.choice(letters) + random.choice(punctuation) + random.choice(digits)

    # Fill the remaining characters randomly
    for _ in range(length - 3):
        password += random.choice(all_characters)

    # Shuffle the password to make it more secure
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password
