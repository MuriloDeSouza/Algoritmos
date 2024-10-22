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
        resultado = supabase.table("Evento").select("*").execute()
        if resultado:
            return resultado.data
    except Exception as e:
        print("An error occurred:", e)
        return False

def select_group_by_name(name):
    supabase = conectar_supabase()  # Certifique-se de adicionar os parênteses para a conexão
    try:
        # Executa a query para pegar os registros onde o nome é igual a "name"
        resultado = supabase.table("Evento").select("*").eq("cl_nome", name).execute()  # Corrigir o campo "name" para "cl_nome"
        
        if resultado and resultado.data:  # Verifica se há resultados
            # Extrair os valores da coluna "cl_valor" (valores float) e somar
            total_valor = sum([item['cl_valor'] for item in resultado.data if 'cl_valor' in item])
            return total_valor
        else:
            return "Nenhum dado encontrado para o nome fornecido."
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


