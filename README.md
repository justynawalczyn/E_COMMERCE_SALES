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
