select 
YEAR(YM) AS YEAR,
ROUND(AVG(PM_VAL1), 2) AS PM10,
ROUND(AVG(PM_VAL2), 2) AS "PM2.5"
from air_pollution
where location2 = '수원'
GROUP BY 1
ORDER BY 1
-- YEAR 는 숫자로 처리, DATE_FORMAT은 문자로 처리
