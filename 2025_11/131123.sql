-- 단순점수 출력 --> 서브쿼리 필요x
-- 최고 점수의 '이름'--> 서브쿼리 필요함
select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from rest_info
where (food_type, favorites) in (
    select food_type, max(favorites)
    from rest_info
    group by food_type
)
order by food_type desc
