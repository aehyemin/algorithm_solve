# 전날에 비해 온도가 상승한 날짜
select today.ID
from weather as today
JOIN weather as yesterday
on today.recordDate = date_add(yesterday.recordDate, interval 1 day)
where today.temperature > yesterday.temperature 

#datediff(one_day, two_day)
#date_add(one_day, interval 1 day)
#date_sub(one_day, interval 1 day)
#year()
#month()
#day()
