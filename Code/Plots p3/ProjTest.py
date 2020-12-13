import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import numpy as py
# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/DateRange.csv')
df2 = pd.read_csv('../Datasets/myData.csv')
df3 = pd.read_csv('../Datasets/GDPGlobal.csv')


app = dash.Dash()

# Line Chart
#1960 2019

#Date:str
py.Date2 = [0] * 60
dummy = 0
for i in range(1960, 2020):
    #py.Date2 [dummy] = i
    #dummy = dummy + 1
    #print( py.Date2[dummy] )
    print()#DO NOT COMMENT OUT THIS LINE


fuckThis = 11
if fuckThis == 0:
    place = 'Aruba'
elif fuckThis == 1:
    place= 'Afghanistan'
else:
    place = 'United States'

dynamicCountryTitle = 'GDP of ' + str(place) + ' From 1960 to 2020'

line_df = df3
data_linechart = [go.Scatter(x=line_df['Year'], y=line_df[str(place)], mode='lines', name= str(place))]
# #data_linechart = [go.Scatter(x=line_df['Year'], y=line_df[str(place)], mode='lines', name= str(place))]


###
# line_df = df2
# line_df2 = df1
# #line_df['Country Name'] = pd.to_datetime((line_df['Country Name'])
# data_linechart = [go.Scatter(x=line_df2['Year'], y=line_df['1960'], mode='lines', name='Death')]
# #data_linechart = [go.Scatter(x=line_df['Date'], y=line_df['Confirmed'], mode='lines', name='Death')]
###


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
    html.Div('This line chart represent the GDP of the selected country between 1960 to 2020.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title= dynamicCountryTitle,
                  #'layout': go.Layout(title='GDP of XXX From 1960 to 2020',
                                      xaxis={'title': 'Year'}, yaxis={'title': 'Estimated GDP'})
              }
              ),
    html.H3('Define Year Range', style={'color': '#df1e56'}),
    dcc.RangeSlider(
        id = 'FirstSlider',
        #marks={i: 'Label {}'.format(i) for i in range(1960, 2019)},
        marks={i: '{}'.format(i) for i in range(1960, 2020)},
        #count=5,
        min=1960,
        max=2019,
        step=5,
        value=[1960, 2019]
),
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


@app.callback(Output('graph1', 'figure'),
              [Input('select-continent', 'value')])
def update_figure(selected_continent):
    filtered_df = df1[df1['Continent'] == selected_continent]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    new_df = filtered_df.groupby(['Country'])['Confirmed'].sum().reset_index()
    new_df = new_df.sort_values(by=['Confirmed'], ascending=[False]).head(20)
    data_linechart = [go.Bar(x=new_df['Country'], y=new_df['Confirmed'])]
    return {'data': data_linechart, 'layout': go.Layout(title='Corona Virus Confirmed Cases in '+selected_continent,
                                                                   xaxis={'title': 'Country'},
                                                                   yaxis={'title': 'Number of confirmed cases'})}

@app.callback(
    dash.dependencies.Output('output-container-range-slider', 'children'),
    [dash.dependencies.Input('FirstSlider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server()
