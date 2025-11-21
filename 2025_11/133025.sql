select i.FLAVOR
from first_half as f
join icecream_info as i
on i.flavor = f.flavor
where total_order >= 3000 and INGREDIENT_TYPE = 'fruit_based'
order by total_order desc
