import dash_html_components as html
import dash_bootstrap_components as dbc
from utilities import utilities

df = utilities.df[['Description', 'Mint Year', 'Purchase Price', 'Weight', 'Spot Price']]
data = df.copy()

# Format currency columns
data['Purchase Price'] = data['Purchase Price'].map('${:,.2f}'.format)
data['Spot Price'] = data['Spot Price'].map('${:,.2f}'.format)

def generate_table(dataframe, max_rows=500):
    return html.Table(
        # Header
        [
            html.Tr(
                [
                    html.Th(col) for col in dataframe.columns
                ]
            ) 
        ] +
        # Body
        [
            html.Tr(
                [
                    html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ]
            ) for i in range(min(len(dataframe), max_rows))
        ]
    )

# Table for spot values
table_header = [
    html.Thead(
        html.Tr(
            [
                html.Th('Metric'),
                html.Th('Gold'), 
                html.Th('Silver')
            ]
        )
    )
]
b_e = html.Tr(
    [
        html.Td('B/E Spot'), 
        html.Td(utilities.gold_cost_per_ounce),
        html.Td(utilities.silver_cost_per_ounce),
    ]
)
spot = html.Tr(
    [
        html.Td('Spot'), 
        html.Td(utilities.gold_spot_price),
        html.Td(utilities.silver_spot_price)
    ]
)
delta = html.Tr(
    [
        html.Td('Delta'), 
        html.Td(utilities.gold_delta),
        html.Td(utilities.silver_delta)
    ]
)
table_body = [
    html.Tbody(
        [
            b_e, 
            spot, 
            delta
        ]
    )
]