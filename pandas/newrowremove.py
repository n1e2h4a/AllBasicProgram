import pandas as pd
import numpy as np
usedata  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
result = pd.DataFrame(usedata,index=labels)
print("\n Real Data Frame:--")
print(result)
print("\n now append the new row in the dataframe")
result.loc["k"] = [4,"manoj","no",16.3]
print("\n new dataframe after append")
print(result)
print("\n Delete the appended column")
result = result.drop("k")
print(result)
