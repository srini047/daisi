import streamlit as st
import base64

# Function to Encode

def Encode(message, key):

    '''
    Function to Encode

    Parameters:
	- message (str) :  Make sure you are passing language from given list 
    - key (str) : This can be any text in string form (similar to a OTP Password)
	Returns : Encoded text as per - https://docs.python.org/3/library/base64.html
    '''
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# Function to decode

    '''
    Function to Decode

    Parameters:
    - key (str) : This can be any text in string form (similar to a OTP Password)
	- message (str) :  Make sure you are passing language from given list 
	Returns : Encoded text as per - https://docs.python.org/3/library/base64.html
    '''
def Decode(key, encoded_message):
    dec = []
    encoded_message = base64.urlsafe_b64decode(encoded_message).decode()
    for i in range(len(encoded_message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(encoded_message[i]) - ord(key_c)) % 256))

    return "".join(dec)


message = st.text_input('Message Text')

key = st.text_input("Private key", type="password")

mode = st.selectbox("What action would you like to perform?",
                    ("Encode", "Decode"))

# Streamlit UI
def st_ui():
    if st.button('Result'):
        if (mode == "Encode"):
            st.write(Encode(key, message))
        else:
            st.write(Decode(key, message))
    else:
        st.write('Please enter all the required information!!')

if __name__ == "__main__":
    st_ui()