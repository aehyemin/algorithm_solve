select i.NAME, i.DATETIME
from ANIMAL_INS as i
left join animal_outs as a
on a.animal_id = i.animal_id
where a.datetime is null
order by i.datetime
limit 3
