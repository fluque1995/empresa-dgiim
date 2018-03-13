import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd

data = pd.read_csv('../environmental.csv', index_col='Concept')
data = data[data.columns[::-1]] 

print(data)

trace1 = go.Scatter(
    x=data.columns,
    y=data.iloc[0].tolist(),
    name='Uso de energía'
)
trace2 = go.Scatter(
    x=data.columns,
    y=data.iloc[1].tolist(),
    name='Uso de agua',
)
trace3 = go.Scatter(
    x=data.columns,
    y=data.iloc[2].tolist(),
    name='Emisiones de CO2',
)

layout = go.Layout(
    title='Gasto medioambiental',
    xaxis=dict(
        domain=data.columns
    ),
)
data=[trace1, trace2, trace3]
fig = go.Figure(data=data, layout=layout)

plot_url = py.plot(fig, filename='multiple-axes-multiple')
