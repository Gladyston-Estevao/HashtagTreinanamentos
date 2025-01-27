lista_precos = [100, 50, 2000, 6000]
reajuste = 0.05
lista_reajustada = []

for preco in lista_precos:
    novo_preco = preco * (1 + reajuste)
    lista_reajustada.append(novo_preco)
print(lista_reajustada) 