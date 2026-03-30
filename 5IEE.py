#Calculadora de IMC

#Coleta de dados
peso = float(input("Digite seu peso em kg (ex.: 65.1): "))   
altura = float(input("Digite sua altura em metros (ex.:1.58): "))

#Cálculo do IMC
IMC = peso / (altura**2)

#Classificação
if IMC < 18.5:
    categoria = "Magreza"

elif IMC < 25:
    categoria = "Normal"
elif IMC < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidade"

#Saída Formatada
print (f"IMC = {IMC:.2f} - {categoria}")