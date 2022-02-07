import dash
from dash import dcc, html
import dash_daq as daq
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import datetime


from azure.cosmos import CosmosClient, PartitionKey, errors
import json


url = "https://ahmedbaioumy.documents.azure.com:443/"
key = "ES46Ho3VjTgp9HYh0E6CPq1vwiqVaC1D2815D2CZOPEmHghQ7iK1Idkgo5YJCQ29KEgCKScM5rqDs3fXG8LJKw=="
client = CosmosClient(url, credential=key)


database = client.get_database_client("CosmosWithIOT")
container = database.get_container_client("EgytrafoTest")


# intialise data of lists.
data = {"IDENTITYS"        :['1' , '2' , '3' , '4' ],
        "Productivity"     :[20  , 21  , 19  , 18  ],
        "Total_sheets"     :[3070, 3170, 3250, 4070],
        "Downtime"         :[1   , 5   , 10  , 15  ],
        "Setup_time"       :[5   , 10  , 15  , 20  ],
        "Maintenance_time" :[15  , 20  , 22  , 25  ],
        "Avalability"      :[85  , 90  , 92  , 95  ],
        "Non_run_time"     :[21  , 35  , 47  , 60  ],
        "Qaulity"          :[99  , 95  , 97  , 100 ],
        "Oee"              :[75  , 80  , 82  , 85  ],
        "Performance"      :[80  , 70  , 72  , 77  ],
        "Run_time"         :[100 , 99  , 90  , 85  ],
        "Date"             :['20220120', '20220120','20220120','20220120'],
        "Time"             :['00:10', '01:10', '02:10', '03:10'],
        "color"            :['green', 'green', 'red', 'green'],
    }
 
# Create DataFrame
dfff = pd.DataFrame(data)


#app = dash.Dash(__name__, assets_folder = 'assets', include_assets_files = True)
dash_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])#CYBORG LITERA DARKLY
app = dash_app.server

df1 = {"Total_Run_Time":["Run", "Maint", "Setup", "Down", "Break"],
       "Values"        :[100, 0, 0, 0, 0  ]
    }
df_RunTime = pd.DataFrame(df1)

fig2 = px.pie(df_RunTime, values='Values', names='Total_Run_Time', title="Total Run Time")
fig2.update_layout(
    autosize=False,
    width=335,
    height=335,
    margin=dict(l=1, r=1, t=25, b=1),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color="#00ced1",
)

df2 = {"Total_Pieces" :["Good", "Bad"],
       "Values"        :[100, 0]
    }
df_Pieces = pd.DataFrame(df2)

fig3 = px.pie(df_Pieces, values='Values', names='Total_Pieces', title="Good Pieces/Bad Pieces")
fig3.update_layout(
    autosize=False,
    width=300,
    height=300,
    margin=dict(l=1, r=1, t=25, b=1),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color="#00ced1",
)

df = px.data.stocks()
fig1 = px.line(dfff, x='Time', y="Oee")
fig1.update_traces(line_color='#00ced1', mode='markers+lines', marker = dict(
                             size=10,
                             color = dfff["color"]
                         ))
fig1.update_layout(
    autosize=False,
    width=650,
    height=250,
    margin=dict(l=1, r=1, t=1, b=1),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color="#00ced1",
    yaxis_range=[0,100],
    xaxis=dict(
         showgrid=False,),
         
    yaxis=dict(
         showgrid=False,)
         
    #    title_text="Y",
    #    tickmode="array",
    #    titlefont=dict(size=30),
    #)
)

