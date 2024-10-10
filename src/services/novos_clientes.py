from database.supabase import conectar_supabase

def inserir_cliente(grupo, nome, idade, pix):
    supabase = conectar_supabase()
    dados = {
        "cl_grupo": grupo,
        "cl_nome": nome,
        "cl_idade": idade,
        "cl_pix": pix,
    }
    resultado = supabase.table("Clientes").insert(dados).execute()
    return resultado
