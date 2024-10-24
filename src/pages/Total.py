import streamlit as st
from database.supabase import conectar_supabase
from pages.Gastos import get_eventos

eventos = get_eventos()

evento = st.selectbox("Selecione o evento", eventos, format_func=lambda x: x[1])

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
