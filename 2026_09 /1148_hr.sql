# Write your MySQL query statement below
# 자신의 글을 한번 이상 조회한 저자
select distinct author_id as id
from Views
where author_id = viewer_id
order by author_id
