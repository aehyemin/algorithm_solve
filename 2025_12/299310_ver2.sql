select 
    year(DIFFERENTIATION_DATE) as YEAR,
    (select max(e2.size_of_colony)
    from ecoli_data e2
    where year(e2.DIFFERENTIATION_DATE) = year(e.DIFFERENTIATION_DATE) 
    ) - e.size_of_colony as YEAR_DEV,
    ID
from ecoli_data e
order by year, year_dev
