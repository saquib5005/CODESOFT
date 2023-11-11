# Import the string and random libraries
import string
import random

# Function to generate a password
def generate_password(length):
    # Define the characters that will be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    # Return the generated password
    return password

# Main function to interact with the user
def main():
    # Infinite loop to keep the program running until the user decides to quit
    while True:
        # Prompt the user to enter the desired length of the password
        print("Enter the desired length of the password:")
        try:
            # Try to convert the user's input to an integer
            password_length = int(input())
            # If the length is less than or equal to 0, print an error message and continue to the next iteration
            if password_length <= 0:
                print("Password length should be a positive number.")
                continue
            # Generate a password of the specified length
            password = generate_password(password_length)
            # Print the generated password
            print(f"Your generated password is: {password}")
        # If the user's input cannot be converted to an integer, print an error message
        except ValueError:
            print("Please enter a valid number for password length.")

        # Ask the user if they want to generate a new password
        print("Do you want to generate a new password? (y/n)")
        # Get the user's response
        reset = input().lower()
        # If the user's response is not 'y', thank the user and break the loop to end the program
        if reset != "y":
            print("Thank You!")
            break

# If this script is being run directly (not being imported), call the main function
if __name__ == "__main__":
    main()
