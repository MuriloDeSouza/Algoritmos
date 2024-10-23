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

# clientes_cadastrados = []

# formulario_cliente_novo = st.form(key='clientes', clear_on_submit=True)

st.write("## Seja Bem-Vindo novo cliente")
st.write("### Preencha o formulário abaixo para se cadastrar")

st.title("Cadastro de Clientes")

with st.form(key="Clientes", clear_on_submit=True):
    nome = st.text_input("Nome: ", placeholder="Digite seu nome aqui")
    pix = st.text_input("Pix:", placeholder="Digite seu pix")
    
    # Dropdown para selecionar o evento ao qual o cliente será vinculado
    evento = st.selectbox("Selecione o evento", eventos, format_func=lambda x: x[1])

    button = st.form_submit_button("Cadastrar novo cliente")
    if button:
        resultado = inserir_cliente(nome, pix, evento[0])  # Passa o id do evento
        if resultado:
            st.success("Cliente cadastrado com sucesso!")
        else:
            st.error("Ocorreu um erro ao cadastrar o cliente.")


# with st.form(key="Clientes", clear_on_submit=True):
#     nome = st.text_input("Nome: ", placeholder="Digite seu nome aqui")
#     st.write("Coloque conforme a sua cahve PIX mesmo, que seja CPF, CNPJ, E-mail ou Telefone")
#     pix = st.text_input("Pix:", placeholder="Digite seu pix")

#     button = st.form_submit_button("Cadastrar novo cliente")
#     if button:
#         resultado = inserir_cliente(nome, pix)
#         if resultado:
#             st.success("Valor cadastrado com sucesso!")
#         else:
#             st.error("Ocorreu um erro ao cadastrar o valor.")

# with formulario_cliente_novo:
#     nome = st.text_input("Nome", placeholder="Digite seu nome")
#     idade = st.number_input("Idade", placeholder="Digite sua idade", max_value=150)
#     email = st.text_input("Email", placeholder="Digite seu email")
#     chave = st.selectbox("Qual modelo a sua chave PIX ?", ["CPF", "Telefone", "Email", "CNPJ", "Chave-aleatória"])
#     if chave == "CPF":
#         pix = st.text_input("Pix" , placeholder="Digite seu CPF aqui")
#     elif chave == "Telefone":
#         pix = st.text_input("Pix" , placeholder="Digite seu pix com DDD aqui")
#     elif chave == "Email":
#         pix = st.text_input("Pix" , placeholder="Digite seu Email aqui")
#     elif chave == "CNPJ":
#         pix = st.text_input("Pix" , placeholder="Digite seu pix")
    
#     botao = formulario_cliente_novo.form_submit_button("Cadastrar")
#     if botao == True:
#         st.write("### Cliente Cadastrado com sucesso")
#         clientes_cadastrados.append({"Nome": nome, "Idade": idade, "Email": email, "Chave PIX": pix})

# print(clientes_cadastrados)