select p.PRODUCT_ID, p.PRODUCT_NAME, sum(p.price * o.amount) as TOTAL_SALES
from food_product as p
join food_order as o
on p.product_id = o.product_id
where date_format(o.produce_date, '%Y-%m') = '2022-05'
group by p.product_name, p.product_id
order by TOTAL_SALES desc, p.product_id
