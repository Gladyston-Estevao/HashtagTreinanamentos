#Código para definir qual bônus o funcionário deverá receber caso ele conclua duas condições, utilizando Estrutura Condicional.

vendas_empresa = 12300 #R$ 12.300,00  
unidades_vendidas = 900
meta_unidades = 1000
meta_empresa = 10000

if vendas_empresa > meta_empresa and unidades_vendidas > meta_unidades:
    bonus = 250
else:
    bonus = 50

print (bonus)
