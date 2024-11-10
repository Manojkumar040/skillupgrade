import re
import math
from collections import Counter

# List of common weak passwords (for demonstration)
COMMON_WEAK_PASSWORDS = [
    "123456", "password", "123456789", "12345", "1234", "qwerty", "abc123", "password1", "letmein"
]

# Function to check password strength based on various criteria
def check_password_strength(password):
    analysis = {}
    
    # Minimum Length Requirement
    min_length = 8
    analysis['length'] = len(password) >= min_length
    
    # Character Variety Checks
    analysis['has_upper'] = any(char.isupper() for char in password)
    analysis['has_lower'] = any(char.islower() for char in password)
    analysis['has_digit'] = any(char.isdigit() for char in password)
    analysis['has_special'] = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Common Weak Password Check
    analysis['is_common'] = password in COMMON_WEAK_PASSWORDS
    
    # Calculate Entropy of the password
    analysis['entropy'] = calculate_entropy(password)
    
    # Detect patterns like consecutive letters or numbers
    analysis['has_repeated_patterns'] = has_repeated_patterns(password)
    
    return analysis

# Function to calculate entropy of a password
def calculate_entropy(password):
    # Calculate the frequency of characters in the password
    freq = Counter(password)
    password_length = len(password)
    entropy = 0.0
    
    # Shannon entropy formula
    for count in freq.values():
        probability = count / password_length
        entropy -= probability * math.log2(probability)
    
    return entropy

# Function to check for repeated patterns like "abc", "123"
def has_repeated_patterns(password):
    common_patterns = [
        "123", "abc", "password", "qwerty", "iloveyou", "letmein", "welcome"
    ]
    return any(pattern in password.lower() for pattern in common_patterns)

# Function to generate recommendations based on password analysis
def generate_recommendations(analysis):
    recommendations = []
    
    # Check for each analysis point and provide feedback
    if not analysis['length']:
        recommendations.append("Password should be at least 8 characters long.")
    
    if not analysis['has_upper']:
        recommendations.append("Password should contain at least one uppercase letter.")
    
    if not analysis['has_lower']:
        recommendations.append("Password should contain at least one lowercase letter.")
    
    if not analysis['has_digit']:
        recommendations.append("Password should contain at least one digit.")
    
    if not analysis['has_special']:
        recommendations.append("Password should contain at least one special character.")
    
    if analysis['is_common']:
        recommendations.append("Avoid using common passwords. Choose a more unique password.")
    
    if analysis['has_repeated_patterns']:
        recommendations.append("Avoid using common patterns or sequences like '123' or 'qwerty'.")
    
    if analysis['entropy'] < 3:
        recommendations.append("Password entropy is low. Consider using a longer or more random password.")
    
    return recommendations

# Main function to prompt user input and analyze password
def analyze_user_password():
    # Prompt user to enter a password
    password = input("Enter a password to analyze: ").strip()

    # Perform password strength analysis
    analysis = check_password_strength(password)

    # Output the analysis results
    print(f"\nAnalysis for password: {password}")
    for key, value in analysis.items():
        print(f"{key}: {value}")

    # Generate and display recommendations
    recommendations = generate_recommendations(analysis)
    print("\nRecommendations:")
    for rec in recommendations:
        print(f"- {rec}")

# Run the analysis
if __name__ == "__main__":
    analyze_user_password()
