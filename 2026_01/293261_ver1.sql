# 물고기 종류별로 가장 큰 물고기
#1. type별로 가장 큰 length인 물고기 구하기
with rank_type as (
    select max(length) as max_one, fish_type
    from fish_info
    group by fish_type
)

select i.ID, f.FISH_NAME, i.LENGTH
from fish_info as i
join rank_type as t
on i.fish_type = t.fish_type
and t.max_one = i.length
join fish_name_info as f
on f.fish_type = i.fish_type
order by i.id
