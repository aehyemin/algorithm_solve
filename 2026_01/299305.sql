#붙여야됨

select a.ID, coalesce(count(b.parent_id), 0) as CHILD_COUNT
from ecoli_data as a
left join ecoli_data as b
on a.id = b.parent_id
group by a.id
