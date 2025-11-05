select i.ANIMAL_ID, i.NAME
from animal_ins as i
join animal_outs as o
on o.animal_id = i.animal_id
order by o.datetime - i.datetime desc
limit 2
