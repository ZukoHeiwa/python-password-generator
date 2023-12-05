# main.py
from password_generator import generate_password

def main():
    # Get user input for password length
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid input. Using default password length (12).")
        length = 12

    # Generate password
    password = generate_password(length)
    print("Generated Password:", password)

    # Save the password to the text file (appending to a new line)
    save_to_file(password)

def save_to_file(password):
    with open("generated_password.txt", "a") as file:
        file.write(password + "\n")
    print("Password saved to 'generated_password.txt'.")

if __name__ == "__main__":
    main()