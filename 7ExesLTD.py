#7ExesLTD.PY


#-----------------EXERCÍCIO 1
#1 - crie uma lista vazia
#2 - utilize print para exibir lista de compras a cada adição ou remoção de itens da lista
#3 - utilize append para adicionar itens a lista
#4 - adicione remove para remover itens da lista

listadecompras = [] 
print("Lista de compras: ", listadecompras)
listadecompras.append("pão")
print("Lista de compras: ", listadecompras)         
listadecompras.append("queijo")
print("Lista de compras: ", listadecompras)
listadecompras.append("presunto")
print("Lista de compras: ", listadecompras)
listadecompras.remove("presunto")
print("Lista de compras: ", listadecompras)
print()

#-----------------EXERCÍCIO 2
# Remova um número se ele existir

#Tarefa: 
#Leia quatro inteiros e crie uma lista.
#Leia um valor alvo e remova se ele estiver na lista.
#Mostre o tamanho antes e depois.
#Use: int(), input(), in, remove(), len(), print()
#Tipos: int, list.
#Conceitos: teste de pertencimento, tratamento simples de remoção, função len().

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))    
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
numeros = [n1, n2, n3, n4]
print("Números na lista:", numeros)
print("Tamanho da lista antes:", len(numeros))  
remover = int(input("Digite o número a ser removido: "))
if remover in numeros:
    numeros.remove(remover)
    print("Número removido com sucesso.")
else:    print("Número não encontrado na lista.")
print("Números na lista após remoção:", numeros)
print("Tamanho da lista depois:", len(numeros))
print()

#-------------------------EXERCÍCIO 3
#Atualizar elemento com uma operação
#Crie uma lista com três inteiros. 
#Atualize o último elemento para a soma dos dois primeiros.
#xiba a lista.
#Use: int(), input(), indexação lista[i], print()
#Tipos: int, list.
#Conceitos: operadores aritméticos (+), acesso/atribuição por índice.
num1 = int(input("Digite um numero inteiro:"))
num2 = int(input("Digite outro numero inteiro:"))
num3 = int(input("Digite mais um numero inteiro:"))
numeros = [num1, num2, num3]
print("Lista original:", numeros)
numeros[2] = numeros[0] + numeros[1]
print("Lista atualizada:", numeros)
print()


#-------------------------EXERCÍCIO 4
#Notas: 
#subtituir a menor nota, ordenar e recalcular a média