dash_app.layout = html.Div(
                       
            className="content",
            children=[
                html.H1(children='Tatbeek for Digital Solutions'),
                html.H5(children='Live Machine Dashboard.'),
                
                html.Div(
                    className="date",
                    id = 'Time',
                    children=[
                        html.H6(
                            datetime.datetime.now().strftime('%Y-%m-%d'), 
                            style={'opacity': '1', 'fontSize': 12}),
                        html.H6(
                            datetime.datetime.now().strftime('%H:%M:%S'), 
                            style={'opacity': '1', 'fontSize': 12}),
                    ],        
                ),
                html.Div(
                    className="Shift_Time",
                    children=[
                        html.H6(
                            children='Shift Time: 08:00PM - 08:00AM',)
                    ],        
                ),
            
                html.Div(
                    children=[
                        daq.Gauge(
                            className="OEE",
                            id='OEE_Gauge',
                            label={
                                'label': 'OEE',
                                'style': {
                                    'color': "#00ced1",
                                    'fontSize': 24
                                },
                            },
                            value= 70,
                            max = 100,
                            min = 0,
                            size = 200,
                            units='%',
                            showCurrentValue=True,
                            color={
                                "gradient": True,
                                "ranges": {
                                    "red": [0, 70],
                                    "yellow": [70, 80],
                                    "green": [80, 100]
                                },
                            },        
                        ),
                        daq.Gauge(
                            className="Pice_per_Min",
                            id='Pice_per_Min',
                            label={
                                'label': 'Piece/Min',
                                'style': {
                                    'color': "#00ced1",
                                    'fontSize': 24
                                },
                            },
                            value= 70,
                            max = 100,
                            min = 0,
                            size = 200,
                            #units='%',
                            showCurrentValue=True,
                            color={
                                "gradient": True,
                                "ranges": {
                                    "red": [0, 70],
                                    "yellow": [70, 80],
                                    "green": [80, 100]
                                },
                            },        
                        ),
                        daq.Gauge(
                        className="Performance",
                        id='Performance_Gauge',
                        label={
                            'label': 'Performance',
                            'style': {
                                'color': "#00ced1",
                                'fontSize': 24
                            },
                        },
                        value= 70,
                        max = 100,
                        min = 0,
                        size = 190,
                        units='%',
                        showCurrentValue=True,
                        color={
                            "gradient": True,
                            "ranges": {
                                "red": [0, 70],
                                "yellow": [70, 80],
                                "green": [80, 100]
                            },
                        },        
                        ),
                        daq.Gauge(
                        className="Avalability",
                        id='Avalability_Gauge',
                        label={
                            'label': 'Avalability',
                            'style': {
                                'color': "#00ced1",
                                'fontSize': 24
                            },
                        },
                        value= 70,
                        max = 100,
                        min = 0,
                        size = 190,
                        units='%',
                        showCurrentValue=True,
                        color={
                            "gradient": True,
                            "ranges": {
                                "red": [0, 70],
                                "yellow": [70, 80],
                                "green": [80, 100]
                            },
                        },        
                    ),
                    
                    daq.Gauge(
                        className="Quality",
                        id='Quality_Gauge',
                        label={
                            'label': 'Quality',
                            'style': {
                                'color': "#00ced1",
                                'fontSize': 24
                            },
                        },
                        value= 70,
                        max = 100,
                        min = 0,
                        size = 190,
                        units='%',
                        showCurrentValue=True,
                        color={
                            "gradient": True,
                            "ranges": {
                                "red": [0, 70],
                                "yellow": [70, 80],
                                "green": [80, 100]
                            },
                        },        
                    ),
                    
                    dbc.Progress(
                        value=25, 
                        color="info", 
                        className="Productivity",
                        id='Productivity_Progress',
                        style={"height": "45px",
                                "width": "650px"},
                        label=f"Production: 100 Piece, 25%",
                        striped=True,
                        max =100,
                        min=0,
                        animated= True,
                    ),
                    dcc.Graph(
                        figure=fig1,
                        className="Line",
                        id='Line_Chart',
                        
                    ),
                    
                    dcc.Graph(
                        figure=fig2,
                        className="Run_Time",
                        id='Run_Time_Chart',
                        
                    ),
                    
                    dcc.Graph(
                        figure=fig3,
                        className="Errors",
                        id='Errors_Chart',
                        
                    ),
                    
                    dcc.Interval(
                        id='interval_component',
                        interval=50*1000, # in milliseconds
                        n_intervals=0
                    ),
                    
                    dcc.Interval(
                        id='interval_Time',
                        interval=50*1000, # in milliseconds
                        n_intervals=0
                    )
                    
                    ]
                ),    
                
            ],
)

def Read_Database():
    for item in container.query_items(
                        query='SELECT Top 1 * FROM c ORDER BY c.IDENTITYS DESC',
                        enable_cross_partition_query=True):
        data = (json.dumps(item, indent=True))
        
        data_to_json = json.loads(data)
        data_to_pd = pd.json_normalize(data_to_json)
        return data_to_pd

def Read_Database_for_Graph():
    data_100=[]
    for item in container.query_items(
                        query='SELECT Top 100 * FROM c ORDER BY c.IDENTITYS DESC',
                        enable_cross_partition_query=True):
        data = (json.dumps(item, indent=True))
        data_to_json = json.loads(data)
        data_100.append(data_to_json)
    
    data_to_pd = pd.json_normalize(data_100)
    data_to_pd = data_to_pd.iloc[::-1]
    return data_to_pd
        
@dash_app.callback(Output('OEE_Gauge', 'value'), 
              Input('interval_component', 'n_intervals'))
def update_OEE(n):
    
    data = Read_Database()
    _OEE = data["Oee"]
    value = float((_OEE[0]))
    return value
    
@dash_app.callback(Output('Performance_Gauge', 'value'), 
              Input('interval_component', 'n_intervals'))
def update_Performance(n):
    
    data = Read_Database()
    _Performance = data["Performance"]
    value = float((_Performance[0]))
    return value

@dash_app.callback(Output('Avalability_Gauge', 'value'), 
              Input('interval_component', 'n_intervals'))
