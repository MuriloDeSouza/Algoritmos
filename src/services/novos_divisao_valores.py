from database.supabase import conectar_supabase

def dividir_gasto_entre_pessoas(id_gasto, cliente_pagador, participantes, valor_por_pessoa):
    
    supabase = conectar_supabase()
    sucesso = True

    # Para cada participante (exceto o pagador), registramos uma dívida
    for cliente in participantes:
        if cliente != cliente_pagador:  # O pagador já pagou, não deve para si mesmo
            print("XOU DA XUXA!!")
            print(cliente)
            dados_divisao = {
                "id_gasto": id_gasto,
                "id_cliente_pag": cliente_pagador[0],  # ID do pagador
                "id_cliente_dev": cliente[0],  # ID de quem está devendo
                "valor_dividido": valor_por_pessoa,
            }
            # print("mostra dados_divisao " + cliente)
            resposta = supabase.table("DivGastos").insert(dados_divisao).execute()
            if resposta.status_code != 201 or resposta.data is None:  # Verifica se a inserção foi bem-sucedida
                sucesso = False
    
    return sucesso
