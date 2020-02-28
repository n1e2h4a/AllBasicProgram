import seaborn as sb
import matplotlib.pyplot as plt
dataframe=sb.load_dataset('tips')
sb.boxplot(x = "day" , y = 'tip' ,  data = dataframe)
plt.show()