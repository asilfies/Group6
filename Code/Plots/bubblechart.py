import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

data = [go.Scatter(x=df['average_min_temp'], y=df['average_max_temp'], mode='markers',
                   marker=dict(size=df['average_min_temp'], color=df['average_max_temp'], showscale=True))
        ]

layout = go.Layout(title='Bubble Chart', xaxis_title='Date',yaxis_title='Temperature')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')
