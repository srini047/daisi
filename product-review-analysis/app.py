# Streamlit UI
import streamlit as st
from sentiment import prediction

@st.cache
def st_ui():
    st.title("Reviews/Comments Analysis")

    comment = st.text_area("Enter your review/comment")

    if (st.button("Submit")):

        if (prediction(comment) == "Positive Comment😊"):
            st.write("Positive Comment➕")
        else:
            st.write("Negative Comment➖")
    else:
        st.write("Awaiting to submit comment...")

if __name__ == "__main__":
    st_ui()
