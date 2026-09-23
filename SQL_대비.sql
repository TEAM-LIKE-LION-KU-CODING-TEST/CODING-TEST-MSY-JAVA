-- [시작, 다음 경계)
WHERE created_at >= '2026-09-01'
    AND created_at < '2026-10-01'

-- WHERE은 GROUP BY 집계 전 행을 줄이고
-- HAVING은 GROUP BY 집계 후 만들어진 그룹의 집계 결과를 제거

-- 그룹화 전에 NULL인 name의 행을 제거
-- WHERE 단계에는 아직 그룹별 COUNT(*)이 존재하지 않는다
WHERE name IS NOT NULL

--- datetime 형식에서 시각만 추출
--- WHERE과 GROUP BY에서도 사용할 수 있음
HOUR(datetime)
WHERE HOUR(datetime) BETWEEN 9 AND 19

--- WITH : 복잡한 서브쿼리를 별도의 가상 임시 테이블처럼 이름을 붙여 정의한 뒤
WITH cte_name AS (
    SELECT c1, c2
    FROM table_name
    WHERE condition = 1
)
--- 메인 쿼리에서 가져다 쓸 수 있게 해준다
SELECT *
FROM cte_name;
--- “대상이 되는 자동차를 고르는 집계”와 “최종 출력용 월별 집계”의 grain이 다르다는 점
--- 하나의 GROUP BY로 억지로 해결하려 하지 말고 CTE/서브쿼리로 단계를 나눈다
--- 그룹 판정 후 세부 출력이 나오면 GROUP BY → HAVING → JOIN/CTE

--- 서브쿼리
WHERE price = (
    --- 전체 테이블에서 최고 가격 1개 계산
    SELECT MAX(price)
    FROM food_product
)
--- 존재/부재 여부
WHERE (NOT) EXISTS (
    SELECT 1
    FROM child.c1
    WHERE c.parent_id = p.id
)
--- 상관 서브쿼리 : 서브쿼리가 메인 쿼리의 컬럼 값을 참조하여 실행되는 서브쿼리
SELECT
    ...
FROM food_product AS f
WHERE f.category IN ('과자', '국', '김치', '식용유')
    AND f.price = (
        SELECT MAX(f2.price)
        FROM food_product AS f2
        WHERE f2.category = f.category
    )