import streamlit as st
from services.novos_valores import inserir_valores
from database.supabase import select_group_from_tables, select_group_by_name, names_in_group
import pandas as pd

nomes = names_in_group()

st.write("# Cadastro de Valores")
st.write("### Preencha o formulário abaixo para cadastrar um novo valor")

with st.form(key="Evento", clear_on_submit=True):
    nome = st.selectbox("Escolha um nome", nomes)
    valor = st.number_input("Valor:", format="%.2f", step=0.01, min_value=0.01, placeholder="Digite o valor separado por ponto")
    descricao = st.text_input("Descrição:", placeholder="Digite uma descrição para o valor")
    botao = st.form_submit_button("Cadastrar")

    if botao:
        resultado = inserir_valores(nome, valor, descricao)
        if resultado:
            st.success("Valor cadastrado com sucesso!")
        else:
            st.error("Ocorreu um erro ao cadastrar o valor.")

# Parte de pegar os grupos do banco de dados
st.write("## Pessoas no grupo, valores e a descrição")

# Obtém os dados do Supabase
resultado = select_group_from_tables()

# Verifica se os dados foram recebidos corretamente
if resultado:
    # Transforma os dados em um DataFrame
    df = pd.DataFrame(resultado)
    st.dataframe(df)  # Exibe a tabela de forma interativa
else:
    st.write("Nenhum dado encontrado ou houve um erro na recuperação dos dados.")


selecionar = st.selectbox("Escolha um nome:", nomes)
botton = st.button("Ver valor gasto")

if botton:
    st.success("Valor cadastrado com sucesso!")
    valor = select_group_by_name(selecionar)
    if valor:
         st.write(valor)
    else:
            st.error("Ocorreu um erro ao cadastrar o valor.")
