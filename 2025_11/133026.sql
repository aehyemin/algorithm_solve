select i.INGREDIENT_TYPE, sum(total_order) as TOTAL_ORDER
from first_half as f
join icecream_info as i
on f.flavor = i.flavor
group by i.ingredient_type
