from database.supabase import conectar_supabase

def inserir_valores(nome, valor, descricao, nomes):
    supabase = conectar_supabase()
    dados = {
        "cl_nome": nome,
        "cl_valor": valor,
        "cl_descricao": descricao,
        "cl_nomes": nomes,
    }
    resultado = supabase.table("Evento").insert(dados).execute()
    return resultado
