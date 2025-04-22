# Password Strength Checker

A simple yet powerful password strength checker built using **Streamlit** in Python. This tool evaluates the strength of your passwords based on length, character diversity, and entropy. It also provides a strong password suggestion generator and visual feedback in the form of a progress bar.

## Features

- **Password Strength Evaluation**: Evaluates passwords as **Weak**, **Moderate**, or **Strong** based on length, character diversity, and entropy.
- **Entropy Calculation**: Calculates the entropy of the password to measure its unpredictability.
- **Common Password Check**: Alerts users if the password is commonly used and easily guessable.
- **Strong Password Generator**: Suggests a randomly generated strong password if the entered password is weak.
- **Visual Feedback**: Displays a visual entropy meter (progress bar) to show how strong the password is.

## Technologies Used

- **Programming Language**: Python
- **Web Framework**: [Streamlit](https://streamlit.io)
- **Libraries**:
  - `math` (for entropy calculation using log2)
  - `string` and `random` (for generating random passwords)
  - `streamlit` (for building the web app interface)

## Installation

To run this project locally, follow these steps:

### 1. Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/password-strength-checker.git

##Install Dependencies
cd password-strength-checker
pip install -r requirements.txt

##Run the Streamlit Application
streamlit run password_checker.py

##Usage
Usage
Enter a Password: In the input field, type in the password you want to check.

View Strength: The app will evaluate your password and display its strength as Weak, Moderate, or Strong based on length, character diversity, and entropy.

Check Entropy: The app will show the entropy value in bits to measure how unpredictable your password is.

Check Common Passwords: If your password is commonly used, a warning message will appear.

Generate a Strong Password: If your password is weak, the app will suggest a randomly generated strong password.

Example
Here’s an example of how the app evaluates a password:

Input Password: password123

Strength: Weak

Length: 11 characters

Diversity: 7 unique characters

Entropy: 38.36 bits

Password Strength Evaluation Criteria
Weak: Password is too short or lacks diversity (e.g., using only lowercase letters).

Moderate: Password has decent length and some diversity but could be improved.

Strong: Password has a good length, high diversity (uppercase, lowercase, digits, symbols), and high entropy.
