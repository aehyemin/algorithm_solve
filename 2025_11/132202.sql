select CATEGORY, sum(s.sales) as TOTAL_SALES
from book_sales as s
join book as b
on b.book_id = s.book_id
where month(sales_date) = 1

group by category
order by category