def update_Avalability(n):
    
    data = Read_Database()
    _Avalability = data["Avalability"]
    value = float((_Avalability[0]))
    return value
    
    
@dash_app.callback(Output('Quality_Gauge', 'value'), 
              Input('interval_component', 'n_intervals'))
def update_Qaulity(n):
    
    data = Read_Database()
    _Quality = data["Qaulity"]
    value = float((_Quality[0]))
    return value
    
    
@dash_app.callback(
              [Output('Productivity_Progress', 'value'), Output('Productivity_Progress', 'label')], 
              [Input('interval_component', 'n_intervals')],
            )
def update_Productivity(n):
    
    data = Read_Database()
    _Productivity = data["Productivity"]
    _Total_sheets = data["Total_sheets"]
    sheets = float(_Total_sheets[0])
    value = int((_Productivity[0]))
    return value, f"Production: {sheets} Piece, {value}%"

@dash_app.callback(Output('Pice_per_Min', 'value'), 
              Input('interval_component', 'n_intervals'))
def update_Pice_per_Min(n):
    
    data = Read_Database()
    _Total_sheets = data["Total_sheets"]
    _Run_time = data["Run_time"]
    pi_min = float(_Total_sheets[0])/(float(_Run_time[0]))
    value = float((pi_min))
    return value
    
@dash_app.callback(Output('Run_Time_Chart', 'figure'), 
              Input('interval_component', 'n_intervals'))
def update_Run_Time_Chart(n):
    
    data = Read_Database()
    
    _Run = (data["Run_time"])
    _Mai = (data["Maintenance_time"])
    _Set = (data["Setup_time"])
    _Dow = (data["Downtime"])
    
    new_data = {"Total_Run_Time":["Run", "Maint", "Setup", "Down", "Break"],
                "Values"        :[_Run[0], _Mai[0], _Set[0], _Dow[0], 0  ]
    }
 
    df_RunTime = pd.DataFrame(new_data)

    x = px.pie(df_RunTime, values='Values', names='Total_Run_Time', title="Total Run Time")
    x.update_layout(
        autosize=False,
        width=335,
        height=335,
        margin=dict(l=1, r=1, t=25, b=1),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="#00ced1",
    )
    return (x)

@dash_app.callback(Output('Errors_Chart', 'figure'), 
              Input('interval_component', 'n_intervals'))
def update_Errors_Chart(n):
    
    data = Read_Database()
    
    _Good = (data["Total_sheets"])
       
    df2 = {"Total_Pieces" :["Good", "Bad"],
           "Values"        :[_Good[0], 0]
    }
    
    df_Pieces = pd.DataFrame(df2)
    
    x = px.pie(df_Pieces, values='Values', names='Total_Pieces', title="Good Pieces/Bad Pieces")
    x.update_layout(
        autosize=False,
        width=300,
        height=300,
        margin=dict(l=1, r=1, t=25, b=1),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="#00ced1",
    )
    return (x)

@dash_app.callback(Output('Line_Chart', 'figure'), 
              Input('interval_component', 'n_intervals'))
def update_Line_Chart(n):
    
    def Label_Color (row):
        if row['Oee'] > 80 :
            return 'green'
        if row['Oee'] <= 80 and row['Oee']>= 70 :
            return 'yellow'
        if row['Oee'] < 70 :
            return 'red'
   
    data = Read_Database_for_Graph()
    
    data["Oee"] = pd.to_numeric(data["Oee"])
    data["Color"] = data.apply (lambda row: Label_Color(row), axis=1)
    
    x = px.line(data, x='Time', y="Oee")
    x.update_traces(line_color='#00ced1')
    x.update_traces(line_color='#00ced1', 
                    mode='markers+lines', 
                    marker = dict(
                                size=10,
                                color = data["Color"]
                            )
    )
    x.update_layout(
        autosize=False,
        width=650,
        height=250,
        margin=dict(l=1, r=1, t=1, b=1),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="#00ced1",
        yaxis_range=[0,100],
        xaxis=dict(
            showgrid=False,),
            
        yaxis=dict(
            showgrid=False,
            title_text="OEE",)
        #    tickmode="array",
        #    titlefont=dict(size=30),
        #)
    )

    return (x)

@dash_app.callback(Output('Time', 'children'),
              Input('interval_Time', 'n_intervals'))
def update_date(n):
    
    x = [
    html.H6(datetime.datetime.now().strftime('%Y-%m-%d'), 
            style={'opacity': '1', 'fontSize': 12}),
    html.H6(datetime.datetime.now().strftime('%H:%M'), 
            style={'opacity': '1', 'fontSize': 12}),
    ]
                            
    return x#[html.P('Last updated ' +str(datetime.datetime.now()))]

if __name__ == '__main__':
    dash_app.run_server(debug=True)
    #server.run(host="0.0.0.0",port = 80, debug=True)
    #server.run(debug=True, host='0.0.0.0', port='80')
