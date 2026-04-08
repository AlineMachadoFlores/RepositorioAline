# 1. Definimos a função (ela apenas calcula e devolve)
def soma(num1, num2):
    return num1 + num2

# 2. Agora pedimos os números FORA da função
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# 3. Chamamos a função passando os valores e imprimimos o resultado
resultado = soma(n1, n2)
print(f"A soma dos números é: {resultado}")