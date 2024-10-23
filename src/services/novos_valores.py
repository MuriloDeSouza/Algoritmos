from database.supabase import conectar_supabase

def inserir_gastos(cliente, evento, valor):
    supabase = conectar_supabase()
    dados = {
        "id_cliente": cliente,
        "ide_evento": evento,
        "cl_valor": valor,
    }
    resultado = supabase.table("Gastos").insert(dados).execute()
    return resultado
