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
df4 = pd.read_csv('PopGlobal.csv')
df5 = pd.read_csv('DeathRateGlobal.csv')
df6 = pd.read_csv('LifeExpectancyGlobal.csv')

buffer = io.StringIO()
app = dash.Dash()
available_countries = df2['Country Name'].unique()

#Date:str
#Ensure Date Range
py.Date2 = [0] * 60
dummy = 0
for i in range(1960, 2020):
    py.Date2 [dummy] = i
    dummy = dummy + 1

place = 'None' #United States'
dynamicCountryTitle ='' #= 'GDP of ' + str(place)
layout = go.Layout(xaxis_title="Year Range",yaxis_title="GDP")

#create figure
fig = go.Figure()
#create trace
fig.add_trace(
    go.Scatter(x=list(py.Date2), y=list(df3[str(place)]))
)

# Set title
fig.update_layout(
    title_text= dynamicCountryTitle,
    xaxis_title="Year Range", yaxis_title="GDP"
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
        title="Drag & Zoom Slide-bar",
        type="date"
    )
)
fig.write_html(buffer)
html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()

# Layout
app.layout = html.Div(children=[
    html.H1(children='Global Data Project',
            style={
                'text-indent' : '90px',
                'textAlign': 'left',
                'color': '#00B200'
            }
            ),
    html.Div('Data Visualization Dashboard using Python', style={'textAlign': 'left','text-indent' : '90px'}),
    html.Div('Graphical Comparision and Rending of Data Between Up to Two Countries', style={'textAlign': 'left','text-indent' : '90px'}),
    html.Br(),

    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Data Visualization Chart', style={'color': '#00B200', 'text-indent' : '90px'}),
    html.Div('This line chart compares two countries by the specified parameter between the years of 1960 and 2019.',style={'text-indent' : '90px'}),
    dcc.Dropdown(
        id='country-dropdown1',
        options=[{'label': i, 'value': i} for i in available_countries],
        placeholder="Select Country 1",
        style = dict(left = '90px', width='300px', display = 'inline-block', float = 'auto')
    ),
    dcc.Dropdown(
        id='country-dropdown2',
        options=[{'label': i, 'value': i} for i in available_countries],
        placeholder="Select Country 2",
        style = dict(width='300px', display = 'inline-block', float = 'auto', left = '90px'),
    ),

    dcc.Dropdown(
        id='yaxis-dropdown',
        options=[
            {'label': 'GDP', 'value': 'df3',},
            {'label': 'Population', 'value': 'df4'},
            {'label': 'Death Rate', 'value': 'df5'},
            {'label': 'Life Expectancy', 'value': 'df6'},

        ],
        placeholder="Select Data List",
        style=dict(width='300px', display='inline-block', float='auto',left = '90px'),
        value ='df3',

    ),
    dcc.Graph(id="graph", figure=fig),
    html.Div(id='output-container-range-slider'),
    html.Hr(),
])


@app.callback(
    Output('graph', 'figure'),
    Input('country-dropdown1', 'value'),
    Input('country-dropdown2', 'value'),
    Input('yaxis-dropdown', 'value'),
)


def update_graph(countryonevalue, countrytwovalue, yaxisvalue):


    # Check for Database Input
    if(str(yaxisvalue) == "df4"):
        database = "Population"
    elif(str(yaxisvalue) == "df5"):
        database = "Death Rate"
    elif(str(yaxisvalue) == "df6"):
        database = "Life Expectancy"
    else:
        database = "GDP"

    #Check for Country Input
    if ( (countryonevalue == 'None' or countryonevalue == None) and (countrytwovalue == 'None' or countrytwovalue == None) ):
        dynamicCountryTitle = database + ' comparison of ' + '[No Country Selected]'
    elif(countrytwovalue == 'None' or countrytwovalue == None):
        dynamicCountryTitle = database + ' comparison of ' + str(countryonevalue)
    elif ( countrytwovalue != 'None' and (countryonevalue == 'None' or countryonevalue == None) ):
        dynamicCountryTitle = database + ' comparison of ' + str(countrytwovalue)
    else:
        dynamicCountryTitle = database + ' comparison of ' + str(countryonevalue) + ' and ' + str(countrytwovalue)


    layout = go.Layout(title=dynamicCountryTitle, yaxis_title = database)
    # create figure
    fig = go.Figure(layout=layout)

    # create trace based on variable
    database = "GDP"
    if (str(yaxisvalue) == "df4"):
        database = "Population"
        fig.add_trace(
            go.Scatter(x=list(py.Date2), y=list(df4[str(countryonevalue)]), name=str(countryonevalue))
        )
        fig.add_trace(
            go.Scatter(x=list(py.Date2), y=list(df4[str(countrytwovalue)]), name=str(countrytwovalue))
        )
    elif (str(yaxisvalue) == "df5"):
        database = "Death Rate"
        fig.add_trace(
            go.Scatter(x=list(py.Date2), y=list(df5[str(countryonevalue)]), name=str(countryonevalue))
        )
        fig.add_trace(
            go.Scatter(x=list(py.Date2), y=list(df5[str(countrytwovalue)]), name=str(countrytwovalue))
        )
    elif (str(yaxisvalue) == "df6"):
        database = "Life Expectancy"
        fig.add_trace(
            go.Scatter(x=list(py.Date2), y=list(df6[str(countryonevalue)]), name=str(countryonevalue))
        )
        fig.add_trace(
            go.Scatter(x=list(py.Date2), y=list(df6[str(countrytwovalue)]), name=str(countrytwovalue))
        )
    else:
        fig.add_trace(
            go.Scatter(x=list(py.Date2), y=list(df3[str(countryonevalue)]), name=str(countryonevalue))
        )
        fig.add_trace(
            go.Scatter(x=list(py.Date2), y=list(df3[str(countrytwovalue)]), name=str(countrytwovalue))
        )


    # Set title
    fig.update_layout(
        title=dynamicCountryTitle,
        yaxis_title=database
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
            title="Drag & Zoom Slide-bar",
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