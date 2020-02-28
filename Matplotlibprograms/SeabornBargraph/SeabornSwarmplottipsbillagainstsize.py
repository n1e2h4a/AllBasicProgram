import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
dataframe=sb.load_dataset('tips')
sb.swarmplot(x = "total_bill" , y = 'size' ,  data = dataframe)
plt.show()