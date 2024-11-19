print ("""
==========================================================================

Author : Akshay Sannakki                                Date : 2024-11-06

Email ID : akshaysannakki@gmail.com                 License : MIT License

==========================================================================
# Disclaimer : For educational purposes only.
==========================================================================
""")

import re

def password_complexity_checker(password: str) -> str:
    """
    Checks the complexity of a password and returns its strength.

    Args:
        password (str): The password to evaluate.

    Returns:
        str: Password strength ("Strong", "Good", or "Weak").
    """
    length_score = len(password) >= 8
    uppercase_score = bool(re.search(r'[A-Z]', password))
    lowercase_score = bool(re.search(r'[a-z]', password))
    number_score = bool(re.search(r'[0-9]', password))
    special_char_score = bool(re.search(r'[!-/:-@[-`{-~]', password))

    total_score = length_score + uppercase_score + lowercase_score + number_score + special_char_score

    if total_score == 5:
        return "Strong password"
    elif total_score >= 3:
        return "Good password"
    else:
        return "Weak password"


if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = password_complexity_checker(password)
    print(f"Password strength: {strength}")
