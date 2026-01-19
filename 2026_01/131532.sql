#년,월,성별 별로 상품을 구매한 회원수 집계 | 성별 없으면 제외
select year(s.sales_date) AS YEAR, month(s.sales_date) as MONTH, i.GENDER, count(distinct i.user_id) as USERS
from user_info as i
join online_sale as s
on i.user_id = s.user_id
where i.gender is not null
group by  YEAR, MONTH, i.gender
order by YEAR, MONTH, i.GENDER
