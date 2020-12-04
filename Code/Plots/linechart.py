import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

data = [go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='Max Temp')]

layout = go.Layout(title='Max Temp Each Day From 7-1-2014 through 6-30-2015', xaxis_title='Date',
                   yaxis_title='Temperature')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')
