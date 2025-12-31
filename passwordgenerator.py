import string
import secrets

def generate_password(length=16, use_digits=True, use_symbols=True):
    """
    Generates a secure, random password.
    """
    # Define the base character sets
    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''
    
    # Combine all selected characters
    all_characters = letters + digits + symbols
    
    if not all_characters:
        return "Error: No character types selected."

    # Ensure the password contains at least one of each selected type
    # to guarantee complexity
    password = []
    password.append(secrets.choice(string.ascii_lowercase))
    password.append(secrets.choice(string.ascii_uppercase))
    
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))
    
    # Fill the rest of the length with random choices from the full pool
    for _ in range(length - len(password)):
        password.append(secrets.choice(all_characters))
    
    # Shuffle the list to ensure the guaranteed characters aren't always at the start
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def main():
    print("--- 🛡️ Strong Password Generator ---")
    
    try:
        count = int(input("How many passwords do you need? "))
        length = int(input("Enter password length (min 8): "))
        
        if length < 8:
            print("Length too short. Setting to default (12).")
            length = 12
            
        print("\nGenerated Passwords:")
        for i in range(count):
            pwd = generate_password(length)
            print(f"Password {i+1}: {pwd}")
            
    except ValueError:
        print("Invalid input. Please enter numbers for count and length.")

if __name__ == "__main__":
    main()
