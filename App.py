


import streamlit as st

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    return encrypted_text

# Streamlit app layout
st.title("Sabrin's Cipher App")
st.write("The Caeser Cipher App allows you to encrypt normal text by shifting the values. You can shift values from 1-25, but 5 is the default shift value. Press the Encrypt Now! button to get your encryption when you're done. But, if you want to decrypt your text, click the Decrypt Now! button.")
# Input for plain text
text = st.text_input("Enter the text to be encrypted:")

# Input for shift value
shift = st.number_input("Enter the shift value (1-25):", min_value=1, max_value=25, value=5)

# Button to encrypt
if st.button("Encrypt Now!"):
    if text:
        encrypted_text = caesar(text, shift)
        st.write('**Plain text:**', text)
        st.write('**Encrypted text:**', encrypted_text)
    else:
        st.warning("Please enter a text to encrypt.")


if st.button("Decrypt Now!"):
    if text:
        decrypted_text = caesar(text, -shift)  # Use negative shift for decryption
        st.write('**Plain text:**', text)
        st.write('**Decrypted text:**', decrypted_text)
    else:
        st.warning("Please enter a text to decrypt.")

