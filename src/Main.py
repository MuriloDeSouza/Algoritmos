import streamlit as st

st.set_page_config(
    page_title='Bora Lá!', 
    page_icon=':shark:',
    
    layout='wide')

with st.form(key="Clientes", clear_on_submit=True):
    grupo = st.text_input("Grupo: ", placeholder="Digite o nome do grupo")
    nome = st.text_input("Nome: ", placeholder="Digite seu nome aqui")
    idade = st.number_input("Idade:", format="%d", step=1, min_value=0)
    st.write("Coloque conforme a sua cahve PIX mesmo, que seja CPF, CNPJ, E-mail ou Telefone")
    pix = st.text_input("Pix:", placeholder="Digite seu pix")
    # pix = st.selectbox("Pix:", ("CPF", "Telefone", "E-mail", "CNPJ"))
    button = st.form_submit_button("Cadastrar")



st.link_button('Profile','/Profile')
st.link_button('Clients','/Clients')

