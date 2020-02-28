import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
dataframe=sb.load_dataset('iris')
sb.violinplot(x = "species" , y = 'sepal_length' , hue=None,hue_order=None,orient=None, data = dataframe)
plt.show()