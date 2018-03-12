import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd

data = pd.read_csv('../environmental.csv', index_col='Concept')
data = data[data.columns[::-1]] 

trace1 = go.Scatter(
    x=data.columns,
    y=data.iloc[0].tolist(),
    name='Uso de energía'
)
trace2 = go.Scatter(
    x=data.columns,
    y=data.iloc[1].tolist(),
    name='Uso de agua',
    yaxis='y2'
)
trace3 = go.Scatter(
    x=data.columns,
    y=data.iloc[2].tolist(),
    name='Emisiones de CO2',
    yaxis='y3'
)

layout = go.Layout(
    title='Environmental summary',
    width=800,
    xaxis=dict(
        domain=data.columns
    ),
    yaxis=dict(
        title='yaxis title',
        titlefont=dict(
            color='#1f77b4'
        ),
        tickfont=dict(
            color='#1f77b4'
        )
    ),
    yaxis2=dict(
        title='yaxis2 title',
        titlefont=dict(
            color='#ff7f0e'
        ),
        tickfont=dict(
            color='#ff7f0e'
        ),
        anchor='free',
        overlaying='y',
        side='left',
        position=0.15
    ),
    yaxis3=dict(
        title='yaxis4 title',
        titlefont=dict(
            color='#d62728'
        ),
        tickfont=dict(
            color='#d62728'
        ),
        anchor='x',
        overlaying='y',
        side='right'
    ),
)
data=[trace1, trace2, trace3]
fig = go.Figure(data=data, layout=layout)

plot_url = py.plot(fig, filename='multiple-axes-multiple')
