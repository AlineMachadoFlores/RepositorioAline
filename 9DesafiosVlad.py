

#Resolva os desafios abaixo utilizando funções (def) em Python.
()

print("Desafio 01")
#Crie uma função que receba um nome como parâmetro e exiba a mensagem: 'Bem-vindo, NOME' 
#a-criar função saudação
#b-Exibir a mensagem de boas-vindas para o nome "Aline"
()
def saudacao(nome):
    print(f'Bem-vinda, {nome}')
saudacao("Aline")  
()
()


print("Desafio 02")
#Crie uma função que receba dois números como parâmetros e retorne a soma desses números
#a-criar função soma, com dois numeros
#b - retornar a soma dos dois numeros
#c - chamar (print)a função, definindo eu mesma os números
()
def soma(num1, num2):
    return num1 + num2
print(f"A soma de 5 e 10 é: {soma(5, 10)}")
()
()


print("Desafio 03")
#Crie uma função que receba um número e informe se ele é PAR ou ÍMPAR. 
#a-criar uma função chamada par_ou_impar que receba um número como parâmetro.
#b-chamar (print) o resultado, depois de definir numero
()
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "PAR"
    else:
        return "ÍMPAR"  
print(f"O número 10 é: {par_ou_impar(10)}")
()
()



print("Desafio 04")
#Crie uma função que receba uma lista de números e retorne o maior número da lista. 
#a-criar função, vamos chama-la de listadenumeros
#b-criar uma variavel para receber o maior numero, vamos chama-la de maiornumero
#d-retornar o maior numero
#e-chamar a função e passar uma lista de numeros para ela
()
def listadenumeros(lista):
    maiornumero = lista[0]   
    for numero in lista:
        if numero > maiornumero:
            maiornumero = numero
    return maiornumero
print("o maior número é:", listadenumeros([10,20,30,40,50,60]))


print("Desafio 05")
#Crie uma função que receba uma string e retorne a quantidade de caracteres que ela possui.
#a-criar função, vamos chama-la de caracteres   
#b- a função deve receber um parametro do tipo string, vamos definir que vai ser "paz" para testar a função depois de criada        
#c- a função deve retornar a quantidade de caracteres que a string possui, para isso podemos usar a função len() do python, que retorna a quantidade de caracteres de uma string
()
def caracteres(string):
    return len(string)  
print("A quantidade de caracteres em 'paz' é:", caracteres("paz"))
()
()



print("Desafio 06")
#Crie uma função que receba uma lista de números e retorne a média dos valores.
#a-Criar uma função com lista de numeros
#b-Criar uma função para calcular a média dos valores da lista
#c-Chamar a função para calcular a média dos valores da lista e imprimir o resultado
()
def calcular_media(lista_numeros):
    if len(lista_numeros) == 0:
        return 0
    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    return media
print("A média dos valores [1, 2, 3, 4, 5] é:", calcular_media([1, 2, 3, 4, 5]))
()
()



print("Desafio 07")
#Crie uma função que receba uma palavra e verifique se ela é um palíndromo
#a-Criar uma função com uma palavras
#b-Verificar se a palavra é um palíndromo   
def verificar_palindromo(palavra):
    return palavra == palavra[::-1]  
print("A palavra 'arara' é um palíndromo?", verificar_palindromo("arara"))
()
()








