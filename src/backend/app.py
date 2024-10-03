import streamlit as st

st.title("Hello World")
st.write("This is a Streamlit app.")
texto = st.text_input("Escreva aqui")
if texto:
    st.write(f"Você escreveu: {texto}")
