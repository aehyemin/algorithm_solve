#2022년 1월, 저자별, 카테고리별 매출액
#저자 id, 저자명, 카테고리, 매출액
#order_id, category desc
#book as b
#author as a
#book_sales as s
#b.author_id = a.author_id
#s.book_id = b.book_id
select a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, sum(b.price * s.sales) as TOTAL_SALES
from book as b
join author as a
on b.author_id = a.author_id
join book_sales as s
on s.book_id = b.book_id
where date_format(s.sales_date, '%Y-%m') = '2022-01'
group by a.author_name, b.category
order by a.author_id, b.category desc
