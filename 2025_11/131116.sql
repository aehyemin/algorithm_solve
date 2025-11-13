select CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
from food_product
where (category, price) in (
    select category, max(price)
    from food_product
    group by category 
    having category in ('국', '김치', '식용유', '과자')
   
)
order by MAX_PRICE desc

