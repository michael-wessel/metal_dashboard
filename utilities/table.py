import dash_html_components as html
from utilities import utilities

df = utilities.df[['Description', 'Mint Year', 'Purchase Price', 'Weight', 'Spot Price']]
# TODO: Format currency columns

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