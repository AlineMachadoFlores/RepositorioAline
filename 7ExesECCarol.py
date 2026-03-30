#1. Solicite ao usuário que informe um número e depois exiba se o número é positivo, negativo ou zero.
#2. Solicite ao usuário que informe a sua idade e depois exiba se é maior ou menor de idade.#
#3. Solicite ao usuário que informe a sua idade e depois classifique em:
#a. Menor ou igual a 11 anos = criança.
#b. Maior do que 11 e menor ou igual a 17 = adolescente.
#c. Maior do que 17 e menor ou igual a 59 = adulto
#d. Maior do que 59 = idoso.
#4. Solicite ao usuário que informe um número e depois exiba se é par ou ímpar.
#5. Solicite ao usuário que informe dois números e depois exiba qual número é maior ou se são iguais.
#6. Faça uma calculadora simples contendo as operações: soma, subtração, divisão e multiplicação. Solicite ao usuário que informe dois número e que informe também a operação que deseja realizar (+, -, /, *) e depois exiba o resultado.
numero = float(input("Informe um número: "))    
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

print()
idade = int(input("Informe sua idade: "))
if idade <=11:
    print("Criança")
elif idade > 11 and idade <=17:
    print("Adolescente")
elif idade > 17 and idade <=59:
    print("Adulto")
else:
    print("Idoso")
print()
numero2 = int(input("Informe outro número: "))
if numero2 % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")  
print()
numero3 = float(input("Informe um número: "))
numero4 = float(input("Informe outro número: "))
if numero3 > numero4:
    print(f"O número {numero3} é maior que {numero4}.")
elif numero4 > numero3:
    print(f"O número {numero4} é maior que {numero3}.")
else:
    print(f"Os números {numero3} e {numero4} são iguais.")
print()
operacao = input("Informe a operação que deseja realizar (+, -, /, *): ")
numero5 = float(input("Informe um número: "))
numero6 = float(input("Informe outro número: "))
if operacao == "+":
    resultado = numero5 + numero6
    print(f"O resultado da soma é: {resultado}")
elif operacao == "-":
    resultado = numero5 - numero6       
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "*":
    resultado = numero5 * numero6
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "/":
    if numero5 != 0:
        resultado = numero5 / numero6
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")    