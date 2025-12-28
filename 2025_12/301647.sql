select b.ID, b.GENOTYPE, a.GENOTYPE as PARENT_GENOTYPE
from ecoli_data as a
join ecoli_data as b
on a.ID = b.parent_id
where (a.genotype & b.genotype) = a.genotype
order by b.id 
