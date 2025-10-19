
#lower than 8 == null, grade desending, samegrade--marks ascending
#descending grade , name alphabet

select 
    case when g.grade >= 8 then s.name else 'NULL' end,
    g.grade,
    s.marks
from students s
join grades g
on s.marks between g.min_mark and g.max_mark
order by 
    g.grade desc,
    case when g.grade >= 8 then s.name end asc,
    case when g.grade < 8 then s.marks end asc
