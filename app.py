import dash
import dash_table
import dash_core_components as dcc 
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

# Load data
df = pd.read_csv('data/holdings.csv')

colors = ['gold', 'silver']

line = go.Figure(data=[go.Scatter(x=df['Purchase Date'],y=df['Purchase Price'],connectgaps=True)])
line.update_layout(title='Historical Value',template='plotly_white',showlegend=False)

pie = go.Figure(data=[go.Pie(labels=df['Type'],values=df['Purchase Price'],textinfo='label+percent',marker=dict(colors=colors))])
pie.update_layout(title='Gold to Silver Ratio',template='plotly_white',showlegend=False)

table = dbc.Table.from_dataframe(df)

graphs = html.Div([
    dbc.Row([
            dbc.Col(dcc.Graph(figure=line)),
            dbc.Col(dcc.Graph(figure=pie)),
    ])])

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([   
        html.H1('STACK VALUE TRACKER'),
        html.P('Visualizing my precious metal stack with Python and Plotly Dash.'),
        html.Hr(),
        dbc.Row([dbc.Col(graphs)], align='center'),
        dbc.Row([dbc.Col(table)], align='center'), 
], fluid=True,)

if __name__ == '__main__':
    app.run_server(port=8050, debug=True)