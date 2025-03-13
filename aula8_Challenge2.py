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
preco_simples = 100.00
preco_duplo = 150.00
preco_luxo = 250.00

# Cadastro de clientes
nome_cliente1 = input("Digite o nome do primeiro cliente: ")
idade_cliente1 = int(input(f"Digite a idade de {nome_cliente1}: "))

nome_cliente2 = input("Digite o nome do segundo cliente: ")
idade_cliente2 = int(input(f"Digite a idade de {nome_cliente2}: "))

nome_cliente3 = input("Digite o nome do terceiro cliente: ")
idade_cliente3 = int(input(f"Digite a idade de {nome_cliente3}: "))

# Escolha do quarto para cada cliente
print("\nTipos de quarto disponíveis:")
print("1. simples - R$ 100,00 por dia")
print("2. duplo - R$ 150,00 por dia")
print("3. luxo - R$ 250,00 por dia")

# Lógica para escolha de quarto e cálculo de preço com base na idade
# Para o primeiro cliente
if idade_cliente1 < 18:
    print(f"\n{nome_cliente1}, como você tem menos de 18 anos, você pode escolher apenas os quartos 'simples' ou 'duplo'.")
    quarto1 = input(f"{nome_cliente1}, qual tipo de quarto deseja (simples ou duplo)? ")
    if quarto1 == 'simples':
        preco1 = preco_simples
    elif quarto1 == 'duplo':
        preco1 = preco_duplo
    else:
        print("Escolha inválida! Seu quarto foi automaticamente definido como 'simples'.")
        quarto1 = 'simples'
        preco1 = preco_simples
elif idade_cliente1 >= 60:
    print(f"\n{nome_cliente1}, como você tem 60 anos ou mais, você tem 10% de desconto no quarto de sua escolha!")
    quarto1 = input(f"{nome_cliente1}, qual tipo de quarto deseja (simples, duplo ou luxo)? ")
    if quarto1 == 'simples':
        preco1 = preco_simples
    elif quarto1 == 'duplo':
        preco1 = preco_duplo
    elif quarto1 == 'luxo':
        preco1 = preco_luxo
    else:
        print("Escolha inválida! Seu quarto foi automaticamente definido como 'simples'.")
        quarto1 = 'simples'
        preco1 = preco_simples
    preco1 = preco1 * 0.90  # Desconto de 10%
else:
    print(f"\n{nome_cliente1}, você pode escolher qualquer tipo de quarto.")
    quarto1 = input(f"{nome_cliente1}, qual tipo de quarto deseja (simples, duplo ou luxo)? ")
    if quarto1 == 'simples':
        preco1 = preco_simples
    elif quarto1 == 'duplo':
        preco1 = preco_duplo
    elif quarto1 == 'luxo':
        preco1 = preco_luxo
    else:
        print("Escolha inválida! Seu quarto foi automaticamente definido como 'simples'.")
        quarto1 = 'simples'
        preco1 = preco_simples

# Para o segundo cliente
if idade_cliente2 < 18:
    print(f"\n{nome_cliente2}, como você tem menos de 18 anos, você pode escolher apenas os quartos 'simples' ou 'duplo'.")
    quarto2 = input(f"{nome_cliente2}, qual tipo de quarto deseja (simples ou duplo)? ")
    if quarto2 == 'simples':
        preco2 = preco_simples
    elif quarto2 == 'duplo':
        preco2 = preco_duplo
    else:
        print("Escolha inválida! Seu quarto foi automaticamente definido como 'simples'.")
        quarto2 = 'simples'
        preco2 = preco_simples
elif idade_cliente2 >= 60:
    print(f"\n{nome_cliente2}, como você tem 60 anos ou mais, você tem 10% de desconto no quarto de sua escolha!")
    quarto2 = input(f"{nome_cliente2}, qual tipo de quarto deseja (simples, duplo ou luxo)? ")
    if quarto2 == 'simples':
        preco2 = preco_simples
    elif quarto2 == 'duplo':
        preco2 = preco_duplo
    elif quarto2 == 'luxo':
        preco2 = preco_luxo
    else:
        print("Escolha inválida! Seu quarto foi automaticamente definido como 'simples'.")
        quarto2 = 'simples'
        preco2 = preco_simples
    preco2 = preco2 * 0.90  # Desconto de 10%
else:
    print(f"\n{nome_cliente2}, você pode escolher qualquer tipo de quarto.")
    quarto2 = input(f"{nome_cliente2}, qual tipo de quarto deseja (simples, duplo ou luxo)? ")
    if quarto2 == 'simples':
        preco2 = preco_simples
    elif quarto2 == 'duplo':
        preco2 = preco_duplo
    elif quarto2 == 'luxo':
        preco2 = preco_luxo
    else:
        print("Escolha inválida! Seu quarto foi automaticamente definido como 'simples'.")
        quarto2 = 'simples'
        preco2 = preco_simples

