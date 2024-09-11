# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)
val=int(input("digite sua idade"))
if (val <= 12):
    print("criança")
if (val <=17) and (val >= 13):
        print("adolescente")
if (val >=18) and (val <=59):
            print("adulto")
if (val >= 60):
                print("idoso") 