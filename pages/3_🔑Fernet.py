import os
import io
from cryptography.fernet import Fernet
import streamlit as st

def generate_key():
    return Fernet.generate_key()

def load_key(key):
    return Fernet(key)

def encrypt_file(file, key, original_extension):
    data = file.read()
    fernet = load_key(key)
    encrypted_data = fernet.encrypt(data)
    return encrypted_data, original_extension

def decrypt_file(file, key, original_extension):
    data = file.read()
    fernet = load_key(key)
    decrypted_data = fernet.decrypt(data)
    return decrypted_data, original_extension

st.title("File Encryption and Decryption with Fernet")

action = st.selectbox("Select Action", ["Encrypt", "Decrypt"])

generated_key = None

if action == "Encrypt":
    generated_key = generate_key()
else:
    user_key = st.text_input("Enter Key")

file = st.file_uploader("Upload a file")

if st.button("Encrypt/Decrypt"):
    if file is not None and (action == "Encrypt" or (action == "Decrypt" and user_key)):
        if action == "Encrypt":
            original_extension = os.path.splitext(file.name)[1]  # Get the original file extension
            encrypted_data, original_extension = encrypt_file(file, generated_key, original_extension)
            with io.BytesIO(encrypted_data) as encrypted_file:
                st.download_button(label="Download Encrypted File", data=encrypted_file, file_name="encrypted_file" + original_extension, mime="application/octet-stream")
            st.info("File encrypted successfully! This is the encryption key: {}".format(generated_key.decode()))
        elif action == "Decrypt":
            original_extension = os.path.splitext(file.name)[1]  # Get the original file extension
            decrypted_data, original_extension = decrypt_file(file, user_key, original_extension)
            with io.BytesIO(decrypted_data) as decrypted_file:
                st.download_button(label="Download Decrypted File", data=decrypted_file, file_name="decrypted_file" + original_extension, mime="application/octet-stream")
