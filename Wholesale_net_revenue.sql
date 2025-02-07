-- Finding out how much Wholesale net revenue each product_line generated per month per warehouse in the dataset.

SELECT warehouse,
		product_line, 
		to_char(date, 'Month') as month ,
		sum(total) - sum(payment_fee) as net_revenue
from sales 
where client_type = 'Wholesale'
group by product_line, to_char(date, 'Month'), payment, warehouse
order by warehouse, product_line, min(date), net_revenue desc
