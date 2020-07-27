import pandas as pd
import numpy as np
from datetime import date, timedelta
import quandl

# API date range variables
today = date.today()
ten_years_ago = today - timedelta(days=10*365)

# API calls and spot variable creation
quandl.read_key()
gold_api = quandl.get("LBMA/GOLD.2", start_date=ten_years_ago, end_date=today)
gold_api.reset_index(level=0, inplace=True)
gold_spot = gold_api.loc[gold_api['Date'] == gold_api['Date'].max(), 'USD (PM)'].iloc[0]
silver_api = quandl.get("LBMA/SILVER.1", start_date=ten_years_ago, end_date=today)
silver_api.reset_index(level=0, inplace=True)
silver_spot = silver_api.loc[silver_api['Date'] == silver_api['Date'].max(), 'USD'].iloc[0]

# Read in my data and add a 'Spot Price' column
df = pd.read_csv('C:/Users/mwessel001/Projects/holdings/data/holdings.csv')
df['Weight'] = df['Troy Ounces'] * df['Quantity']
df['Spot Price'] = np.where(df['Type'] == 'Gold',
                                    df['Weight'] * gold_spot,
                                    df['Weight'] * silver_spot)

# Format values for donut charts
purchase_price = '${:,.2f}'.format(df['Purchase Price'].sum())
spot_price = '${:,.2f}'.format(df['Spot Price'].sum())
delta = ((df['Spot Price'].sum() - df['Purchase Price'].sum()) / df['Purchase Price'].sum())
gain_loss = "{:.2%}".format(delta)

def gain_loss_color(gain_loss):
    """ 
    Function to return a color for gain or loss.
    """
    if delta > 0:
        color = 'limegreen'
    else:
        color = 'red'
    return color

def gain_loss_text(gain_loss):
    """ 
    Function to return the formatted delta.
    """
    if delta > 0:
        symbol = '+'
    else:
        symbol = '-'
    return '(' + symbol + gain_loss + ')'