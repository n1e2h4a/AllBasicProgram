import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
dataframe=sb.load_dataset('tips')
sb.violinplot(x = "sex" , y = 'total_bill' ,  data = dataframe)
plt.show()