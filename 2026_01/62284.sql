#MILK YOGURT 동시에 구입한 장바구니
#count(name = 'milk') 같은 경우 네임이 밀크인 개수를 세는 것이아닌, count(식) 이 널값이 아닌 모든 행의 개수를셈
SELECT CART_ID
FROM CART_PRODUCTS
WHERE name in ('Milk', 'Yogurt')
group by cart_id
having count(distinct name) = 2
order by cart_id

