print ("Exercícios de fixação para desenvolvimento em Python")

print("\n"+"1-Peça ao usuário seu nome e cumprimente utilizando a função print, ex.: Olá, Carol!")
nome = input("Qual o seu nome?") 
print("Olá,", nome,"!")


print("\n"+"2-Peça ao usuário sua idade e exiba na tela: Você tem {idade} anos!")
idade = input("Qual a sua idade?") 
print("Você tem", idade,"anos!")


print("\n"+"3-Leia o nome e a cidade da pessoa e imprima: nome x mora em cidade x.")
nome = "Aline"
cidade = "Palhoça"
print(nome, "mora em", cidade, ".")


print("\n"+"4-Leia um número e imprima o dobro dele.")
numero = 2
dobro = numero*2
print ("O dobro do numero é: " ,dobro)


print("\n"+"5-Leia dois números inteiros e imprima a soma.")
numero1 = 2
numero2 = 2
soma = numero1 + numero2
print("A soma é:", soma)



print("\n"+"6-Leia a altura em metros como float e imprima: Sua altura é x metros")
altura = 1.58
print("A altura é:", altura, "metros")


print("\n"+"7-Leia dois números decimais, float, e imprima a média. ")
dec1 = 12.0
dec2 = 12.0
media = (dec1 + dec2) /2
print("A média é:", media)

print("\n"+"8-Leia um número como string e imprima o seu tipo antes e depois de converter para int.")
numstr = "4"
print (type(numstr))
numint = int(numstr)
print (type(numint))

print("\n"+"9-Leia o preço de um produto e imprima o preço com 10% de desconto.")
preço = 10
desconto = 0.90
novopreço = (preço*desconto)
print ("O preço, com desconto, é: " , novopreço)


print("\n"+"10-Leia o raio de um círculo (float) e calcule a área, utilize π = 3.14.")
raio = 5.0
pi = 3.14
area = pi * (raio * raio)
print("A área do círculo é", area)


print("\n"+"11-Leia a distância (km) e o tempo (h), calcule a velocidade média")
dist = 2
temp = 1
vm = dist / temp
print ("A velocidade média é:" ,vm ,"km/hora")

print("\n"+"12-Leia 3 notas (float) e imprima a média com duas casas decimais.")
nota1 = float (10.0)
nota2 = float (20.0)
nota3 = float (30.0)
media = ( nota1 + nota2 + nota3) / 3
print (f"A média é:{media:.2f}")


print("\n"+"13-Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.")
salario = float (2000.00)
aumento = float (1.10)
novosalario = (salario*aumento)
print ("O novo salario é: ",novosalario)

print("\n"+"14-Leia uma quantidade de minutos (int) e converta para horas e minutos (ex.: 130 -> 2h10)")
totalminutos = 70
horas = totalminutos//60
minutosrest = totalminutos % 60
print(horas, "h", minutosrest)


print("\n"+"15 - Leia o nome e a idade e imprima exatamente neste formato:Nome: <nome> | Idade: <idade> anos")
nome = "Aline" 
idade = "42"  
print (f"Nome : {nome}| Idade: {idade} anos.")


print("\n"+"16 - Leia dois int (a e b) e imprima: a + b = X | a - b = Y | a * b = Z ")
a = 20
b = 40
soma = a + b
sub = a - b
multi = a * b
print("a + b =", soma, "| a - b =", sub, "| a * b =", multi)

print("\n"+"17 - Leia um float e imprima com 2 casas decimais")
valor = 42.20
print(f"O valor, com duas casas decimais, é: {valor:.2f}")

print("\n"+"18-Leia um nome e uma nota (float), com uma casa decimal, e imprima: Aluno <nome> ficou com nota <nota>")
NomeAluno = "Aline"
Nota = 7.8
print("Aluna" ,NomeAluno , "ficou com nota" ,Nota)

print("\n"+"19-Leia o ano de nascimento (int) e imprima a idade estimada. (considere ano atual = 2026).")
AN = 1983
AA = 2026
IE = AA - AN
print("A idade estimada é" , IE)

