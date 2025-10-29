select car_type, count(*)
from car_rental_company_car
# where options regexp '통풍시트|열선시트|가죽시트'
where options like '%가죽시트%' or options like '%통풍시트%' or options like '%열선시트%'
group by car_type
order by car_type
