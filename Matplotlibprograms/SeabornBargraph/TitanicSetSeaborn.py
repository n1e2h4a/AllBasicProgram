import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
dataframe=sb.load_dataset('titanic')
sb.barplot(x = "sex" , y = 'survived' , hue ="class" , data = dataframe)
plt.show()