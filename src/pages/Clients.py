import streamlit as st
from services.novos_clientes import inserir_cliente
from database.supabase import conectar_supabase

# Função para buscar todos os eventos cadastrados
def get_eventos():
    supabase = conectar_supabase()
    eventos = supabase.table("Evento").select("id_serial, cl_nome").execute()
    lista_eventos = [(evento['id_serial'], evento['cl_nome']) for evento in eventos.data]
    return lista_eventos

# Pegar todos os eventos do banco de dados
eventos = get_eventos()

st.title("Seja Bem-Vindo novo cliente")
st.write("# Preencha o formulário abaixo para se cadastrar no evento que deseja")

st.write("## Cadastro de Clientes")

with st.form(key="Clientes", clear_on_submit=True):

    # Dropdown para selecionar o evento ao qual o cliente será vinculado
    evento = st.selectbox("Selecione o evento", eventos, format_func=lambda x: x[1])

    nome = st.text_input("Nome: ", placeholder="Digite seu nome aqui")
    pix = st.text_input("Pix:", placeholder="Digite seu pix")

    button = st.form_submit_button("Cadastrar cliente no evento")
    if button:
        resultado = inserir_cliente(nome, pix, evento[0])  # Passa o id do evento
        if resultado:
            st.success("Cliente cadastrado com sucesso!")
        else:
            st.error("Ocorreu um erro ao cadastrar o cliente.")
