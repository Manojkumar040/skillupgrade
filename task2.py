import hashlib
import itertools

# Define the password hash to crack
password_hash = '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'

# Define the wordlist to use for cracking
wordlist = ['password123', 'qwerty', 'letmein']

# Create a hash object
hash_object = hashlib.md5()

# Crack the password using the wordlist
for password in wordlist:
    # Update the hash object with the password
    hash_object.update(password.encode('utf-8'))
    # Get the password hash
    cracked_password_hash = hash_object.hexdigest()
    # Check if the cracked password hash matches the target password hash
    if cracked_password_hash == password_hash:
        print(f"Password cracked: {password}")
        break
else:
    print("Password not cracked")

# Conduct password strength analysis
def password_strength_analysis(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return "Weak"
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Weak"
    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return "Weak"
    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return "Weak"
    # Check if the password contains at least one special character
    if not any(not char.isalnum() for char in password):
        return "Weak"
    return "Strong"

# Test the password strength analysis function
password = 'Password123!'
print(password_strength_analysis(password))
