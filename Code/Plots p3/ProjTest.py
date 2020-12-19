import io
from base64 import b64encode
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import numpy as py
# Load CSV file from Datasets folder
df1 = pd.read_csv('DateRange.csv')
df2 = pd.read_csv('myData.csv')
df3 = pd.read_csv('GDPGlobal.csv')

buffer = io.StringIO()
app = dash.Dash()

# Line Chart
#1960 2019

#Date:str
py.Date2 = [0] * 60
dummy = 0
for i in range(1960, 2020):
    py.Date2 [dummy] = i
    #print( py.Date2[dummy] )
    dummy = dummy + 1
    print()#DO NOT COMMENT OUT THIS LINE


fuckThis = 11
if fuckThis == 0:
    place = 'Aruba'
elif fuckThis == 1:
    place= 'Afghanistan'
else:
    place = 'United States'

dynamicCountryTitle = 'GDP of ' + str(place) + ' From 1960 to 2019'


layout = go.Layout(xaxis_title="Year Range",yaxis_title="GDP")

#create figure
fig = go.Figure()

#create trace
fig.add_trace(
    go.Scatter(x=list(py.Date2), y=list(df3[str(place)]))
    #go.Scatter(x=list(df3['Year']), y=list(df3[str(place)]))
)

# Set title
fig.update_layout(
    title_text= dynamicCountryTitle,
    xaxis_title="Year Range",yaxis_title="GDP"
    )

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="Last Month",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="Last 6 Months",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="Last Year",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)
fig.write_html(buffer)
html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()

# #data_linechart = [go.Scatter(x=line_df['Year'], y=line_df[str(place)], mode='lines', name= str(place))]

# Multi Line Chart

# multiline_df = df2
# multiline_df['Date'] = pd.to_datetime(multiline_df['Date'])
# trace1_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['Death'], mode='lines', name='Death')
# trace2_multiline = trace1_multiline#go.Scatter(x=multiline_df['Date'], y=multiline_df['Recovered'], mode='lines', name='Recovered')
# trace3_multiline = trace1_multiline#go.Scatter(x=multiline_df['Date'], y=multiline_df['Unrecovered'], mode='lines', name='Under Treatment')
# data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]



# Layout
app.layout = html.Div(children=[
    html.H1(children='Prototype',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Graphical rendering of GDP of selected country', style={'textAlign': 'center'}),
    html.Br(),

    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the GDP of the selected country between 1960 to 2019.'),

    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'United States', 'value': 'United States'},
            {'label': 'Aruba', 'value': 'Aruba'},
            {'label': 'Afghanistan', 'value': 'Afghanistan'}
        ],
        placeholder="Select Country"
    ),

    dcc.Graph(id="graph", figure=fig),
    html.Div(id='output-container-range-slider')
    #           ),
    # html.Hr(style={'color': '#7FDBFF'}),
    # html.H3('Multi Line chart', style={'color': '#df1e56'}),
    # html.Div(
    #     'This line chart represent the CoronaVirus death, recovered and under treatment cases of all reported cases in the given period.'),
    # dcc.Graph(id='graph5',
    #           figure={
    #               'data': data_multiline,
    #               'layout': go.Layout(
    #                   title='Corona Virus Death, Recovered and under treatment Cases From 2020-01-22 to 2020-03-17',
    #               xaxis={'title': 'Date'}, yaxis={'title': 'Number of cases'})
    #           }
    #           )

])


@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_figure(value):
    dynamicCountryTitle = 'GDP of ' + str(value) + ' From 1960 to 2019'

    layout = go.Layout(title=str(value),
                       xaxis_title="Year Range",
                       yaxis_title="GDP")
    # create figure
    fig = go.Figure(layout=layout)

    # create trace
    fig.add_trace(
        go.Scatter(x=list(py.Date2), y=list(df3[str(value)]))
        #go.Scatter(x=list(df3['Year']), y=list(df3[str(value)]))
    )

    # Set title
    fig.update_layout(
        title_text= dynamicCountryTitle
    )

    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="Last Month",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="Last 6 Months",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="Last Year",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )

    fig.write_html(buffer)

    html_bytes = buffer.getvalue().encode()
    encoded = b64encode(html_bytes).decode()
    return fig


@app.callback(
    dash.dependencies.Output('output-container-range-slider', 'children'),
    [dash.dependencies.Input('FirstSlider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server()