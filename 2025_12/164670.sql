select u.USER_ID, u.NICKNAME, concat(u.city,' ', u.street_address1,' ', u.street_address2) as '전체주소',
concat(substr(u.tlno,1,3), '-', substr(u.tlno,4,4), '-', substr(u.tlno,8,4)) as '전화번호'
from used_goods_board as b
join used_goods_user as u
on b.writer_id = u.USER_ID
group by u.user_id
having count(b.writer_id) >= 3
order by b.writer_id desc
