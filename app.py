import streamlit as st
import math
import random
import string

# Function to calculate entropy based on character diversity
def password_entropy(password):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`"
    char_set = set()

    if any(c in lower for c in password):
        char_set.update(lower)
    if any(c in upper for c in password):
        char_set.update(upper)
    if any(c in digits for c in password):
        char_set.update(digits)
    if any(c in special for c in password):
        char_set.update(special)

    char_set_size = len(char_set)
    if char_set_size > 1:
        entropy = len(password) * math.log2(char_set_size)
    else:
        entropy = 0
    return entropy

# Common password list
COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345", "qwerty",
    "abc123", "password1", "111111", "letmein",
    "welcome", "password123"
}

# Check if password is common
def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS

# Evaluate strength based on length, diversity, entropy
def evaluate_strength(password):
    length = len(password)
    entropy = password_entropy(password)
    diversity = len(set(password))

    if length < 6:
        length_score = 0
    elif 6 <= length <= 8:
        length_score = 1
    else:
        length_score = 2

    if diversity <= 6:
        diversity_score = 0
    elif diversity <= 12:
        diversity_score = 1
    else:
        diversity_score = 2

    if entropy < 32:
        entropy_score = 0
    elif 32 <= entropy <= 64:
        entropy_score = 1
    else:
        entropy_score = 2

    total_score = length_score + diversity_score + entropy_score

    if total_score <= 2:
        return "Weak"
    elif total_score <= 4:
        return "Moderate"
    else:
        return "Strong"

# Generate a strong random password
def generate_strong_password(length=14):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:',.<>?/~`"
    return ''.join(random.choices(all_chars, k=length))

# UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    strength = evaluate_strength(password)
    entropy_value = password_entropy(password)
    diversity = len(set(password))

    color_map = {"Weak": "red", "Moderate": "orange", "Strong": "green"}
    st.markdown(f"**Strength:** <span style='color:{color_map[strength]}'>{strength}</span>", unsafe_allow_html=True)

    if is_common_password(password):
        st.error("⚠️ This password is too common and easily guessable. Try making it more complex.")

    st.write(f"**Length:** {len(password)} characters")
    st.write(f"**Diversity:** {diversity} unique characters")
    st.write(f"**Entropy:** {entropy_value:.2f} bits")
    st.caption("ℹ️ Entropy measures the unpredictability of your password. Higher is better.")

    # Visual entropy meter (max 100 bits scale)
    entropy_percentage = min(int(entropy_value), 100)
    st.progress(entropy_percentage)

    # Suggest a better password if the current one is not strong
    if strength != "Strong":
        st.subheader("🔧 Suggested Strong Password")
        st.code(generate_strong_password(14))
