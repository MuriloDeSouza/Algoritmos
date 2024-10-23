import streamlit as st
from services.novos_eventos import inserir_evento

st.write("## Seja Bem-Vindo")
st.write("### Preencha o formulário abaixo para criar um evento")

st.title("Cadastro de Eventos")

with st.form(key="Evento", clear_on_submit=True):
    nome = st.text_input("Nome: ", placeholder="Digite o nome do evento")

    button = st.form_submit_button("Cadastrar evento")
    if button:
        resultado = inserir_evento(nome)
        if resultado:
            st.success("Valor cadastrado com sucesso!")
        else:
            st.error("Ocorreu um erro ao cadastrar o valor.")