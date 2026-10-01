SELECT user_id, email
FROM Users
-- "+"로 여러 조건 이어붙이기
-- [.]으로 "."가 지닌 딱 하나의 문자라는 특수 문자 조건 해제
-- ^으로 시작, $로 종료 위치 명시
-- +는 String 합치기가 아니라 1회 이상 반복
WHERE email REGEXP '^[A-Za-z0-9_]+@[A-Za-z]+[.]com$'
ORDER BY user_id ASC;