-- select ID, EMAIL, FIRST_NAME, LAST_NAME
-- from developer_infos
-- where skill_1 = 'Python' or skill_2 = 'Python' or skill_3 = 'Python'
-- order by ID

select ID, EMAIL, FIRST_NAME, LAST_NAME
from developer_infos
where 'Python' in (skill_1, skill_2, skill_3)
order by ID
