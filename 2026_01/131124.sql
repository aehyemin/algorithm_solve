#리뷰를 가장 많이 작성한 회원의 리뷰들 조회
#meber_profile as p, rest_review as r
#p.member_name, r.review_text, r.review_date
#1. 리뷰를 가장 많이 작성한 회원을 구함
with rank_one as (
    select count(review_id) as review_cnt, member_id
    from rest_review
    group by member_id 
    order by review_cnt desc
    limit 1 
)
select p.MEMBER_NAME, r.REVIEW_TEXT, date_format(r.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from rank_one as o
join member_profile as p
on o.member_id = p.member_id
join rest_review as r
on r.member_id = o.member_id
order by r.review_date, r.review_text
