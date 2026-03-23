'''

CRUD

hanburgueria
Site de cardapio online de vendas e entregas de Fastfood

'''


print("hello world!")
#input("Pressione enter para sair...")  

nome_do_cliente = input("Digite seu nome: ")

print(f"Olá, {nome_do_cliente}! Seja bem-vindo à nossa hamburgueria online!")

nome_do_cliente = input("Pressione enter para abrir o menu...")
print("Aqui está o nosso menu:")

while True:
# Menu
 print("\n=== MENU DA HAMBURGUERIA ===")
 print("1. cardapio")
 print("2. fazer pedido")
 print("3. atendimento ao cliente")
 print("4. sair")

 escolha = input("Digite os numeros dos pedidos que deseja: ")

# Cardapio
 if escolha == "1":
        print("\n=== CARDÁPIO ===")
        print("1. Hambúrguer Clássico - R$ 15,00")
        print("2. Senhor Cheeseburger - R$ 18,00")
        print("3. Bacon Burger - R$ 20,00")
        print("4. Mestre dos baicons - R$ 17,00")
        print("5. Senhor das fritas - R$ 15,00")
        print("6. coca-cola - R$ 5,00")
        print("7. suco de laranja - R$ 6,00")
        print("8. suco de uva - R$ 6,00")
        print("9. suco de abacaxi - R$ 6,00")
        print("10. suco de maracujá - R$ 6,00")
        print("11. suco de limão - R$ 6,00")
        print("12. suco de morango - R$ 6,00")
        print("13. suco de manga - R$ 6,00")
        print("14. guaraná - R$ 5,00")
        print("15. pepsi - R$ 5,00")
        print("16. sprite - R$ 5,00")
        print("17. água - R$ 3,00")

       # Fazer pedido
 elif escolha == "2":
        print("\nFaça seus pedidos:")
        pedido = input("digite os numeros do cardapio que deseja pedir: ")
        print(f"Você escolheu os itens {pedido}.")
        print("Agora, vamos para a quantidade.")
        quantidade = input("Digite a quantidade: ")
        print(f"Você escolheu {quantidade} dos itens {pedido}.")

        # Confirmação
        deseja_confirmar = input("Deseja confirmar seu pedido? (sim/não): ")
        if deseja_confirmar.lower() == "não":
            print("Pedido cancelado.")  
            continue # Volta pro menu
        elif deseja_confirmar.lower() == "sim":
                print("Pedido confirmado! Em breve, entraremos em contato para o pagamento e entrega.")
        # Pagamento
                deseja_pagar = input("Deseja pagar agora? (sim/não): ")
                if deseja_pagar.lower() == "não":
                    print("Tudo bem! Você pode pagar no momento da entrega.")
                    continue
             
        elif deseja_pagar.lower() == "sim":
                   print("\nFormas de pagamento disponíveis:")
                   formas_de_pagamento = [
                          "1. Cartão de crédito",
                          "2. Cartão de débito",
                          "3. Pix",
                          "4. Dinheiro"
                        ]


                   escolha_pagamento = input("Digite o número da forma de pagamento desejada: ")
                   if escolha_pagamento == "1":
                        print("Você escolheu pagar com cartão de crédito. Por favor, insira os dados do cartão.")
        elif escolha_pagamento == "2":
                        print("Você escolheu pagar com cartão de débito. Por favor, insira os dados do cartão.")
        elif escolha_pagamento == "3":
                        print("Você escolheu pagar com Pix. Por favor, escaneie o código QR para realizar o pagamento.")
        elif escolha_pagamento == "4":
                        print("Você escolheu pagar com dinheiro. O pagamento será feito no momento da entrega.")
        else:
                        print("Opção de pagamento inválida. Por favor, tente novamente.")
                    continue 

 elif escolha == "3":
        print("\nAtendimento ao cliente:")
        duvida = input("Digite sua dúvida ou comentário: ")
        print("Obrigado por entrar em contato! Responderemos em breve.")

 elif escolha == "4":
        print("Obrigado por visitar nossa hamburgueria online! Até a próxima!")
        break

 else:
        print("Opção inválida. Por favor, tente novamente.")
