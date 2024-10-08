import streamlit as st

st.write("## Seja Bem-Vindo novo cliente")
st.write("### Preencha o formulário abaixo para se cadastrar")

st.title("Cadastro de Clientes")

clientes_cadastrados = []

formulario_cliente_novo = st.form(key='clientes', clear_on_submit=True)

with formulario_cliente_novo:
    nome = st.text_input("Nome", placeholder="Digite seu nome")
    idade = st.number_input("Idade", placeholder="Digite sua idade", max_value=150)
    email = st.text_input("Email", placeholder="Digite seu email")
    chave = st.selectbox("Qual modelo a sua chave PIX ?", ["CPF", "Telefone", "Email", "CNPJ", "Chave-aleatória"])
    if chave == "CPF":
        pix = st.text_input("Pix" , placeholder="Digite seu CPF aqui")
    elif chave == "Telefone":
        pix = st.text_input("Pix" , placeholder="Digite seu pix com DDD aqui")
    elif chave == "Email":
        pix = st.text_input("Pix" , placeholder="Digite seu Email aqui")
    elif chave == "CNPJ":
        pix = st.text_input("Pix" , placeholder="Digite seu pix")
    
    botao = formulario_cliente_novo.form_submit_button("Cadastrar")
    if botao == True:
        st.write("### Cliente Cadastrado com sucesso")
        clientes_cadastrados.append({"Nome": nome, "Idade": idade, "Email": email, "Chave PIX": pix})

print(clientes_cadastrados)