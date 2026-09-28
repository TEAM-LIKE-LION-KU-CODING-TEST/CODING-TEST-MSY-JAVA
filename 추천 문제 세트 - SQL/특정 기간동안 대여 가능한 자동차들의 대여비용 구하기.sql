WITH RENTABLE AS (
    SELECT
        CC.CAR_ID,
        CC.CAR_TYPE,
        CC.DAILY_FEE
    -- JOIN CH 구문을 삭제하여 대여 기록이 없는 차량도 포함
    FROM CAR_RENTAL_COMPANY_CAR CC 
    WHERE CC.CAR_TYPE IN ('세단', 'SUV')
        -- 11월에 단 하루라도 대여 기록이 있는 차량을 전체 제외
        AND CC.CAR_ID NOT IN (
              SELECT CAR_ID 
              FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
              WHERE START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01'
        )
)
SELECT
    R.CAR_ID,
    R.CAR_TYPE,
    -- 하드코딩(0.90, 0.92) 대신 테이블의 DISCOUNT_RATE를 받아와 동적 계산
    ROUND(R.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100) AS FEE
FROM RENTABLE R
-- 실제 할인율 정책 테이블을 '30일 이상' 조건으로 조인
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P 
    ON R.CAR_TYPE = P.CAR_TYPE AND P.DURATION_TYPE = '30일 이상'
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC;