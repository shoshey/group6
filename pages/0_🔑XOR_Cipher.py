import streamlit as st

def xor_cipher(text, key):
    cipher_text = ""
    for char in text:
        cipher_text += chr(ord(char) ^ key)
    return cipher_text

def main():
    st.title("XOR Cipher")
    st.write("This app encrypts and decrypts text using XOR cipher.")

    action = st.selectbox("Select Action", ["Encrypt", "Decrypt"])
    if action == "Encrypt":
        text = st.text_input("Enter text to Encrypt:")
        key = st.number_input("Enter key:", value=5)
        if st.button("Encrypt"):
            encrypted_text = xor_cipher(text, key)
            st.write(f"Encrypted text: {encrypted_text}")

    if action == "Decrypt":
        text = st.text_input("Enter Ciphertext to Decrypt:")
        key = st.number_input("Enter key:", value=5)
        if st.button("Decrypt"):
            decrypted_text = xor_cipher(text, key)
            st.write(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
