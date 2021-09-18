import corsikaio as crkio
import pandas as pd
import matplotlib.pyplot as plt

dt = crkio.CorsikaFile('/home/vikoluna/Documents/BUAP/Proyecto/gamma0_salida/gamma0_J11DAT000011')

data = pd.DataFrame(dt)
print(data.columns)
# data = data[['header', 'data', 'longitudinal', 'end']]
pd.DataFrame.to_csv(data)
data = data.dropna()
print(data.head)
