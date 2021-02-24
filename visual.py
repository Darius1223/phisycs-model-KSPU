import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd


if __name__ == '__main__':
    filename = 'data.txt'

    with open(filename, 'r') as file:
        x, y = [], []
        for line in file:
            t_i, x_i, y_i, vx_i, vy_i = list(map(float, line.split()))
            x.append(x_i)
            y.append(y_i)

        px.scatter(x=x, y=y).show()
