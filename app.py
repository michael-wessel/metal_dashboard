import dash
import dash_table
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly import express as px
import pandas as pd

# Load data
df = pd.read_csv('C:/Users/mwessel001/Projects/holdings/data/holdings.csv')
# Format 'Purchase Price' column to USD    
df['Purchase Price']=df['Purchase Price'].map('${0:,.2f}'.format)

external_stylesheets = ['assets/style.css']

colors = {
    'background': "#31302F",
    'text': '#ffffff'
}

markdown_text='''
### Summary Statistics Placeholder

* Live Spot Prices?
* Overall Stack Value
* Gold Ounces and Price/Ozt
* Silver Ounces and Price/Ozt
'''


pie = px.pie(df, 
    values='Purchase Price', 
    names='Type',
    hover_data=['Type'],
    labels={
        'Type': 'Metal Type',
        'Purchase Price': 'Purchase Price (USD)'
    },
    color='Type',
    color_discrete_map={
        'Silver':'silver',
        'Gold':'gold'
    }
)

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    children=[
        html.Div(className='row',
            children=[
                html.Div(className='three columns div-user-controls',
                    children=[
                        html.H1('STACK VALUE TRACKER'),
                        html.P('Visualizing my precious metal stack using Python and Dash.'),
                        html.Div(
                            children=[
                                dcc.Markdown(
                                    markdown_text
                                )
                            ]
                        )
                    ]
                ),

                html.Div(className='nine columns div-for-charts bg-grey',
                    children=[
                        # html.Div(
                        #     dcc.Graph(figure=pie)   
                        # ),
                        html.Div(
                            dash_table.DataTable(
                                id='table',
                                data=df.to_dict('records'),
                                columns=[{'name':i, 'id': i} for i in df.columns],
                                style_as_list_view=True,
                                style_header={
                                    'backgroundColor': '#31302F',
                                    'fontWeight': 'bold'
                                },
                                style_cell={
                                    'font_family': 'roboto',
                                    'font_size': '12px',
                                    'backgroundColor': '#31302F',
                                    'color': '#ffffff'
                                },
                                style_cell_conditional=[
                                    {
                                    'if': {'column_id': 'Type'},
                                    'textAlign': 'left'
                                    },
                                    {
                                    'if': {'column_id': 'Description'},
                                    'textAlign': 'left'
                                    },
                                    {
                                    'if': {'column_id': 'Source'},
                                    'textAlign': 'left'
                                    }
                                ]
                            )
                        )                     
                    ]
                ),
                
            ]
        )
    ]
)


if __name__ == '__main__':
    app.run_server(port=8050, debug=True)