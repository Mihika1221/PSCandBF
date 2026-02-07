import re
import streamlit as st

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    if not re.search("[a-z]", password):
        return "Weak"
    if not re.search("[A-Z]", password):
        return "Weak"
    if not re.search("[0-9]", password):
        return "Weak"
    return "Strong"

st.title("Password Strength Checker")
password = st.text_input("Enter Password", type="password")
if password:
    strength = check_password_strength(password)
    st.write(f"Password Strength: {strength}")
