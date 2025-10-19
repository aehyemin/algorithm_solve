SELECT co.continent, floor(avg(c.population))
from city c
join country co
on c.countrycode = co.code
group by continent
