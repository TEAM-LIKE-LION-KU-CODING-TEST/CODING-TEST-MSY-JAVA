SELECT user_id, name, mail
FROM Users
-- 기본적으로 대소문자를 구분하지 않음
-- Character set 'utf8mb3_general_ci' cannot be used in conjunction with 'binary' in call to regexp_like.
-- REGEXP_LIKE 함수의 세 번째 인자로 'c'(Case-sensitive) 옵션 전달
WHERE REGEXP_LIKE(mail, '^[A-Za-z]+[A-Za-z0-9_.-]+@leetcode[.]{1}com$|^[A-Za-z]+@leetcode[.]{1}com$', 'c');