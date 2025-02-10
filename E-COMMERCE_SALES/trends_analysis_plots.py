#connected Python to PostgreSQL and fetch data:'''


import psycopg2
import pandas as pd

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="ecommerce_db",
    user="postgres",
    password="Cokolwiek@123",
    host="localhost",
    port="5432"
)

# Loaded data into a Pandas DataFrame
query = "SELECT * FROM ecommerce_sales ;"
df = pd.read_sql(query, conn)

# Closed connection
conn.close()

# Showed first rows
print(df.head())

#Visualizing Trends
#Monthly Sales Trend

import matplotlib.pyplot as plt
import seaborn as sns

# Convert InvoiceDate to datetime
df['invoicedate'] = pd.to_datetime(df['invoicedate'])

# Extract year-month properly
df['month'] = df['invoicedate'].dt.to_period('M')
 
# Group by month 
monthly_sales = df.groupby(df['month'].astype(str))['quantity'].sum().reset_index()

# Ensuring data is not empty
print(monthly_sales)

# Plot the corrected trend
plt.figure(figsize=(12,5))
sns.lineplot(data=monthly_sales, x="month", y="quantity", marker="o")

plt.title("📈 Monthly Sales Trend")
plt.xticks(rotation=45)
#plt.show()


"""
✅ Sales Growth: The trend is increasing throughout 2011.
✅ Peak Sales in November 2011: Highest quantity sold in November → Black Friday, Holiday Season?
✅ Sharp Drop in December 2011: Possibly incomplete data for December, or seasonal demand drop after the holiday rush.
"""

print(df[df['month'] == '2011-12']['invoicedate'].max())  # Latest date in December

#Identifying Top-Selling Products by Month
top_products = df.groupby(['month', 'description'])['quantity'].sum().reset_index()
top_products = top_products.sort_values(by=['month', 'quantity'], ascending=[True, False])

# Show top 5 products per month
top_products.groupby('month').head(5)

#Analyze Seasonal Trends
#Plot monthly revenue instead of quantity:

df['revenue'] = df['quantity'] * df['unitprice']
monthly_revenue = df.groupby(df['month'].astype(str))['revenue'].sum().reset_index()

plt.figure(figsize=(12,5))
sns.lineplot(data=monthly_revenue, x="month", y="revenue", marker="o")
plt.xticks(rotation=45)
plt.title("💰 Monthly Revenue Trend")
#plt.show()

#Finding Which Countries Contributed Most to Sales
country_sales = df.groupby('country')['quantity'].sum().nlargest(10).reset_index()

plt.figure(figsize=(12,5))
sns.barplot(data=country_sales, x="quantity", y="country", palette="Blues_r")
plt.title("🌎 Top 10 Countries by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Country")
plt.show()


""" CONCLUSIONS
1️ Sales Show an Upward Trend Throughout 2011
Sales steadily increase from January to November 2011, showing a strong growth trend.
This suggests that the business is expanding or gaining more customers over time.
Possible causes: Marketing efforts, increased product demand, or seasonal shopping cycles.
2️ Peak Sales in November 2011 – Likely Black Friday or Holiday Shopping
November shows the highest number of sales, significantly higher than any previous month.
Possible reasons:
Black Friday & Christmas shopping period (huge consumer spending).
Discounts or promotions driving more sales.
Popular seasonal products (e.g., Christmas decorations, gifts) selling in bulk.
3️ Sharp Drop in December 2011 – Possible Missing Data or Post-Holiday Effect
December sales plummet drastically compared to November.
Two possible explanations:
Data might be incomplete for December (needs verification).
Post-holiday drop: Consumers buy more in November and slow down in December after holiday shopping.
Action: Check the dataset for missing records in December.
4️ Fluctuations in Mid-Year Sales – Signs of Seasonality?
Some months (e.g., March, May, July) show temporary spikes, while others dip.
This suggests that certain months have naturally higher demand.
Possible causes:
Product seasonality – Some items sell better in specific months.
Sales promotions/events – Discounts or special events may have boosted sales in certain months.
"""
