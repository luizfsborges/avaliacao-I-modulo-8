import re

def orientar_pagamento(_):
    return("\nInformações de pagamento.\n")

def mostrar_status(_):
    return("\nStatus do pedido.\n")

intencoes_dict = {
    r'(?i)^Como posso atualizar meu cartão de crédito$': "info_pagamento", 
    r'(?i)^"Preciso mudar a forma de pagamento, o que fazer$':"info_pagamento", 
    r'(?i)^"Quero atualizar minhas informações de pagamento$':"info_pagamento", 
    r'(?i)^"Método de pagamento desatualizado, como proceder para atualizar$':"info_pagamento",
    r'(?i)^"Onde vejo o status do meu pedido$':"status_pedido", 
    r'(?i)^"Como faço para rastrear meu pedido$':"status_pedido", 
    r'(?i)^"Quero saber onde está meu pedido, como faço$':"status_pedido", 
    r'(?i)^"Status de entrega, como consultar$':"status_pedido"
}

acoes_dict = {
    "info_pagamento":orientar_pagamento,
    "status_pedido":mostrar_status
}

def main():
    executar_chat = True
    while executar_chat:

        requisicao = input("\nDigite sua pergunta: ")

        if requisicao == "sair":
            executar_chat = False
        else:
            for key, value in intencoes_dict.items():
                padrao = re.compile(key)
                grupos = padrao.findall(requisicao)

                if grupos:
                    print(f"{acoes_dict[value](grupos[0])}", end=" ")

if __name__ == "__main__":
    main()