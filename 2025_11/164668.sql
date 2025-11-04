select USER_ID, NICKNAME, sum(b.price) as TOTAL_SALES
from used_goods_board as b
join used_goods_user as u
on b.writer_id = u.user_id
where b.status = 'DONE' 
group by writer_id
having TOTAL_SALES >= 700000
order by sum(b.price)
