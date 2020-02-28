import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
dataframe=pd.read_csv('/home/bridgelabz/Desktop/gapminder-FiveYearData.csv')
sb.boxplot(x = "continent" , y = 'lifeExp' ,  data = dataframe)
plt.show()