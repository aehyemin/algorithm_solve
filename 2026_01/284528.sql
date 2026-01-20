#부서정보 hr_department as d
#사원정보 hr_employees as e
#사원평가정보 hr_grade as g
#사원별 성과금. 사번 e.emp_no, 성명e.emp_name, 평가등급grade, 성과금bonus
#1.번호, 이름, 등급 | 으로 정리
#2. 연봉테이블과 join
#3. 보너스 계산
select e.EMP_NO, e.EMP_NAME, grade_rank.grade as GRADE, 
    case 
        when GRADE = 'S' then e.sal*0.2
        when GRADE = 'A' then e.sal*0.15
        when GRADE = 'B' then e.sal*0.1
        else 0
    end as BONUS
from hr_employees as e

join (
select 
    emp_no,
    case 
        when avg(score) >= 96 then 'S'
        when avg(score) >= 90 then 'A'
        when avg(score) >= 80 then 'B'
        else 'C'
    end as GRADE
from hr_grade 
group by emp_no
) as grade_rank

on grade_rank.emp_no = e.emp_no
order by e.EMP_NO
