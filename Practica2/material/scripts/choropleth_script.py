import plotly.offline as py
import pandas as pd

df = pd.read_csv('../inversores_paises.csv')

data = [ dict(
        type = 'choropleth',
        locations = df['CODE'],
        z = df['Investors'],
        text = df['COUNTRIES'],
        autocolorscale = True,
        reversescale = False,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            title = 'Número de inversores'),
      ) ]

layout = dict(
    title = 'Número de inversores por país (año 2015)',
    geo = dict(
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)

fig = dict( data=data, layout=layout )
py.plot( fig, validate=False, filename='inversores-paises' )
