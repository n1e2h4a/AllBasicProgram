import pandas as pd
import numpy as np
exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]
sample = pd.DataFrame(exam_data)
for index, row in sample.iterrows():
    print(row['name'], row['score'])