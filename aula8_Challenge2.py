'''
- ***Desafio 2:  Condicionais***
***Sistema de Reservas de Hotel:***

***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.

- *Cadastro de Cliente:*
*O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*

- *Reservas de Quartos:*
***O sistema deve oferecer 3 tipos de quartos:*** 
***"Simples", "Duplo" e "Luxo".***

***Cada cliente deve escolher um quarto para sua estadia.
O preço da diária varia conforme o tipo de quarto:
Simples: R$ 100,00 por dia.
Duplo: R$ 150,00 por dia.
Luxo: R$ 250,00 por dia.***

- ***Cálculo da Estadia:***
***O usuário deve informar quantos dias cada cliente ficará no hotel.
O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***

Exemplo: 
 ***valor_cliente3 = preco_duplo * cliente3_dias***

*Pagamento:*
*O sistema deve exibir o valor total a ser pago por cada cliente após a aplicação do desconto.*

*Regras Adicionais:
Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.*

***O sistema não deve usar loops (for, while) nem funções.**
O código deve considerar todos os casos possíveis de escolha dos clientes.*
'''

# Preços dos quartos
preco_quartos = {
    "simples": 100.00,
    "duplo": 150.00,
    "luxo": 250.00
}

# Cadastro de clientes
clientes = []
for i in range(3):
    nome = input(f"Digite o nome do cliente {i+1}: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    clientes.append({"nome": nome, "idade": idade})

# Processamento para cada cliente
for cliente in clientes:
    nome_cliente = cliente["nome"]
    idade_cliente = cliente["idade"]

    # Definindo quais quartos são disponíveis
    print(f"\nTipos de quarto disponíveis:")
    print("1. Simples - R$ 100,00 por dia")
    print("2. Duplo - R$ 150,00 por dia")
    print("3. Luxo - R$ 250,00 por dia")
    
    # Lógica para a escolha do quarto
    if idade_cliente < 18:
        print(f"{nome_cliente}, como você tem menos de 18 anos, você pode escolher apenas os quartos 'simples' ou 'duplo'.")
        quarto = input(f"{nome_cliente}, qual tipo de quarto deseja (simples ou duplo)? ")
        if quarto not in preco_quartos:
            quarto = 'simples'  # Valor padrão se a escolha for inválida
    elif idade_cliente >= 60:
        print(f"{nome_cliente}, como você tem 60 anos ou mais, você tem 10% de desconto no quarto de sua escolha!")
        quarto = input(f"{nome_cliente}, qual tipo de quarto deseja (simples, duplo ou luxo)? ")
        if quarto not in preco_quartos:
            quarto = 'simples'  # Valor padrão se a escolha for inválida
    else:
        print(f"{nome_cliente}, você pode escolher qualquer tipo de quarto.")
        quarto = input(f"{nome_cliente}, qual tipo de quarto deseja (simples, duplo ou luxo)? ")
        if quarto not in preco_quartos:
            quarto = 'simples'  # Valor padrão se a escolha for inválida
    
    # Calcular o preço com base na escolha de quarto e idade
    preco = preco_quartos[quarto]
    if idade_cliente >= 60:
        preco *= 0.90  # Desconto de 10% para clientes com 60 anos ou mais
    
    # Cálculo da estadia para o cliente
    dias = int(input(f"\nQuantos dias {nome_cliente} ficará no hotel? "))
    total = preco * dias
    print(f"\nO valor total da estadia de {nome_cliente} é: R$ {total:.2f}")

    # Processamento do pagamento
    pagamento = float(input(f"\n{nome_cliente}, digite o valor pago: R$ "))
    if pagamento == total:
        print(f"Pagamento de R$ {total:.2f} realizado com sucesso! Volte sempre.")
    elif pagamento > total:
        print(f"Pagamento realizado! Seu troco é R$ {pagamento - total:.2f}.")
    else:
        print(f"Pagamento insuficiente. Faltam R$ {total - pagamento:.2f}.")
        dias_trabalhando = (total - pagamento) / 100
        print(f"Você precisaria trabalhar {int(dias_trabalhando)} dias no hotel para cobrir a diferença.")
