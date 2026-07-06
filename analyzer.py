import string
import re

COMMON_PASSWORDS = [
    "123456", "password", "123456789", "qwerty", "12345678",
    "111111", "123123", "abc123", "password1"
]

def check_length(password):
    if len(password) < 6:
        return "Too short"
    elif len(password) < 10:
        return "Moderate"
    else:
        return "Strong"

def check_character_types(password):
    types = 0
    if any(c.islower() for c in password):
        types += 1
    if any(c.isupper() for c in password):
        types += 1
    if any(c.isdigit() for c in password):
        types += 1
    if any(c in string.punctuation for c in password):
        types += 1
    return types

def check_common_patterns(password):
    if password.lower() in COMMON_PASSWORDS:
        return True
    if re.search(r'(.)\1{2,}', password):  # repeated characters
        return True
    if re.search(r'123|abc|qwe|password', password.lower()):  # sequences
        return True
    return False

def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)
    if pool == 0:
        return 0
    import math
    return round(len(password) * math.log2(pool), 2)

def rate_password(password):
    if check_common_patterns(password):
        return "Very Weak"
    length_score = check_length(password)
    char_types = check_character_types(password)
    entropy = calculate_entropy(password)

    if length_score == "Too short" or char_types < 2 or entropy < 28:
        return "Weak"
    elif length_score == "Moderate" or char_types < 3 or entropy < 36:
        return "Medium"
    elif length_score == "Strong" and char_types >= 3 and entropy >= 36:
        return "Strong"
    else:
        return "Very Strong"

def recommendations(password):
    tips = []
    if len(password) < 10:
        tips.append("Increase password length to at least 10 characters.")
    if not any(c.isupper() for c in password):
        tips.append("Add uppercase letters.")
    if not any(c.islower() for c in password):
        tips.append("Add lowercase letters.")
    if not any(c.isdigit() for c in password):
        tips.append("Add numbers.")
    if not any(c in string.punctuation for c in password):
        tips.append("Add special characters.")
    if check_common_patterns(password):
        tips.append("Avoid common passwords or repeated sequences.")
    return tips