#Leia três notas (float) em uma lista.
#Calcule a média.
#Substitua a menor nota por uma nova informada.
#Ordene a lista e mostre a nova média.
#Use: float(), input(), min(), list.index(), atribuição por índice, sort(), sum(), len(), print()
#Tipos: float, list.
#Conceitos: mutabilidade, ordenação in-place, média aritmética.
notas = [float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: ")), float(input("Digite a terceira nota: "))]
media = sum(notas) / len(notas)
print("A média das nots é: ", media)
menor_nota = min(notas)
nova_nota = float(input("Digite a nova nota para substituir a menor: "))
indice_menor = notas.index(menor_nota)
notas[indice_menor] = nova_nota 
notas.sort()
print("A lista ordenada é: ", notas)
nova_media = sum(notas) / len(notas)
print("A nova média das notas é: ", nova_media)
print()



#-------------------------EXERCÍCIO 5

#desafio] Fila: chegadas, prioridade e atendimento
#Tarefa: Inicie fila = ["Ana", "Bruno"]. Leia dois nomes e adicione (use extend). Leia um cliente prioritário e insira na posição 1. Atenda (remova e capture) o primeiro com pop(0). Exiba a fila a cada etapa.
#Use: input(), extend(), insert(), pop(), print()
#Tipos: str, list.
#Conceitos: estrutura de fila, operações de inserção/remoção, ordem.
# Iniciando a fila com os clientes iniciais
fila = ["Ana", "Bruno"] 
print("Fila inicial:", fila)
novos_clientes = input("Digite dois nomes de clientes separados por espaço: ").split()
fila.extend(novos_clientes)
print("Fila após adicionar novos clientes:", fila)
cliente_prioritario = input("Digite o nome do cliente prioritário: ")       
fila.insert(0, cliente_prioritario)
print("Fila após adicionar cliente prioritário:", fila)
cliente_atendido = fila.pop(0)
print("Cliente atendido:", cliente_atendido)
print("Fila após atendimento:", fila)
print()



#-------------------------EXERCÍCIO 6
#Criar e exibir dicionário de aluno
#Tarefa: Leia nome e idade. Crie aluno = {"nome": ..., "idade": ...} e exiba o dicionário e seu tipo.
#Use: input(), int(), literal {}, acesso por chave dict["chave"], print(), type()
#Tipos: str, int, dict.
#Conceitos: mapeamento chave-valor, criação e exibição.
#Leitura de dados
nome = input("Digite o nome do aluno: ")    
idade = int(input("Digite a idade do aluno: "))
#Criação do dicionário
aluno = {"nome": nome, "idade": idade}
#Exibição do dicionário e seu tipo
print(aluno)  # Exibe o dicionário do aluno
print(type(aluno))  # Exibe o tipo do dicionário
print()

#-------------------------EXERCÍCIO 7
#CONTINUIDADE DO EXERCÍCIO ANTERIOR] 
#Adicionar uma nova chave nota
#Tarefa: Partindo de um aluno com nome e idade, leia uma nota (float) e adicione a chave "nota". Exiba o dicionário.
#Use: float(), input(), atribuição dict["nota"] = valor, print()
#Tipos: float, dict.
#Conceitos: atualização/adição de chave, tipos numéricos.
aluno = {"nome": "João", "idade": 20}
nota = float(input("Digite a nota do aluno: "))
aluno["nota"] = nota
print(aluno)
print()

#------------------------EXERCÍCIO 8
#[DICT] Remover uma chave com segurança
#Tarefa: Leia produto = {"nome": str, "preco": float}. 
#Tente remover a chave "desconto" se existir, sem gerar erro. 
#Mostre antes e depois.
#Use: input(), float(), dict.pop("chave", valor_padrao), print()
#Tipos: str, float, dict.
#Conceitos: remoção segura, estado antes/depois.
#Criando o dicionário do produto
nome = str(input("Digite o nome do produto: "))
preco = float(input("Digite o preço do produto: "))
produto = {"nome": nome, "preco": preco}
print("Antes:", produto)
produto.pop("desconto", None)
print("Depois:", produto)
print()

#-------------------------EXERCÍCIO 9
#[DICT - desafio] Atualizar preço e quantidade; calcular o total 
#Tarefa: Leia produto = {"nome": str, "preco": float, "quantidade": int}. 
#Aplique aumento percentual ao preço e some 2 unidades na quantidade. 
#Calcule total = preco * quantidade e exiba.
#Use: float(), int(), input(), acesso/atribuição por chave, print()
#Tipos: str, float, int, dict.
#Conceitos: operadores aritméticos (*, +), atualização de valores no dict.
#Exemplo de entrada:
#Produto: Caneta    
#Preço: 1.50
#Quantidade: 10 
#Aumento percentual: 10
#Exemplo de saída:
#Produto: Caneta
#Preço atualizado: 1.65
#Quantidade atualizada: 12
#Leitura dos dados do produto
produto = {}
produto["nome"] = input("Produto: ")        
produto["preco"] = float(input("Preço: "))
produto["quantidade"] = int(input("Quantidade: "))
aumento_percentual = float(input("Aumento percentual: "))
#Atualização do preço e quantidade
produto["preco"] += produto["preco"] * (aumento_percentual / 100)
produto["quantidade"] += 2
#Cálculo do total
total = produto["preco"] * produto["quantidade"]
#Exibição dos resultados
print(f"Produto: {produto['nome']}")
print(f"Preço atualizado: {produto['preco']:.2f}")
print(f"Quantidade atualizada: {produto['quantidade']}")
print(f"Total: {total:.2f}")
print()


#--------------------------EXERCÍCIO 10
#[DICT  - desafio] Agenda (CRUD simples) com ordenação de nomes
#Tarefa: Comece com agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}. 
#Adicionar um novo contato (nome→telefone)
#Atualizar o telefone de um contato informado (se existir)
#Remover um contato pelo nome (se existir)
#Exibir a lista ordenada de nomes de contatos
#Tipos: str, dict, list (para a lista ordenada, se desejar armazenar).Conceitos: CRUD em dicionários, teste de existência, ordenação de chaves.Use: input(), acesso/atribuição agenda[nome] = tel, in, pop(), sorted(agenda.keys()), print()
agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}
while True:
    print("\nAgenda de Contatos")
    print("1. Adicionar contato")
    print("2. Atualizar telefone")
    print("3. Remover contato")
    print("4. Exibir contatos ordenados")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda[nome] = telefone
        print(f"Contato {nome} adicionado/atualizado com sucesso.")

    elif escolha == "2":
        nome = input("Digite o nome do contato a atualizar: ")
        if nome in agenda:
            telefone = input("Digite o novo telefone do contato: ")
            agenda[nome] = telefone
            print(f"Telefone de {nome} atualizado com sucesso.")
        else:
            print(f"Contato {nome} não encontrado.")

    elif escolha == "3":
        nome = input("Digite o nome do contato a remover: ")
        if nome in agenda:
            agenda.pop(nome)
            print(f"Contato {nome} removido com sucesso.")
        else:
            print(f"Contato {nome} não encontrado.")

    elif escolha == "4":
        print("\nContatos ordenados:")
        for nome in sorted(agenda.keys()):
            print(f"{nome}: {agenda[nome]}")

    elif escolha == "5":
        print("Saindo da agenda. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")
