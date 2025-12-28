select 
    year(differentiation_date) as YEAR,
    (max(size_of_colony) over (partition by year(differentiation_date)) - size_of_colony) as YEAR_DEV,
    ID
from ecoli_data
order by YEAR, YEAR_DEV 
