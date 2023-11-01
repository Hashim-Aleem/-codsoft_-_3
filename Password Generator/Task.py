6import random
import string

def generate_password(length):
    """Generate a random password of specified length"""
    # Define the character set to use for password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choices()
    password = ''.join(random.choices(characters, k=length))

    return password

# Prompt the user to specify the desired length of the password
length = int(input("Enter the desired length of the password: "))

# Generate the password
password = generate_password(length)

# Display the password
print("Generated password:", password)