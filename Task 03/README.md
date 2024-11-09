# Password Complexity Checker

This Python script checks the strength of a given password based on several security criteria, such as 

length, the presence of uppercase letters, lowercase letters, numbers, and special characters. 

It then provides feedback on whether the password is "Strong," "Good," or "Weak."


## Features
1. Checks if the password meets the minimum length requirement (at least 8 characters).
2. Validates the presence of :
   - Uppercase letters
   - Lowercase letters
   - Numbers
   - Special characters (`!@#$%^&*(),.?":{}|<>`)
3. Provides feedback on password strength :
   - **Strong password** : Meets all criteria.
   - **Good password** : Meets at least 3 of the criteria.
   - **Weak password** : Meets fewer than 3 of the criteria.


## Requirements
- Python 3.x


## Dependencies
This script uses Python's built-in `re` module for regular expression operations, so no additional installations are needed.


## Usage
1. Clone or download this repository to your local machine.
2. Open the terminal or command prompt and navigate to the project directory.
3. Run the script using Python:
   ```bash
   python password_complexity_checker.py
4. Enter a password when prompted to check its strength.


## Code Explanation
#### password_complexity_checker(password)
- Length Check: Verifies if the password has at least 8 characters.
- Uppercase Check: Uses a regular expression to check for uppercase letters (A-Z).
- Lowercase Check: Uses a regular expression to check for lowercase letters (a-z).
- Number Check: Uses a regular expression to check for numbers (0-9).
- Special Character Check: Uses a regular expression to check for special characters like !@#$%^&*(),.?":{}|<>.


#### Feedback Logic
- Strong password: If the password meets all five criteria (length, uppercase, lowercase, number, and special character).
- Good password: If the password meets at least 3 of the criteria.
- Weak password: If the password meets fewer than 3 of the criteria.


## License
This project is open-source and available under the MIT License.
