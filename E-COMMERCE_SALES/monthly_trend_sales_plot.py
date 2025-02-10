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
plt.show()


"""
✅ Sales Growth: The trend is increasing throughout 2011.
✅ Peak Sales in November 2011: Highest quantity sold in November → Black Friday, Holiday Season?
✅ Sharp Drop in December 2011: Possibly incomplete data for December, or seasonal demand drop after the holiday rush.
"""


