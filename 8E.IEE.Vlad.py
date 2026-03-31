#Peça para o aluno digitar a idade de uma pessoa e o programa deve classificar:
#0–12 → Criança
#13–17 → Adolescente
#18–59 → Adulto
#60+ → Idoso
idade = int(input("Informe a idade da pessoa: "))
if idade <= 12:
    print("Criança")        
elif idade > 12 and idade <=17:
    print("Adolescente")
elif idade > 17 and idade <=59:
    print("Adulto")
else:
    print("Idoso")


print ()
#O aluno digita uma nota de 0 a 10. O programa retorna: 
#≥ 9 → Excelente
#≥ 7 → Bom
#≥ 5 → Regular
#< 5 → Reprovado
nota = float(input("Informe a nota (0 a 10): "))
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
else:
    print("Reprovado")
