import streamlit as st
from services.novos_eventos import inserir_evento
from database.supabase import select_group_eventos
import pandas as pd

st.set_page_config(
    page_title='Bora Lá!', 
    page_icon=':shark:',
    layout='wide')

st.title("Seja Bem-Vindo")
st.write("# Preencha o formulário abaixo para criar um evento")

st.write("## Cadastro de Eventos")

with st.form(key="Evento", clear_on_submit=True):
    nome = st.text_input("Nome: ", placeholder="Digite o nome do evento")

    button = st.form_submit_button("Cadastrar evento")
    if button:
        resultado = inserir_evento(nome)
        if resultado:
            st.success("Valor cadastrado com sucesso!")
        else:
            st.error("Ocorreu um erro ao cadastrar o valor.")

st.write("## Todos os eventos criados")

st.write("Aqui estão todos os eventos criados:")

resultado = select_group_eventos()

if resultado:
    df = pd.DataFrame(resultado)
    st.dataframe(df)



st.link_button('Grupos','/Grupos')
st.link_button('Clients','/Clients')
st.link_button('Conta','/Conta')

