from database.supabase import conectar_supabase

def inserir_gastos(cliente_pagador, evento, valor, descricao):
    supabase = conectar_supabase()
    dados = {
        "id_cliente": cliente_pagador,
        "id_evento": evento,
        "cl_valor": valor,
        "cl_descricao": descricao,
    }
    resultado = supabase.table("Gastos").insert(dados).execute()
    return resultado
