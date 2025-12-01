select max(sum(score)) as SCORE, em.EMP_NO, em.EMP_NAME, em.POSITION, em.EMAIL
from HR_GRADE as gr
join hr_employees as em
on gr.EMP_NO = em.EMP_NO
group by em.emp_no
order by SCORE desc
limit 1

# select *
# from (
#     select sum(gr.score) as SCORE, em.EMP_NO, em.EMP_NAME, em.POSITION,	em.EMAIL
#     from HR_GRADE as gr
#     join hr_employees as em
#     on gr.EMP_NO = em.EMP_NO
#     group by em.emp_no
#     order by SCORE desc
#     limit 1
# ) as t
# select *
# from (
#     select sum(gr.score) as SCORE, em.EMP_NO, em.EMP_NAME, em.POSITION,	em.EMAIL
#     from HR_GRADE as gr
#     join hr_employees as em
#     on gr.EMP_NO = em.EMP_NO
#     group by em.emp_no
# ) as t
# order by SCORE desc
# limit 1
