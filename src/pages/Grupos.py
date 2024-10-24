import streamlit as st
import pandas as pd
from database.supabase import select_group, delete_group_by_id, delete_group_by_name

# Parte de pegar os grupos do banco de dados
st.write("## Grupos Cadastrados")
st.write("Aqui estão os grupos cadastrados:")

# Obtém os dados do Supabase
resultado = select_group()

# Verifica se os dados foram recebidos corretamente
if resultado:
    # Transforma os dados em um DataFrame
    df = pd.DataFrame(resultado)
    st.dataframe(df)  # Exibe a tabela de forma interativa

        # Parte de apagar algum grupo inserindo o ID do grupo para poder apagar
    st.write("## Apagar Grupo pelo ID")
    selected_id = st.selectbox("Selecione o ID do Grupo para apagar", df["id_serial"])  # Combina a lógica de seleção

    if st.button("Apagar Grupo pelo ID"):  # Usa um botão para confirmar a exclusão
        sucesso = delete_group_by_id(selected_id)
        if sucesso:
            st.success(f"Grupo com ID {selected_id} apagado com sucesso!")
        else:
            st.error("Ocorreu um erro ao tentar apagar o grupo.")

    # Parte de apagar o grupo pelo nome do Grupo
    st.write("## Apagar Grupo pelo Nome")
    selected_nome = st.selectbox("Selecione o Nome do Grupo para apagar", df["cl_nome"])  # Combina a lógica de seleção

    if st.button("Apagar Grupo pelo Nome"):
        group = delete_group_by_name(selected_nome)
        if group:
            st.success(f"Grupo com nome {selected_nome} apagado com sucesso!")
        else:
            st.error("Ocorreu um erro ao tentar apagar o grupo.")

else:
    st.write("Nenhum dado encontrado ou houve um erro na recuperação dos dados.")



