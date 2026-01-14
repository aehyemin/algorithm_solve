#서브쿼리에서 분류하고 밖에서 출력
select d.id,
case when d.r > 0.75 then 'CRITICAL'
     when d.r > 0.5 then 'HIGH'
     when d.r > 0.25 then 'MEDIUM'
     else 'LOW'
end as COLONY_NAME
from (
    select id,
    percent_rank() over (order by size_of_colony) as r
    from ecoli_data
) as d
order by d.id 
