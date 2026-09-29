SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
--  부분 일치 조건을 방지하기 위해 시작을 ^로 끝을 $로 명시
WHERE NAME REGEXP '^(Lucy|Ella|Pickle|Rogan|Sabrina|Mitty)$'
ORDER BY ANIMAL_ID ASC;