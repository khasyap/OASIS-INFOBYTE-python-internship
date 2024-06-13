#RANDOM PASSWORD GENERATOR

# Import the random,string module
import random
import string

# Define letters, symbols, and numbers
def generate_password(length, letters=True, numbers=True, symbols=True):
    characters = ""
    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        print("Error: You must select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Python Password Generator!")
    try:
        length = int(input("Enter the password length: "))  # Get user input for password length
        letters = input("Include letters (y/n)? ").lower() == 'y'
        numbers = input("Include numbers (y/n)? ").lower() == 'y'
        symbols = input("Include symbols (y/n)? ").lower() == 'y'

        password = generate_password(length, letters, numbers, symbols) #generate password
        if password:
            print(f"Your random password is: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for password length.")

if __name__ == "__main__":
    main()
