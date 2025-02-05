#Construa um programa que calcule: Calcule o contrário agora, quanto tempo demora para esse funcionário chegar em um salário de 10.000 reais?

salario = 2970
meta = 3500
aumento = 0.05
anos = 0

while salario < meta:
    salario = salario * (1 + aumento)
    anos += 1

print(f"{anos} anos") 