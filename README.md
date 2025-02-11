# E-commerce Sales Analysis

## Project Overview
This project analyzes an **E-commerce Sales Dataset** stored in **PostgreSQL**.  
It includes **trend analysis, product insights, and customer behavior analysis** using **Python, Pandas, Matplotlib, and Seaborn**.

### **Key Features:**
-  **Monthly Sales Trend Analysis**
-  **Top-Selling Products Identification**
-  **Country-Wise Sales Distribution**
-  **Revenue vs. Sales Volume Trends**
-  **Seasonality & Customer Behavior Analysis**

---

##  **Dataset Description**
The dataset contains **transactional sales data** with the following columns:

| Column Name  | Description |
|-------------|------------|
| `InvoiceNo` | Unique transaction ID |
| `StockCode` | Product identifier |
| `Description` | Product name |
| `Quantity` | Number of units sold |
| `InvoiceDate` | Date & time of purchase |
| `UnitPrice` | Price per unit |
| `CustomerID` | Unique customer identifier |
| `Country` | Country where purchase was made |

 **Source:** Sample e-commerce dataset (converted from CSV to PostgreSQL).

---

##  **Installation & Setup**
### **1️ Install Dependencies**
Ensure you have **Python and PostgreSQL installed**, then install required libraries:

```sh
pip install pandas psycopg2 matplotlib seaborn



Setup PostgreSQL Database
Open pgAdmin 4 and create a new database:

CREATE DATABASE ecommerce_db;
Create a table in PostgreSQL:

CREATE TABLE ecommerce_sales (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INT,
    InvoiceDate TIMESTAMP,
    UnitPrice NUMERIC(10,2),
    CustomerID VARCHAR(20),
    Country VARCHAR(100)
);
Import the CSV file using pgAdmin’s Import/Export tool.
Usage
1️Connect to PostgreSQL & Load Data
Run the following Python script to connect and fetch data:

import psycopg2
import pandas as pd

conn = psycopg2.connect(
    dbname="ecommerce_db",
    user=" ",
    password="your_password",
    host=" ",
    port=" "
)

query = "SELECT * FROM ecommerce_sales;"
df = pd.read_sql(query, conn)
conn.close()
2️ Visualize Monthly Sales Trends
import matplotlib.pyplot as plt
import seaborn as sns

df['invoicedate'] = pd.to_datetime(df['invoicedate'])
df['month'] = df['invoicedate'].dt.to_period('M')
monthly_sales = df.groupby(df['month'].astype(str))['quantity'].sum().reset_index()

plt.figure(figsize=(12,5))
sns.lineplot(data=monthly_sales, x="month", y="quantity", marker="o")
plt.xticks(rotation=45)
plt.title(" Monthly Sales Trend")
plt.show()
3️ Find Top-Selling Products
top_products = df.groupby('description')['quantity'].sum().nlargest(10).reset_index()

plt.figure(figsize=(12,5))
sns.barplot(data=top_products, x="quantity", y="description", palette="Blues_r")
plt.title(" Top 10 Best-Selling Products")
plt.xlabel("Total Sold")
plt.ylabel("Product Name")
plt.show()
 Key Insights from Analysis
 Sales Increased Steadily in 2011: The dataset shows an upward sales trend, peaking in November 2011.
 High Sales in November 2011: Likely due to Black Friday or holiday shopping season.
 Sharp Drop in December: Suggests either missing data or a post-holiday slowdown.
 Most Popular Products: The top-selling items are gift items, home decor, and seasonal products.
 Major Markets: The highest sales are from the UK, Germany, and France.
