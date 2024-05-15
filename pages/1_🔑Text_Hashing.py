import streamlit as st
import hashlib

def hash_text(text, algorithm):
    if algorithm == "MD5":
        hashed_text = hashlib.md5(text.encode()).hexdigest()
    elif algorithm == "SHA-1":
        hashed_text = hashlib.sha1(text.encode()).hexdigest()
    elif algorithm == "SHA-256":
        hashed_text = hashlib.sha256(text.encode()).hexdigest()
    else:
        hashed_text = "Invalid algorithm selected"
    return hashed_text

st.title("Text Hashing App")

text = st.text_input("Enter text to hash:")
algorithm = st.selectbox("Select hashing algorithm", ["MD5", "SHA-1", "SHA-256"])

if st.button("Encrypt"):
    hashed_text = hash_text(text, algorithm)
    st.write(f"Hashed text using {algorithm}: {hashed_text}")
