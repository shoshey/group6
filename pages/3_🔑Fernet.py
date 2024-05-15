import streamlit as st
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(key, file_content):
    fernet = Fernet(key)
    encrypted_content = fernet.encrypt(file_content)
    return encrypted_content

def decrypt_file(key, encrypted_content):
    fernet = Fernet(key)
    decrypted_content = fernet.decrypt(encrypted_content)
    return decrypted_content

def main():
    st.title("File Encryption and Decryption with Fernet")

    # Sidebar for key generation
    st.sidebar.header("Key Generation")
    key = st.sidebar.button("Generate Key")

    if key:
        key = generate_key()
        st.sidebar.text("Generated Key: {}".format(key.decode()))

    # Main content for file encryption and decryption
    st.header("Encrypt / Decrypt Files")

    action = st.radio("Select Action:", ("Encrypt", "Decrypt"))

    if action == "Encrypt":
        file = st.file_uploader("Upload File to Encrypt")
        if file is not None:
            file_contents = file.read()
            if key:
                encrypted_content = encrypt_file(key, file_contents)
                st.download_button(
                    label="Download Encrypted File",
                    data=encrypted_content,
                    file_name="encrypted_file.txt",
                    mime="text/plain",
                )

    elif action == "Decrypt":
        file = st.file_uploader("Upload File to Decrypt")
        if file is not None:
            file_contents = file.read()
            if key:
                try:
                    decrypted_content = decrypt_file(key, file_contents)
                    st.download_button(
                        label="Download Decrypted File",
                        data=decrypted_content,
                        file_name="decrypted_file.txt",
                        mime="text/plain",
                    )
                except Exception as e:
                    st.error("Decryption Error: {}".format(e))

if __name__ == "__main__":
    main()
