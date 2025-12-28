select *
from ecoli_data as e
join (
    select 
    year(DIFFERENTIATION_DATE) as YEAR,
    max(size_of_colony) as max_size
    from ecoli_data
    group by year(DIFFERENTIATION_DATE)
    ) y
on y.year = year(e.DIFFERENTIATION_DATE)
