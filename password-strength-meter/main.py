import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits # Adds numbers (0-9) if selected

    if use_special:
        characters += string.punctuation # Adds special characters (!,@,#,$,%,^,&,*) if selected
        
    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Geneate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: '{password}'")

st.write("-----------------------")

st.write("Build by [Mustafa](https://github.com/MUstafakhanb)")