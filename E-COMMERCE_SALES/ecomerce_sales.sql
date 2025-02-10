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

SELECT  * FROM ecommerce_sales LIMIT 100;

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'ecommerce_sales';

--Count total number of sales:
SELECT COUNT(*) FROM ecommerce_sales;
--Output: 541909

-- Finding the most sold products:
SELECT Description, SUM(Quantity) AS total_sold
FROM ecommerce_sales
GROUP BY Description
ORDER BY total_sold DESC
LIMIT 10;

--revenue by country
SELECT Country, SUM(Quantity * UnitPrice) AS total_revenue
FROM ecommerce_sales
GROUP BY Country
ORDER BY total_revenue DESC;

-- Monthly sales trend
SELECT DATE_TRUNC('month', InvoiceDate) AS month, SUM(Quantity) AS total_sales
FROM ecommerce_sales
GROUP BY month
ORDER BY month;

--Most Profitable Products
SELECT Description, SUM(Quantity * UnitPrice) AS revenue
FROM ecommerce_sales
GROUP BY Description
ORDER BY revenue DESC
LIMIT 10;

--Customer Segmentation (Top Buyers)
SELECT CustomerID, SUM(Quantity * UnitPrice) AS total_spent, COUNT(DISTINCT InvoiceNo) AS purchase_count
FROM ecommerce_sales
GROUP BY CustomerID
ORDER BY total_spent DESC
LIMIT 10;

--Monthly Revenue Trend
--Analysis how revenue changes over time:
SELECT DATE_TRUNC('month', InvoiceDate) AS month, SUM(Quantity * UnitPrice) AS revenue
FROM ecommerce_sales
GROUP BY month
ORDER BY month;

--Sales by Country (Market Insights)
SELECT Country, SUM(Quantity * UnitPrice) AS total_revenue, COUNT(DISTINCT CustomerID) AS unique_customers
FROM ecommerce_sales
GROUP BY Country
ORDER BY total_revenue DESC;




--CUSTOMER BEHAVIOUR ANALYSIS:
--Returning vs. New Customers -  how many customers made repeat purchases
SELECT CustomerID,
       COUNT(DISTINCT InvoiceNo) AS purchase_count,
       CASE 
           WHEN COUNT(DISTINCT InvoiceNo) > 1 THEN 'Returning Customer'
           ELSE 'New Customer'
       END AS customer_type
FROM ecommerce_sales
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY purchase_count DESC;

--Customer Retention Rate
--Checking how many customers return each month:
SELECT DATE_TRUNC('month', InvoiceDate) AS month, 
       COUNT(DISTINCT CustomerID) AS total_customers,
       COUNT(DISTINCT CASE WHEN CustomerID IN (
           SELECT DISTINCT CustomerID FROM ecommerce_sales WHERE InvoiceDate < '2011-12-01'
       ) THEN CustomerID END) AS returning_customers
FROM ecommerce_sales
GROUP BY month
ORDER BY month;


--Basket Analysis (Which Products Are Bought Together)
--Which products are often purchased in the same invoice:
SELECT a.Description AS Product_A, b.Description AS Product_B, COUNT(*) AS times_bought_together
FROM ecommerce_sales a
JOIN ecommerce_sales b ON a.InvoiceNo = b.InvoiceNo AND a.StockCode <> b.StockCode
GROUP BY Product_A, Product_B
ORDER BY times_bought_together DESC
LIMIT 10;



--PREDICTIVE & TREND ANALYSIS
--Find Seasonality in Sales
--Check which days of the week have the highest sales:
SELECT EXTRACT(DOW FROM InvoiceDate) AS day_of_week, 
       SUM(Quantity * UnitPrice) AS total_revenue
FROM ecommerce_sales
GROUP BY day_of_week
ORDER BY total_revenue DESC;

--Predict Future Revenue Using Moving Average
--Calculate 3-month moving average to smooth revenue trends:

SELECT DATE_TRUNC('month', InvoiceDate) AS month, 
       SUM(Quantity * UnitPrice) AS revenue,
       AVG(SUM(Quantity * UnitPrice)) OVER (ORDER BY DATE_TRUNC('month', InvoiceDate) ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg
FROM ecommerce_sales
GROUP BY month
ORDER BY month;


--Detect Anomalies in Sales
--Find days with unusually high sales (outliers detection):
WITH daily_sales AS (
    SELECT InvoiceDate::DATE AS sale_date, SUM(Quantity * UnitPrice) AS revenue
    FROM ecommerce_sales
    GROUP BY sale_date
)
SELECT sale_date, revenue
FROM daily_sales
WHERE revenue > (SELECT AVG(revenue) + 2 * STDDEV(revenue) FROM daily_sales)
ORDER BY revenue DESC;


