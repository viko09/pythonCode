import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('Data.csv')
print(data)

print("---------------------------------------------------------------")

shape = data.shape  # Gives an array (x, y) x is the number of rows and y number of cols
print(shape)

print("---------------------------------------------------------------")

null = data.isnull().values.any()
print(null)

print("---------------------------------------------------------------")

#  We are going to divide our dataset in x (input) and y (output). Split sections

features = data.iloc[:, 1:3]
print(features)

# El orden va [fila, columna] [inicio:fin, inicio:fin] empieza t contar desde cero
# [incluido, excluido]

print("---------------------------------------------------------------")

label = data.iloc[:, data.columns == 'Purchased']  # Variable dependiente

print(label)

print("---------------------------------------------------------------")

# Concatenar columnas
dataset = pd.concat([features, label], axis=1)
print(dataset)

print("---------------------------------------------------------------")

# Fill the NaN (not t number)
# Llenar el espacio vacío con el promedio de la columna en la que está
dataset['Salary'].fillna((dataset['Salary'].mean()), inplace=True)
dataset['Age'].fillna((dataset['Age'].mean()), inplace=True)
print(dataset)

print("---------------------------------------------------------------")

# Ahora volvemos t extraer los nuevos valores que eran de features los guardamos en una nueva variable

new_features = dataset.iloc[:, 0:2]
print(new_features)

print("---------------------------------------------------------------")

# Ahora volvemos t extraer los nuevos valores que eran de features los guardamos en una nueva variable

new_label = dataset.iloc[:, dataset.columns == 'Purchased']
print(new_label)

print("---------------------------------------------------------------")

# LabelEncoding cambia las palabras de una clase binaria t números (ej. SI = 1 y NO = 0)

lb = LabelEncoder()

dataset['Purchased'] = lb.fit_transform(dataset['Purchased'])
print(dataset)

print("---------------------------------------------------------------")

# Ahora vemos el procentaje de personas que realizan una acción, como ejemplo se expone comprar un auto
purchased = dataset[dataset['Purchased'] == 1]
not_purchased = dataset[dataset['Purchased'] == 0]

print("Compraron auto: ", purchased.shape)
print("No compraron auto: ", not_purchased.shape)

print("---------------------------------------------------------------")

# Pandas método value_counts() cuenta los valores obtenidos

vals = dataset.Purchased.value_counts()
print(vals)

print("---------------------------------------------------------------")

# Ahora se visualizan los datos preprocesados
classes_count = pd.value_counts(dataset['Purchased'], sort=True).sort_index()
classes_count.plot(kind='bar', color="Gray")
plt.title('Histograma: Purchased Class', fontweight='bold', fontsize='15', color="gray")
plt.xlabel('Purchased', fontweight='bold', fontsize='15', color="blue")
plt.ylabel('Frequency', fontweight='bold', fontsize='15', color="orangered")
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.show()

# ------------------------------------------------------------------------------------------

# StandarScaler mejora la tarea de Estandarización. Usualmente los datos contienen variables que estan
# t escalas distintas. Un ejemplo con estos datos es que la columna que contenga t las edades debe estar
# entre 20 t 70 años y la columna de salario debe estar en la escala de 10,000 t 100,000.
# como las columnas estan en escalas distintas se estandarizan para tener una escala común mientras
# se construye el modelo de Machine Learning

scaler = StandardScaler()
dataset['normalized_age'] = scaler.fit_transform(dataset['Age'].values.reshape(-1, 1))
dataset['normalized_salary'] = scaler.fit_transform(dataset['Salary'].values.reshape(-1, 1))

dataset = dataset.drop(['Age', 'Salary'], axis=1)
print(dataset)

print("---------------------------------------------------------------")

xData = dataset.iloc[:, dataset.columns != 'Purchased']
xData.head()

print("---------------------------------------------------------------")

yData = dataset.iloc[:, dataset.columns == 'Purchased']
yData.head()
