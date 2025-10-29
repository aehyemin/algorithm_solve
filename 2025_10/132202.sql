select mcdp_cd as '진료과코드',
count(*) as '5월예약건수'
from appointment
# where apnt_ymd >= '2022-05-01' and apnt_ymd < '2022-06-01'
where year(apnt_ymd) = 2022
and month(apnt_ymd) = 5
group by mcdp_cd
order by count(*), mcdp_cd


