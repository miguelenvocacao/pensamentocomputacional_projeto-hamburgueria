'''

CRUD

hanburgueria
Site de cardapio online de vendas e entregas de Fastfood

'''


print("hello world!")

nome_do_cliente = input("Digite seu nome: ")
print(f"Olá, {nome_do_cliente}! Seja bem-vindo à nossa hamburgueria online!")

input("Pressione enter para abrir o menu...")

while True:
    print("\n=== MENU DA HAMBURGUERIA ===")
    print("1. Cardápio")
    print("2. Fazer pedido")
    print("3. Atendimento ao cliente")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    # CARDÁPIO
    if escolha == "1":
        print("\n=== CARDÁPIO ===")
        print("1. Hambúrguer Clássico - R$ 15,00")
        print("2. Senhor Cheeseburger - R$ 18,00")
        print("3. Bacon Burger - R$ 20,00")
        print("4. Mestre dos baicons - R$ 17,00")
        print("5. Senhor das fritas - R$ 15,00")
        print("6. Coca-cola - R$ 5,00")
        print("7. Suco de laranja - R$ 6,00")
        print("8. Suco de uva - R$ 6,00")
        print("9. Suco de abacaxi - R$ 6,00")
        print("10. Suco de maracujá - R$ 6,00")
        print("11. Suco de limão - R$ 6,00")
        print("12. Suco de morango - R$ 6,00")
        print("13. Suco de manga - R$ 6,00")
        print("14. Guaraná - R$ 5,00")
        print("15. Pepsi - R$ 5,00")
        print("16. Sprite - R$ 5,00")
        print("17. Água - R$ 3,00")

    # FAZER PEDIDO
    elif escolha == "2":
        print("\nFaça seu pedido:")
        pedido = input("Digite o número do item: ")
        quantidade = input("Digite a quantidade: ")

        print(f"Você escolheu {quantidade}x do item {pedido}.")

        deseja_confirmar = input("Deseja confirmar seu pedido? (sim/não): ")

        if deseja_confirmar.lower() == "não":
            print("Pedido cancelado.")
            continue

        elif deseja_confirmar.lower() == "sim":
            print("Pedido confirmado!")

            deseja_pagar = input("Deseja pagar agora? (sim/não): ")

            if deseja_pagar.lower() == "sim":
              print("\nFormas de pagamento disponíveis:")
              print("1. Cartão de crédito")
              print("2. Cartão de débito")
              print("3. Pix")
              print("4. Dinheiro")

              escolha_pagamento = input("Escolha a forma de pagamento: ")

              if escolha_pagamento == "1":
                    print("Pagamento com cartão de crédito.")
              elif escolha_pagamento == "2":
                    print("Pagamento com cartão de débito.")
              elif escolha_pagamento == "3":
                    print("Pagamento via Pix.")
              elif escolha_pagamento == "4":
                    print("Pagamento em dinheiro na entrega.")
              else:
                    print("Opção inválida.")

            else:
                print("Você pagará na entrega.")

        else:
            print("Opção inválida.")

    # ATENDIMENTO
    elif escolha == "3":
        print("\nAtendimento ao cliente:")
        duvida = input("Digite sua dúvida: ")
        print("Obrigado! Responderemos em breve.")

    # SAIR
    elif escolha == "4":
        print("Obrigado por visitar! Até a próxima 👋")
        break

    else:
        print("Opção inválida.")