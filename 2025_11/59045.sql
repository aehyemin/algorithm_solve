select i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
from animal_ins as i
join animal_outs as o
on o.animal_id = i.animal_id
where i.sex_upon_intake like 'Intact%'
and (o.sex_upon_outcome like 'Spayed%' or o.sex_upon_outcome like 'Neutered%')


# where (i.sex_upon_intake = 'Intact Male' or i.sex_upon_intake = 'Intact Female' )
# and (o.sex_upon_outcome = 'Spayed Female' or o.sex_upon_outcome = 'Neutered Male')
order by i.animal_id
