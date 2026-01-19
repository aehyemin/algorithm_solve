#식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수
#%서울%이라고 하면 틀림
select u.REST_ID, u.REST_NAME, U.FOOD_TYPE, u.FAVORITES, u.ADDRESS, round(avg(r.review_score),2) as SCORE
                                                                         
from rest_info as u
join rest_review as r
on u.rest_id = r.rest_id
where u.address like '서울%'
group by u.rest_id
order by SCORE desc, u.FAVORITES desc
