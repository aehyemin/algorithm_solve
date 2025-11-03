select p.PRODUCT_CODE, SUM(p.price * s.sales_amount) as SALES
from product as p
join offline_sale as s
on p.product_id = s.product_id
group by p.PRODUCT_CODE
order by SALES desc, p.product_code
