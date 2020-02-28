import matplotlib
import numpy as np
import plotly.graph_objs as go
import seaborn
from plotly.offline import *
import random

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)
trace = go.Scatter(x=random_x, y=random_y,
                   mode='markers')
data = [trace]
offline.plot(data, filename='Basic-Scatter')
