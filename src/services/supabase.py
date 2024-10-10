from supabase import create_client, Client

def conectar_supabase() -> Client:
    url = "https://ofqnhcrmsxvrlivqxoqh.supabase.co"  # Substitua por sua URL do Supabase
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9mcW5oY3Jtc3h2cmxpdnF4b3FoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjg1MjkyNDgsImV4cCI6MjA0NDEwNTI0OH0.XxXElUoIkUXeux7OqJdUh5IQ9gdLAXHL0boTQ2_yII4"  # Substitua pela sua chave de API do Supabase
    return create_client(url, key)

def inserir_cliente(grupo, nome, idade, pix):
    supabase = conectar_supabase()
    dados = {
        "cl_grupo": grupo,
        "cl_nome": nome,
        "cl_idade": idade,
        "cl_pix": pix,
    }
    resultado = supabase.table("Cliente").insert(dados).execute()
    return resultado
