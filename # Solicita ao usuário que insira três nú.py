# Solicita ao usuário que insira três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Compara os números para encontrar o maior
if num1 >= num2 and num1 >= num3:
    maior_numero = num1
elif num2 >= num1 and num2 >= num3:
    maior_numero = num2
else:
    maior_numero = num3

# Exibe o resultado
print("O maior número é:", maior_numero)