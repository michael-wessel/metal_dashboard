import dash
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly import express as px
import pandas as pd
import datetime

# Load data
df = pd.read_csv('data/holdings.csv')
df['purchase_date'] = pd.to_datetime(df['purchase_date'])

external_stylesheets = ['assets/style.css']

colors = {
    'background': "#31302F",
    'text': '#ffffff'
}

markdown_text='''
### Placeholder
Add some sort of filters or kpis here.
'''

   
pie = px.pie(df, 
    values='cost', 
    names='type',
    hover_data=['type'],
    labels={
        'type': 'Metal Type',
        'cost': 'Purchase Price (USD)'
    },
    color='type',
    color_discrete_map={
        'Silver':'silver',
        'Gold':'gold'
    }
)


def generate_table(dataframe, max_rows=5):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


# Initialize the app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    children=[
        html.Div(className='row',
            children=[
                html.Div(className='three columns div-user-controls',
                    children=[
                        html.H2('STACK VALUE TRACKER'),
                        html.P('Visualizing my precious metal stack using Python and Dash.'),
                        html.Div(
                            className='div-for-filters',
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
                        html.Div(
                            dcc.Graph(figure=pie)  
                        ),
                        html.Div(
                            generate_table(df)
                        )                     
                    ]
                ),
            ]
        )
    ]
)


if __name__ == '__main__':
    app.run_server(port=8050, debug=True)