# Para o terceiro cliente
if idade_cliente3 < 18:
    print(f"\n{nome_cliente3}, como você tem menos de 18 anos, você pode escolher apenas os quartos 'simples' ou 'duplo'.")
    quarto3 = input(f"{nome_cliente3}, qual tipo de quarto deseja (simples ou duplo)? ")
    if quarto3 == 'simples':
        preco3 = preco_simples
    elif quarto3 == 'duplo':
        preco3 = preco_duplo
    else:
        print("Escolha inválida! Seu quarto foi automaticamente definido como 'simples'.")
        quarto3 = 'simples'
        preco3 = preco_simples
elif idade_cliente3 >= 60:
    print(f"\n{nome_cliente3}, como você tem 60 anos ou mais, você tem 10% de desconto no quarto de sua escolha!")
    quarto3 = input(f"{nome_cliente3}, qual tipo de quarto deseja (simples, duplo ou luxo)? ")
    if quarto3 == 'simples':
        preco3 = preco_simples
    elif quarto3 == 'duplo':
        preco3 = preco_duplo
    elif quarto3 == 'luxo':
        preco3 = preco_luxo
    else:
        print("Escolha inválida! Seu quarto foi automaticamente definido como 'simples'.")
        quarto3 = 'simples'
        preco3 = preco_simples
    preco3 = preco3 * 0.90  # Desconto de 10%
else:
    print(f"\n{nome_cliente3}, você pode escolher qualquer tipo de quarto.")
    quarto3 = input(f"{nome_cliente3}, qual tipo de quarto deseja (simples, duplo ou luxo)? ")
    if quarto3 == 'simples':
        preco3 = preco_simples
    elif quarto3 == 'duplo':
        preco3 = preco_duplo
    elif quarto3 == 'luxo':
        preco3 = preco_luxo
    else:
        print("Escolha inválida! Seu quarto foi automaticamente definido como 'simples'.")
        quarto3 = 'simples'
        preco3 = preco_simples

# Cálculo da estadia para cada cliente
dias1 = int(input(f"\nQuantos dias {nome_cliente1} ficará no hotel? "))
total1 = preco1 * dias1
print(f"\nO valor total da estadia de {nome_cliente1} é: R$ {total1:.2f}")

dias2 = int(input(f"\nQuantos dias {nome_cliente2} ficará no hotel? "))
total2 = preco2 * dias2
print(f"\nO valor total da estadia de {nome_cliente2} é: R$ {total2:.2f}")

dias3 = int(input(f"\nQuantos dias {nome_cliente3} ficará no hotel? "))
total3 = preco3 * dias3
print(f"\nO valor total da estadia de {nome_cliente3} é: R$ {total3:.2f}")

# Pagamento
pagamento1 = float(input(f"\n{nome_cliente1}, digite o valor pago: R$ "))
if pagamento1 == total1:
    print(f"Pagamento de R$ {total1:.2f} realizado com sucesso! Volte sempre.")
elif pagamento1 > total1:
    troco1 = pagamento1 - total1
    print(f"Pagamento realizado! Seu troco é R$ {troco1:.2f}.")
else:
    valor_restante1 = total1 - pagamento1
    print(f"Pagamento insuficiente. Faltam R$ {valor_restante1:.2f}.")
    dias_trabalhando1 = (valor_restante1 / 100)  # Supondo R$ 100/dia de trabalho no hotel
    print(f"Você precisaria trabalhar {int(dias_trabalhando1)} dias no hotel para cobrir a diferença.")


pagamento2 = float(input(f"\n{nome_cliente2}, digite o valor pago: R$ "))
if pagamento2 == total2:
    print(f"Pagamento de R$ {total2:.2f} realizado com sucesso! Volte sempre.")
elif pagamento2 > total2:
    troco2 = pagamento2 - total2
    print(f"Pagamento realizado! Seu troco é R$ {troco2:.2f}.")
else:
    valor_restante2 = total2 - pagamento2
    print(f"Pagamento insuficiente. Faltam R$ {valor_restante2:.2f}.")
    dias_trabalhando2 = (valor_restante2 / 100)  # Supondo R$ 100/dia de trabalho no hotel
    print(f"Você precisaria trabalhar {int(dias_trabalhando2)} dias no hotel para cobrir a diferença.")


pagamento3 = float(input(f"\n{nome_cliente3}, digite o valor pago: R$ "))
if pagamento3 == total3:
    print(f"Pagamento de R$ {total3:.2f} realizado com sucesso! Volte sempre.")
elif pagamento3 > total3:
    troco3 = pagamento3 - total3
    print(f"Pagamento realizado! Seu troco é R$ {troco3:.2f}.")
else:
    valor_restante3 = total3 - pagamento3
    print(f"Pagamento insuficiente. Faltam R$ {valor_restante3:.2f}.")
    dias_trabalhando3 = (valor_restante3 / 100)  # Supondo R$ 100/dia de trabalho no hotel
    print(f"Você precisaria trabalhar {int(dias_trabalhando3)} dias no hotel para cobrir a diferença.")