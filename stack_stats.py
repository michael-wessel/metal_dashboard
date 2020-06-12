import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 

# Load data.
df = pd.read_csv('data/holdings.csv')

# # Function to format the purchase price column to currancy.
# df['Value'] = df['Purchase Price'].apply(lambda x: '${:,.2f}'.format(x))

# Subset the data based on metal type.
gold = df[df.Type == 'Gold']
silver = df[df.Type == 'Silver']

# Gold stats.
gold_value = '${:,.2f}'.format(gold['Purchase Price'].sum())
gold_quantity = gold['Quantity'].sum()
gold_weight = ((gold['Quantity'] * gold['Troy Ounces']).sum())

# Silver stats.
silver_value = '${:,.2f}'.format(silver['Purchase Price'].sum())
silver_quantity = silver['Quantity'].sum()
silver_weight = ((silver['Quantity'] * silver['Troy Ounces']).sum())

# Stack stats
stack_value = '${:,.2f}'.format(df['Purchase Price'].sum())

print('Gold value:', gold_value)
print('Silver value:', silver_value)
print('Stack value:', stack_value)