print()

#--------------------EXERCÍCIO 11
#[TUPLE] Criar e exibir uma tupla simples
#Tarefa: Leia dois nomes do usuário e coloque-os em uma tupla.
# Depois exiba a tupla e o tipo dela.
#Orientações: 
#usar input(), print(), type()
#usar tupla no formato (valor1, valor2)
#tipo trabalhado: str, tuple
#Exemplo de saída:
#Digite o primeiro nome: Alice
#Digite o segundo nome: Bob
#A tupla criada é: ('Alice', 'Bob')
#Criar a tupla com os nomes fornecidos pelo usuário
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
tupla_nomes = (nome1, nome2)
#Exibir a tupla e o tipo dela
print("A tupla criada é:", tupla_nomes)
print("O tipo da tupla é:", type(tupla_nomes))
print()

#----------------------EXERCÍCIO 12
#[TUPLE] Acessar elementos da tupla
#Tarefa: Leia três frutas e coloque em uma tupla.
#Depois leia uma fruta e diga se ela está ou não na tupla.
#Orientações: 
#usar in
#usar input()
#tipo: str, tuple
#conceito: operador de pertinência
#Criando a tupla com as frutas
fruta1 = input("Digite o nome da primeira fruta: ") 
fruta2 = input("Digite o nome da segunda fruta: ")
fruta3 = input("Digite o nome da terceira fruta: ")
frutas = (fruta1, fruta2, fruta3)
fruta = input("Digite o nome de uma fruta: ")
if fruta in frutas:
    print(f"A fruta {fruta} está na tupla.")
else:
    print(f"A fruta {fruta} não está na tupla.")
print()

#---------------------------EXERCÍCIO 13
#[TUPLE] Contar quantas vezes um número aparece
#Tarefa: Leia quatro números inteiros e crie uma tupla.
#Depois leia um número e diga quantas vezes ele aparece na tupla.
#Orientações: 
#método: tuple.count()
#tipos: int, tuple


numeros = tuple(int(input("Digite um número inteiro: ")) for _ in range(4)) 
numero_contar = int(input("Digite um número para contar: "))
contador = numeros.count(numero_contar)
print(f"O número {numero_contar} aparece {contador} vezes na tupla {numeros}.")
print()

#---------------------------EXERCÍCIO 14
#[TUPLE] Exibir maior e menor valor
#Tarefa: Leia quatro números inteiros, coloque em uma tupla e exiba o maior e o menor.
#Orientações: 
#funções: max(), min()
#tipos: int, tuple
#conceito: operações básicas de agregação

numeros = tuple(int(input("Digite um número inteiro: ")) for _ in range(4))
maior = max(numeros)
menor = min(numeros)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print()

#--------------------------EXERCÍCIO 15
#[TUPLE] Dias da semana com tuplas
#1 - Crie uma tupla com os dias da semana. dias = ()
#2 - Utilize print() para exibis os dias da semana na tela. print(dias)
#3 - Utilize o índice para exibir o primeiro dia da semana. Dica: dias [0]
#4 - Utilize o índice para exibiri o último dia da lista.Dica? dias [-1]
#5 - Verifique o tamanho da tupla utilizando len(dias).

dias = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")
print(dias)     
print(dias[0])
print(dias[-1])
print(len(dias))    
print()

#--------------------------EXERCÍCIO 16
#[TUPLE - desafio] Tupla de notas com média (sem alterar a tupla)
#Tarefa: Leia três notas (float) earmazene em uma tupla. 
#Exiba a tupla e a média das notas.
# #Use: float(), sum(), len(), print()
#Sem alterar tupla.

notas = (float(input("Digite a primeira nota: ")),
         float(input("Digite a segunda nota: ")),   
            float(input("Digite a terceira nota: ")))
media = sum(notas) / len(notas)
print("Notas:", notas)
print("Média:", media)
print()


#--------------------------EXERCÍCIO 17
#[TUPLE - desafio] Organizar valores sem mexer na tupla original
#Tarefa: Leia quatro números em uma tupla e exiba: 
#a tupla original
#uma lista ordenada apenas para visualização
#o tipo da variável ordenada
#Objetivo: mostrar diferença entre tupla e lista sem precisar modificar nada.Use: sorted(), print(), type()

numeros = (4, 2, 3, 1)
print("Tupla original:", numeros)
numeros_ordenados = sorted(numeros)
print("Lista ordenada para visualização:", numeros_ordenados)
print("Tipo da variável ordenada:", type(numeros_ordenados))
