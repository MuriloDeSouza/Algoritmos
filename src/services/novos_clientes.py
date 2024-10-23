from database.supabase import conectar_supabase

def inserir_cliente(nome, pix):
    supabase = conectar_supabase()
    dados = {
        "cl_nome": nome,
        "cl_pix": pix,
    }
    resultado = supabase.table("Clientes").insert(dados).execute()
    return resultado
