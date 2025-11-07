# password_checker.py
import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        strength += 1
        feedback.append("Length: Strong (12+ chars)")
    elif len(password) >= 8:
        strength += 0.5
        feedback.append("Length: Medium (8-11 chars)")
    else:
        feedback.append("Length: Weak (<8 chars) - Use longer passwords!")
    
    # Uppercase
    if re.search(r'[A-Z]', password):
        strength += 1
        feedback.append("Uppercase: Present")
    else:
        feedback.append("Uppercase: Missing - Add at least one!")
    
    # Lowercase
    if re.search(r'[a-z]', password):
        strength += 1
        feedback.append("Lowercase: Present")
    else:
        feedback.append("Lowercase: Missing - Add at least one!")
    
    # Numbers
    if re.search(r'\d', password):
        strength += 1
        feedback.append("Numbers: Present")
    else:
        feedback.append("Numbers: Missing - Include digits!")
    
    # Special chars
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
        feedback.append("Special chars: Present")
    else:
        feedback.append("Special chars: Missing - Add symbols!")
    
    # Rating
    if strength >= 4.5:
        rating = "Strong"
        tip = "Excellent! Enable 2FA and avoid reusing this password."
    elif strength >= 3:
        rating = "Medium"
        tip = "Good start, but beef it up. Change every 90 days."
    else:
        rating = "Weak"
        tip = "At risk! Use a password manager like Bitwarden."
    
    return rating, feedback, tip

if __name__ == "__main__":
    pwd = input("Enter your password (it won't be saved): ")
    rating, feedback, tip = check_password_strength(pwd)
    print(f"\nPassword Strength: {rating}")
    print("Analysis:")
    for item in feedback:
        print(f"  - {item}")
    print(f"\nSecurity Tip: {tip}")