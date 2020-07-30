import dash
import dash_core_components as dcc 
import dash_html_components as html
import dash_bootstrap_components as dbc
from utilities import utilities, donuts, line, table

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        # Top row
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1('STACK VALUE TRACKER'),
                        html.H2('Visualizing my precious metal stack with Python and Plotly Dash'),
                        html.Hr()
                    ]
                )
            ]
        ),
        # Middle row
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            className='div-for-table',                                                       
                            children=[
                                table.generate_table(table.df)
                            ], 
                            style={
                                'display': 'inline-block', 
                                'height': '265px', 
                                'overflow': 'auto'
                            }
                        )
                    ], 
                    width=6
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dcc.Graph(
                                    figure=donuts.buy, 
                                    style={
                                        'width': '50%', 
                                        'display': 'inline-block'
                                    }
                                ),
                                dcc.Graph(
                                    figure=donuts.spot, 
                                    style={
                                        'width': '50%', 
                                        'display': 'inline-block'
                                    }
                                ),  
                            ], 
                            style={
                                'height': '100%'
                            }
                        )
                    ], 
                    width=6
                )
            ], 
            style={
                'height': '30%'
            }
        ),
        # Bottom row
        dcc.Tabs(
            id='tabls-with-classes',
            parent_className='custom-tabs',
            className='custom-tabs-container',
            children=[
                dcc.Tab(
                    label='Gold',
                    className='custom-tab',
                    selected_className='custom-tab--gold',
                    children=[
                        dcc.Graph(figure=line.gold, style={'width': '100%'})
                    ]
                ),
                dcc.Tab(
                    label='Silver',
                    className='custom-tab',
                    selected_className='custom-tab--silver', 
                    children=[
                        dcc.Graph(figure=line.silver, style={'width': '100%'})
                    ]
                )
            ]
        )
    ], 
    style={
        'height': '100vh'
    }
)

if __name__ == '__main__':
    app.run_server(port=8050, debug=True)