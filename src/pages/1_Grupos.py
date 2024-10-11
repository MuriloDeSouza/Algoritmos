import streamlit as st
import pandas as pd
from database.supabase import pegar_grupos

st.write("## Grupos Cadastrados")
st.write("Aqui estão os grupos cadastrados:")

# Obtém os dados do Supabase
resultado = pegar_grupos()

# Verifica se os dados foram recebidos corretamente
if resultado:
    # Transforma os dados em um DataFrame
    df = pd.DataFrame(resultado)
    st.dataframe(df)  # Exibe a tabela de forma interativa
else:
    st.write("Nenhum dado encontrado ou houve um erro na recuperação dos dados.")
