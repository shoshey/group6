def main():
    st.title("File Encryption and Decryption with Fernet")

    # Sidebar for key generation
    st.sidebar.header("Key Generation")
    key = st.sidebar.button("Generate Key")
    generated_key = None

    if key:
        generated_key = generate_key()
        st.sidebar.text("Generated Key: {}".format(generated_key.decode()))

    # Main content for file encryption and decryption
    st.header("Encrypt / Decrypt Files")

    action = st.radio("Select Action:", ("Encrypt", "Decrypt"))

    if action == "Encrypt":
        file = st.file_uploader("Upload File to Encrypt")
        if file is not None:
            file_contents = file.read()
            if generated_key:
                encrypted_content = encrypt_file(generated_key, file_contents)
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
            if generated_key:
                try:
                    decrypted_content = decrypt_file(generated_key, file_contents)
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
