
# EXERCÍCIOS: 

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")


# 2*
# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode votar.")


# 3*
# Declara uma variável com um número qualquer, determine se um número é par ou ímpar.
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


# 4*
# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
a = float(input("Digite o comprimento do primeiro lado: "))
b = float(input("Digite o comprimento do segundo lado: "))
c = float(input("Digite o comprimento do terceiro lado: "))
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.
if a == b == c:
    print("O triângulo é equilátero.")
elif a == b or b == c or a == c:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")


# 5*
# Determine se um número é múltiplo de 5 e 7.
numero = int(input("Digite um número: "))

if numero % 5 == 0 and numero % 7 == 0:
    print("O número é múltiplo de 5 e 7.")
else:
    print("O número não é múltiplo de 5 e 7.")


# 6*
# Verifique se um número é positivo e maior que 10
numero = float(input("Digite um número: "))

if numero >= 10:
    print("O número é positivo e maior que 10.")
elif numero > 0 and numero <10:
    print("O número é positivo, porém, menor que 10.")
else:
    print("O número é negativo.")



# 7*
# Verifique se um número é divisível por 3 ou 5.
numero = int(input("Digite um número: "))

if numero % 3 == 0 or numero % 5 == 0:
    print("O número é divisível por 3 ou 5.")
else:
    print("O número não é divisível por 3 ou 5.")
