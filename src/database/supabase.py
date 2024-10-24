from supabase import create_client, Client

def conectar_supabase() -> Client:
    url = "https://ofqnhcrmsxvrlivqxoqh.supabase.co"  # Substitua por sua URL doSupabase
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9mcW5oY3Jtc3h2cmxpdnF4b3FoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjg1MjkyNDgsImV4cCI6MjA0NDEwNTI0OH0.XxXElUoIkUXeux7OqJdUh5IQ9gdLAXHL0boTQ2_yII4"  # Substitua pela sua chave de API do Supabase
    return create_client(url, key)

def select_group():
    supabase = conectar_supabase()
    try:
        resultado = supabase.table("Evento").select("*").execute()
        if resultado:
            return resultado.data
    except Exception as e:
        print("An error occurred:", e)
        return False

def select_group_eventos():
    supabase = conectar_supabase()
    try:
        resultado = supabase.table("Evento").select("cl_nome").execute()
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

def names_in_group():
    supabase = conectar_supabase()
    try:
        # Seleciona os nomes dos eventos
        resultado = supabase.table("Evento").select("cl_nome").execute()
        
        if resultado and resultado.data:
            # Cria uma lista de nomes únicos
            nomes_unicos = list({nome['cl_nome'] for nome in resultado.data})
            return nomes_unicos
        else:
            return []
    except Exception as e:
        print("An error occurred:", e)
        return []

def select_group_by_name(name):
    supabase = conectar_supabase()
    try:
        # Pega o id_serial do evento pelo nome
        evento = supabase.table("Evento").select("id_serial").eq("cl_nome", name).execute()
        if evento and evento.data:
            id_evento = evento.data[0]['id_serial']
            
            # Soma os valores gastos por todos os clientes no evento
            resultado = supabase.table("Gastos").select("cl_valor").eq("id_evento", id_evento).execute()
            
            if resultado and resultado.data:
                total_valor = sum([item['cl_valor'] for item in resultado.data if 'cl_valor' in item])
                return total_valor
            else:
                return "Nenhum gasto encontrado para este evento."
        else:
            return "Evento não encontrado."
    except Exception as e:
        print("An error occurred:", e)
        return False


def delete_group_by_id(id_serial):
    supabase = conectar_supabase()
    try:
        resultado = supabase.table("Evento").delete().eq("id_serial", id_serial).execute()
        if resultado:
            return resultado.data
    except Exception as e:
        print("An error occurred:", e)
        return False

def delete_group_by_name(nome):
    supabase = conectar_supabase()
    try:
        resultado = supabase.table("Evento").delete().eq("cl_nome", nome).execute()
        if resultado:
            return resultado.data
    except Exception as e:
        print("An error occurred:", e)
        return False

def all_tables():
    supabase = conectar_supabase()
    try:
        resultado = supabase.rpc("get_tables", {}).execute()  # Se você tiver um RPC customizado
        if resultado and resultado.data:
            return resultado.data
        else:
            return "Nenhuma tabela encontrada."
    except Exception as e:
        print("An error occurred:", e)
        return "Erro ao recuperar as tabelas."


