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
----- “대상이 되는 자동차를 고르는 집계”와 “최종 출력용 월별 집계”의 grain이 다르다는 점
----- 하나의 GROUP BY로 억지로 해결하려 하지 말고 CTE/서브쿼리로 단계를 나눈다
----- 그룹 판정 후 세부 출력이 나오면 GROUP BY → HAVING → JOIN/CTE
--- 단계별 CTE도 가능
WITH completed_order AS (
    SELECT ...
    FROM ...
    --- 1단계 : 완료 주문만 분리
    WHERE status = 'DONE'
),
user_summary AS (
    SELECT ...
    FROM completed_order
    --- 2단계 : 사용자별 집계
    GROUP BY user_id
)
SELECT ...
FROM user_summary
--- 3단계 : 최종 조건
WHERE total_amount >= 10000;

--- 서브쿼리
WHERE price = (
    --- 전체 테이블에서 최고 가격 1개 계산
    --- ORDER BY ... LIMIT 1과는 다르게 최고가 상품이 여러개면 모두 반환 가능
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

--- 그룹별 최대값 행 찾기
--- 카테고리마나 반드시 한 상품만 골라야 한다면
WITH ranked AS (
    SELECT
        ...
    ROW_NUMBER() OVER (
        PARTITION BY category
        -- 가격이 같은 경우 product_id가 작은 상품을 선택
        ORDER BY price DESC, product_id ASC
    ) AS RN
    FROM product
)
SELECT
    ...
FROM ranked
WHERE RN = 1;

--- INNER JOIN : 양쪽 모두 존재하는 데이터가 필요할 때
FROM ...
JOIN ...
    ON u.id = o.id
--- LEFT JOIN : 왼쪽 데이터는 모두 보존해야 할 때
FROM ...
LEFT JOIN ...
    --- o에 존재하지 않는 사용자에 대한 o.id는 NULL
    ON u.id = o.id
----- LEFT/RIGHT JOIN에서 WHERE로 범위를 지정한다면
----- 주문이 없는 사용자는 NULL이기에 제거됨
WHERE o.order_date >= '2026-01-01'
----- ON을 사용해야함
LEFT JOIN ...
    ON ... = ...
    AND o.order_date >= '2026-01-01'
----- ON : 어떤 행을 연결? / WHERE : 연결 결과 중 어떤 행을 남길 것인가

--- NULL을 일반 값처럼 비교하지 않음 (NOT IN 사용 주의)
----- 부재 여부는 WHERE로 제거하는 것이 더 안전
WHERE NOT EXISTS (
    SELECT 1
    FROM blacklist AS b
    WHERE b.user_id = u.user_id
)

--- JOIN 만으로 주문 금액을 합치면 중복 행 발생 가능
WITH order_summary AS (
    SELECT
        user_id,
        --- 한 명의 사용자당 1행으로 축소 후 본 쿼리에서 사용
        SUM(amount) AS order_amount
        FROM orders
        GROUP BY user_id

),
coupon_summary AS (...)

--- NULL은 = 연산자로 비교하지 않는다, IS 사용
WHERE name IS NULL
----- MySQL에서 NULL 치환
SELECT
    IFNULL(name, 'No name') AS Name

--- CASE : 조건에 따라 서로 다른 값을 반환하는 조건문 역할을 수행하는 표현식
SELECT
    id,
    CASE
        WHEN out_date IS NULL THEN '출고 미정'
        WHEN out_date <= '2026-09-01' THEN '출고 완료'
        ELSE '출고 대기'
    END AS status
    ...
----- 조건부 집계에서 사용 가능
SELECT
    id,
    SUM(
        CASE
            WHEN status = 'DONE' then amount
            ELSE 0
        END
    ) AS done_amount

--- 날짜 함수
SELECT
    YEAR(order_date) AS order_year,   -- 연도
    MONTH(order_date) AS order_month, -- 월
    DAY(order_date) AS order_day,     -- 일
    HOUR(order_date) AS order_hour    -- 시간
FROM orders;
--- 출력 형식 변경
SELECT
    DATE_FORMAT(
        order_date,
        '%Y-%m-%d'
    ) AS order_date
FROM orders;

--- 문자열 함수
----- CONCAT() : 문자열 결합
CONCAT(first_name, ' ', last_name) AS full_name
----- LOWER() : 소문자 변환
----- UPPER() : 대문자 변환
----- SUBSTRING() : 부분 문자열 추출 (시작 위치, 길이)
SELECT SUBSTRING(phone, 1, 3) AS area_code
----- LEFT() : 왼쪽부터 지정한 길이만큼 추출
----- RIGHT() : 오른쪽부터 지정한 길이만큼 추출
----- LENGTH() : 바이트 단위 문자열 길이 계산
----- CHAR_LENGTH() : 글자 수 단위 문자열 길이 계산
----- REPLACE() : 특정 문자열을 다른 문자열로 대체
REPLACE(phone, '-', '') AS clean_phone
----- TRIM() : 문자열 양쪽 공백 제거
----- LOCATE() : 찾을 문자열의 시작 위치 반환 (1부터 시작, 없으면 0)
LOCATE('@', email) AS at_symbol_pos
----- GROUP_CONCAT() : 그룹화된 행의 문자열을 하나로 결합
----- ex. 101번 주문에 속한 3개의 행('사과', '바나나', '우유')이
----- SEPARATOR ' '(공백)으로 구분되어 "사과 바나나 우유"라는 하나의 문자열로 합쳐짐
SELECT GROUP_CONCAT(product_name SEPARATOR ' ') AS item_list
FROM orders
GROUP BY order_id;

--- DISTINCT : 중복 제거, COUNT 내부 등에서도 사용 가능

--- 윈도우 함수 : 행과 행 간의 관계를 정의하여
--- 기존 행의 개수(결과 집합의 Row 수)를 유지하면서 그룹 단위의 연산을 수행
--- 윈도우 함수는 원래 데이터의 모든 행을 그대로 유지하면서 연산 결과를 별도의 컬럼으로 덧붙임
----- ROW_NUMBER(): 중복 없는 연속 순위 (1, 2, 3, 4)
----- RANK(): 동점 공유 + 순위 건너뜀 (1, 2, 2, 4)
----- DENSE_RANK(): 동점 공유 + 순위 이어짐 (1, 2, 2, 3)
with ranked AS (
    SELECT ...
        ROW_NUMBER() OVER (
            --- 부서 내부에서 (PARTITION BY)
            PARTITION BY dept_id
            --- 연봉 순 번호 부여 (ORDER BY salary)
            ORDER BY salary DESC, emp_id ASC
        ) AS RN
    FROM employee
)
----- LAG(): 현재 행 기준 이전 행의 값을 가져옴
----- LEAD(): 현재 행 기준 다음 행의 값을 가져옴
SELECT ...
    --- 같은 사용자의 직전 주문 금액
    LAG(amount) OVER (
        PARTITION BY user_id
        ORDER BY order_date, order_id
    ) AS prev_amount
----- 첫 주문부터 현재 주문까지 누적
SUM(amount) OVER (
    PARTITION BY user_id
    ORDER BY order_date, order_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS running_total

--- UNION : 중복 제거 / UNION ALL : 중복 제거하지 않고 그대로 결합
SELECT
    user_id,
    amount
FROM online_order
UNION ALL
SELECT
    user_id,
    amount
FROM offline_order

--- 비율 계산
SELECT
    --- ROUND(, n) : 소수점 4번째 자리까지 (5번재 자리에서 반올림)
    --- CEIL() : 자리수 올림 지원하지 않음, 10000 곱하고 올리고, 10000 나누는 방식 권장
    --- TRUNCATE(, n) : 소수점 4번째 자리까지 (5번째 자리 버림)
    ROUND(
        --- 비율 계산 시 분모 분자 주의
        COUNT(DISTINCT o.uid) / COUNT(DISTINCT u.uid),
        4
    ) AS purchase_rate

--- 재귀 CTE(Common Table Expression)
WITH RECURSIVE cte_name AS (
    -- [STEP 1] 앵커 멤버 최초 1회 실행
    -- 조건에 맞는 초기 데이터 세트를 구해 작업 공간(Working Table) 및 최종 결과에 저장
    SELECT id, parent_id, 1 AS depth
    FROM table
    WHERE condition

    UNION ALL

    -- [STEP 2] 재귀 멤버 반복 실행 (Working Table이 비어있지 않을 때까지)
    -- 직전 단계 결과(c)와 원본 테이블(t)을 JOIN하여 다음 계층(자식) 조회
    -- 조회된 신규 결과는 다음 회차의 Working Table이 되고, 최종 결과에도 누적(UNION ALL)
    SELECT t.id, t.parent_id, c.depth + 1
    FROM table AS t
    JOIN cte_name AS c ON t.parent_id = c.id
)
-- [STEP 3] 루프 종료 후 최종 반환
-- [STEP 2]의 결과가 0건(Empty)이 되어 재귀가 멈추면, 지금까지 누적된 전체 결과를 반환
SELECT * FROM cte_name;

--- 0건인 구간도 출력해야 하는 문제
----- 0부터 23시까지의 기준 집합을 가진 CTE
WITH RECURSIVE hours AS (
    SELECT
        0 AS hour
    
    UNION ALL

    SELECT
        hour + 1
    FROM hours
    WHERE HOUR < 23
),
hour_count AS (
    SELECT
        HOUR(event_time) AS HOUR,
        COUNT(*) AS cnt
    FROM event
    GROUP BY HOUR(event_time)
)
SELECT
    h.hour,
    --- IFNULL은 MySQL 전용, COALESCE
    --- COALESCE(휴대전화, 집전화, '번호없음') : 나열된 인자 중 NULL이 아닌 첫 번째 값을 반환
    COALESCE(c.cnt, 0) AS cnt
FROM hours AS h
LEFT JOIN hour_cont AS c
    ON c.hour = h.hour
ORDER BY h.hour