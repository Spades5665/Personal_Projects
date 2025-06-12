from preswald import connect, get_df
from preswald import query
from preswald import table, text
from preswald import plotly
import plotly.express as px


connect()  # Initialize connection to preswald.toml data sources
df = get_df("data/Fruit-Prices-2022.csv")  # Load data

sql = "SELECT Fruit, Yield FROM data/Fruit-Prices-2022.csv WHERE Yield = 0.9"
filtered_df = query(sql, "data/Fruit-Prices-2022.csv")

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

fig = px.scatter(df, x="Fruit", y="Yield")
plotly(fig)


'''
import preswald
import pandas as pd
import plotly.express as px

data = """Fruit,Form,RetailPrice,RetailPriceUnit,Yield,CupEquivalentSize,CupEquivalentUnit,CupEquivalentPrice
Apples,Fresh,1.8541,per pound,0.9,0.2425,pounds,0.4996
"Apples, applesauce",Canned,1.1705,per pound,1,0.5401,pounds,0.6323
"Apples, ready-to-drink",Juice,0.8699,per pint,1,8,fluid ounces,0.4349
"Apples, frozen concentrate",Juice,0.6086,per pint,1,8,fluid ounces,0.3043
Apricots,Fresh,3.6162,per pound,0.93,0.3638,pounds,1.4145"""

# Load data into DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data))

# Create plots
fig1 = px.bar(df, x='Fruit', y='RetailPrice', color='Form', title='Retail Price by Fruit and Form')
fig2 = px.scatter(df, x='Yield', y='CupEquivalentPrice', color='Fruit', size='CupEquivalentSize', title='Yield vs Cup Equivalent Price')
fig3 = px.line(df, x='Fruit', y='CupEquivalentSize', title='Cup Equivalent Size by Fruit')

# Display in app
preswald.text("# Fruit Price Report")
preswald.text("## Analysis of Fruit Prices and Yields")
preswald.text("This report provides insights into the retail prices and yields of various fruit forms.")
preswald.plotly(fig1)
preswald.plotly(fig2)
preswald.plotly(fig3)
'''