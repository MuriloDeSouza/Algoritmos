import streamlit as st
from database.supabase import conectar_supabase
from services.novos_valores import inserir_gastos

# Função para buscar clientes de um evento específico
def get_clientes_por_evento(evento_id):
    supabase = conectar_supabase()
    clientes = supabase.table("Clientes").select("id_serial, cl_nome, id_evento").eq("id_evento", evento_id).execute()
    return [(cliente['id_serial'], cliente['cl_nome']) for cliente in clientes.data]

# Função para buscar eventos
def get_eventos():
    supabase = conectar_supabase()
    eventos = supabase.table("Evento").select("id_serial, cl_nome").execute()
    return [(evento['id_serial'], evento['cl_nome']) for evento in eventos.data]

# Selecionar o evento
eventos = get_eventos()

st.write("## Registro de Gastos")

evento = st.selectbox("Selecione o evento", eventos, format_func=lambda x: x[1])

# Pegar os clientes do evento selecionado
clientes = get_clientes_por_evento(evento[0])

with st.form(key="Gastos", clear_on_submit=True):
    cliente = st.selectbox("Selecione o cliente", clientes, format_func=lambda x: x[1])
    valor = st.number_input("Valor do gasto:", min_value=0.0, step=0.01)

    button = st.form_submit_button("Registrar Gasto")
    if button:
        resultado = inserir_gastos(cliente[0], evento[0], valor)
        if resultado:
            st.success("Gasto registrado com sucesso!")
        else:
            st.error("Ocorreu um erro ao registrar o gasto.")

# Função para calcular o total de gastos de um evento
def calcular_total_e_dividir_gastos(evento_id):
    supabase = conectar_supabase()
    
    # Buscar todos os gastos do evento
    gastos = supabase.table("Gastos").select("cl_valor").eq("id_evento", evento_id).execute()
    total_gastos = sum([gasto['cl_valor'] for gasto in gastos.data])
    
    # Buscar todos os clientes do evento
    clientes = supabase.table("Clientes").select("id_serial").eq("id_evento", evento_id).execute()
    num_clientes = len(clientes.data)

    if num_clientes > 0:
        valor_por_cliente = total_gastos / num_clientes
        return total_gastos, valor_por_cliente
    else:
        return 0, 0

st.write("## Divisão de Gastos")

evento_selecionado = st.selectbox("Selecione o evento para dividir os gastos", eventos, format_func=lambda x: x[1])

if st.button("Calcular divisão"):
    total, por_cliente = calcular_total_e_dividir_gastos(evento_selecionado[0])
    st.write(f"Total de gastos: R$ {total:.2f}")
    st.write(f"Valor por cliente: R$ {por_cliente:.2f}")
