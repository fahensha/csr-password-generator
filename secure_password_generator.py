import random
import string

# picks and returns a random lowercase character
def random_lower():
    return random.choice(string.ascii_lowercase)

# picks and returns a random uppercase character
def random_upper():
    return random.choice(string.ascii_uppercase)

# picks and returns a random digit
def random_number():
    return random.choice(string.digits)

# picks and returns the result of a random function
def wildcard():
    return random.choice([random_lower(), random_upper(), random_number()])

# generates a password based on the complexity string, where each 
def generate_complex_password( complex_string ):
    
    password_chars = []

    for c in complex_string:
        if c == "L":
            password_chars.append(random_lower())
        if c == "U":
            password_chars.append(random_upper())
        if c == "N":
            password_chars.append(random_number())
        if c == "W":
            password_chars.append(wildcard())
    
    random.shuffle(password_chars)
    return ''.join(password_chars)

def main():
    print("Welcome to the random password generator!")
    print(f"Your password is: {generate_complex_password('LUWWWWWWWUNLL')}")

if __name__ == "__main__":
    main()
