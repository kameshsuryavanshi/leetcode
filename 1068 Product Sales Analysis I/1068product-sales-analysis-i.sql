# Write your MySQL query statement below
Select Product.product_name ,Sales.year,Sales.price
from Sales
inner join Product on Sales.product_id = Product.product_id 