import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

trace1 = go.Scatter(x=df['date'], y=df['actual_max_temp'], name='Max Temp', mode='lines')
trace2 = go.Scatter(x=df['date'], y=df['actual_min_temp'], name='Min Temp', mode='lines')
trace3 = go.Scatter(x=df['date'], y=df['actual_mean_temp'], name='Mean Temp', mode='lines')
data = [trace1, trace2, trace3]

layout = go.Layout(title='Max, Min, and Mean Temp Each Day From 7-1-2014 through 6-30-2015', xaxis_title='Date',
                   yaxis_title='Temperature')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart.html')
