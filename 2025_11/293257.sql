select count(i.ID) as FISH_COUNT, n.FISH_NAME
from fish_info as i
join fish_name_info as n
on i.fish_type = n.fish_type
group by i.fish_type, n.fish_name
order by FISH_COUNT desc
