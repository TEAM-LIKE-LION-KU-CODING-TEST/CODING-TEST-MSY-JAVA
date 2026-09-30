SELECT product_id, product_name, description
FROM products
-- [0-9]{4} : 숫자를 4번만 반복
-- ([^0-9]|$) : |은 OR 조건, [^0-9]는 숫자 제외 OR $는 그냥 종료
WHERE description REGEXP 'SN[0-9]{4}-[0-9]{4}([^0-9]|$)'
ORDER BY product_id ASC;