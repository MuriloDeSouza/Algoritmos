from supabase import create_client, Client

def conectar_supabase() -> Client:
    url = "https://ofqnhcrmsxvrlivqxoqh.supabase.co"  # Substitua por sua URL doSupabase
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9mcW5oY3Jtc3h2cmxpdnF4b3FoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjg1MjkyNDgsImV4cCI6MjA0NDEwNTI0OH0.XxXElUoIkUXeux7OqJdUh5IQ9gdLAXHL0boTQ2_yII4"  # Substitua pela sua chave de API do Supabase
    return create_client(url, key)

def select_group():
    supabase = conectar_supabase()
    try:
        resultado = supabase.table("Clientes").select("*").execute()
        if resultado:
            return resultado.data
    except Exception as e:
        print("An error occurred:", e)
        return False

def select_group_from_tables():
    supabase = conectar_supabase()
    try:
        resultado = supabase.table("Eventos").select("*").execute()
        if resultado:
            return resultado.data
    except Exception as e:
        print("An error occurred:", e)
        return False
    
def delete_group_by_id(id):
    supabase = conectar_supabase()
    try:
        resultado = supabase.table("Clientes").delete().eq("id", id).execute()
        if resultado:
            return resultado.data
    except Exception as e:
        print("An error occurred:", e)
        return False

def delete_group_by_name(nome):
    supabase = conectar_supabase()
    try:
        resultado = supabase.table("Clientes").delete().eq("cl_grupo", nome).execute()
        if resultado:
            return resultado.data
    except Exception as e:
        print("An error occurred:", e)
        return False

def all_tables():
    supabase = conectar_supabase()
    try:
        # Consulta SQL para listar todas as tabelas no schema público
        query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
        
        # Executa a consulta SQL diretamente usando o método sql() do Supabase
        resultado = supabase.rpc("execute_sql", {"query": query}).execute()
        
        if resultado and resultado.data:
            return [tabela['table_name'] for tabela in resultado.data]
        else:
            return "Nenhuma tabela encontrada."
    except Exception as e:
        print("An error occurred:", e)
        return "Erro ao recuperar as tabelas."


