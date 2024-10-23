import streamlit as st
from services.novos_clientes import inserir_cliente

st.set_page_config(
    page_title='Bora Lá!', 
    page_icon=':shark:',
    layout='wide')

with st.form(key="Clientes", clear_on_submit=True):
    nome = st.text_input("Nome: ", placeholder="Digite seu nome aqui")
    st.write("Coloque conforme a sua cahve PIX mesmo, que seja CPF, CNPJ, E-mail ou Telefone")
    pix = st.text_input("Pix:", placeholder="Digite seu pix")
    # pix = st.selectbox("Pix:", ("CPF", "Telefone", "E-mail", "CNPJ"))
    button = st.form_submit_button("Cadastrar")

    if button:
        resultado = inserir_cliente(nome, pix)
        if resultado:
            st.success("Cliente cadastrado com sucesso!")
        else:
            st.error("Ocorreu um erro ao cadastrar o cliente.")

st.link_button('Grupos','/Grupos')
st.link_button('Clients','/Clients')
st.link_button('Conta','/Conta')

