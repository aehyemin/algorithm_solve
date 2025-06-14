SELECT 
left(product_code, 2) as category, count(product_id)
from product
group by category
order by product_code