import pandas as opcoesPandas
import numpy as opcoesNumpy

dataFrame_Datas = opcoesPandas.date_range("20221201", periods=31)
print(dataFrame_Datas)

print("\n data frame de 12 meses")
dataDrame = opcoesPandas.date_range("20221231", periods=12, freq="M")
print(dataDrame)

print("\n")

#----------------------------------

numerosAleatorios = opcoesPandas.DataFrame(opcoesNumpy.random.rand(5, 2)) # ele fez 5 linhas e duas colunas

# data frame de números aleatórios
print(numerosAleatorios)

print("\n")
numerossAleatorios = opcoesPandas.DataFrame(opcoesNumpy.random.rand(15, 5))
print(numerossAleatorios)



