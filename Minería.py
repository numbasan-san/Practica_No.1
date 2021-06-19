from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./credit_card.csv')

#----------------------------------Mandatos/Respuestas----------------------------------#
# s1. Cargar el archivo 'credit_card.csv'.
# data = pd.read_csv('./credit_card.csv')
# print(data)
#--------------------------------------------------------------#
# 2. Visualizar los primeros 7 registros del conjunto de datos.
# print(data.head(7))
#--------------------------------------------------------------#
# 3. Visualizar los últimos 6 registros del conjunto de datos.
# print(data.tail(6))
#--------------------------------------------------------------#
# 4. Generar los estadísticos básicos.
# print(data.describe())
#--------------------------------------------------------------#
# 5. Completar todos los datos vacíos (na) con ceros (0).
# print(data.fillna(0))
#--------------------------------------------------------------#
# 6. Realizar un gráfico de tipo 'scatter' utilizando para el eje X la variable 'comprador_recurrente' y para el eje Y la variable 'reclamaciones'.
# print(set(data.comprador_recurrente))
# print(set(data.reclamaciones))
# fig, ax = plt.subplots()
# ax.scatter(data.reclamaciones, data.comprador_recurrente)
# plt.show()