from database.supabase import conectar_supabase

def inserir_evento(nome):
    supabase = conectar_supabase()
    dados = {
        "cl_nome": nome,
    }
    resultado = supabase.table("Evento").insert(dados).execute()
    return resultado