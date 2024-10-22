import streamlit as st
from services.novos_valores import inserir_valores

st.write("# Cadastro de Valores")
st.write("### Preencha o formulário abaixo para cadastrar um novo valor")

with st.form(key="Evento", clear_on_submit=True):
    nome = st.text_input("Nome", placeholder="Digite seu nome")
    valor = st.number_input("Valor:", format="%.2f", step=0.01, min_value=0.01, placeholder="Digite o valor separado por ponto")
    descricao = st.text_input("Descrição:", placeholder="Digite uma descrição para o valor")
    nomes = st.text_input("Nomes:", placeholder="Digite os nomes separados por vírgula")
    botao = st.form_submit_button("Cadastrar")

    if botao:
        st.success("Valor cadastrado com sucesso!")
        resultado = inserir_valores(nome, valor, descricao, nomes)
        if resultado:
            st.success("Valor cadastrado com sucesso!")
        else:
            st.error("Ocorreu um erro ao cadastrar o valor.")