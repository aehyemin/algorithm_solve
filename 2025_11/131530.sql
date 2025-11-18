select floor(price / 10000) * 10000 as PRICE_GROUP, count(product_id) as PRODUCTS
from product
group by price_group
order by price_group
