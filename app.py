import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="GROUP6",
    page_icon="🔒",
    layout="centered"
)

def run():
    st.markdown(
        """
        <center>
        <h1 style='text-align: center; color: #7DDA58; font-size: 36px;'>Cryptographic Application</h1>
        <p style='text-align: center; color: #7DDA58; font-size: 15px;'>GROUP 6</p>
        <p style='text-align: center; color: #7DDA58; font-size: 15px;'>Applied Cryptography - CSAC 329</p>
        <p>
        The Applied Cryptography Application project aims to develop a simple application that 
implements various cryptographic techniques to secure communication, data, and information exchange. 
Cryptography is the science of encoding and decoding messages to protect their confidentiality, integrity, 
and authenticity. The application will provide a user-friendly interface that allows users to encrypt, 
decrypt and hash messages/file using different cryptographic algorithms
</p>
        </center>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    run()