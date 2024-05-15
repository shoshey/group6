import streamlit as st

def xor_cipher(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return ciphertext

def main():
    st.title("XOR Block Cipher")

    option = st.radio("Choose an option:", ("Encrypt", "Decrypt"))

    if option == "Encrypt":
        plaintext = st.text_area("Enter the plaintext:")
        key = st.text_input("Enter the key:")
        if st.button("Encrypt"):
            ciphertext = xor_cipher(plaintext, key)
            st.success(f"Encrypted Text: {ciphertext}")
    elif option == "Decrypt":
        plaintext = st.text_area("Enter the hashed text:")
        key = st.text_input("Enter the key:")
        if st.button("Decrypt"):
            decrypted_text = xor_cipher(plaintext, key)
            st.success(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
