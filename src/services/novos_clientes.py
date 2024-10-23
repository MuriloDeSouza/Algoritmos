from database.supabase import conectar_supabase

def inserir_cliente(nome, pix, evento):
    supabase = conectar_supabase()
    dados = {
        "cl_nome": nome,
        "cl_pix": pix,
        "id_evento": evento,
    }
    resultado = supabase.table("Clientes").insert(dados).execute()
    return resultado
