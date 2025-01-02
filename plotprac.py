import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig = make_subplots(rows=2, cols=1, shared_xaxes=True)

fig.append_trace(go.Scatter(x=x, y=y1, mode='lines', name='sin(x)'), row=1, col=1)
fig.append_trace(go.Scatter(x=x, y=y2, mode='lines', name='cos(x)'), row=2, col=1)

fig.update_layout(title='Sin and Cos Waves',
                  xaxis_title='x',
                  yaxis_title='Amplitude')

fig.show()
