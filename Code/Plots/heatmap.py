import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

data = [go.Heatmap(x=df['day'], y=df['month'], z=df['actual_max_temp'], colorscale='Jet')]

layout = go.Layout(title='Max Temperatures', xaxis_title='Day of Week', yaxis_title='Month of Year')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')