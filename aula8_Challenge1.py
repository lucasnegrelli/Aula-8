'''
***Desafio 1 Condicionais***

***Crie um sistema de e-commerce, onde o usuário possa:***

- ***cadastrar-se***
- ***comprar um produto***
- ***descobrir o valor total***
- ***pagar***

*Utilize variáveis, listas, condicionais*

Foco resolver o problema

Vamos trabalhar:

***Criatividade | Pensamento lógico | Flexibilidade cognitiva***
'''

# Produtos com seus preços
# Produtos com seus preços
produtos = {
    'camiseta': 39.90,
    'calca jeans': 129.90,
    'tenis': 199.90,
    'jaqueta': 249.90,
    'mochila': 89.90
}

# Cadastro inicial (primeiro o usuário deve se cadastrar)
print("\n--- Cadastro de Usuário ---")
nome_usuario = input("Digite seu nome: ")
email_usuario = input("Digite seu e-mail: ")
senha_usuario = input("Digite sua senha: ")

# Login do usuário
print("\n--- Login ---")
email = input("Digite seu e-mail: ")
senha = input("Digite sua senha: ")

if email == email_usuario and senha == senha_usuario:
    print(f"Bem-vindo de volta, {nome_usuario}!")
else:
    print("E-mail ou senha incorretos. Acesso negado.")
    exit()  # Encerra o programa se o login falhar

# Exibindo produtos disponíveis
print("\nProdutos disponíveis:")
print("1. camiseta: R$ 39.90")
print("2. calca jeans: R$ 129.90")
print("3. tenis: R$ 199.90")
print("4. jaqueta: R$ 249.90")
print("5. mochila: R$ 89.90")

# Coletando os produtos escolhidos
produto1 = input("\nDigite o nome do primeiro produto que deseja comprar: ")
produto2 = input("Digite o nome do segundo produto que deseja comprar: ")
produto3 = input("Digite o nome do terceiro produto que deseja comprar: ")

# Inicializando o total
total = 0

# Verificando o primeiro produto
if produto1 in produtos:
    total += produtos[produto1]
else:
    print(f"{produto1} não está disponível.")

# Verificando o segundo produto
if produto2 in produtos:
    total += produtos[produto2]
else:
    print(f"{produto2} não está disponível.")

# Verificando o terceiro produto
if produto3 in produtos:
    total += produtos[produto3]
else:
    print(f"{produto3} não está disponível.")

# Mostrando o total da compra
print(f"\nO total da sua compra é: R$ {total:.2f}")

# Pagamento
pagamento = float(input("\nDigite o valor para pagamento: R$ "))
if pagamento >= total:
    troco = pagamento - total
    print(f"Pagamento realizado! Seu troco é R$ {troco:.2f}")
else:
    print("Valor insuficiente para o pagamento.")
