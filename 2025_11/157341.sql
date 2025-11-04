select distinct r.CAR_ID 
from car_rental_company_rental_history as r
join car_rental_company_car as c
on c.car_id = r.car_id
where car_type = '세단' and start_date >= '2022-10-01'
order by r.car_id desc
