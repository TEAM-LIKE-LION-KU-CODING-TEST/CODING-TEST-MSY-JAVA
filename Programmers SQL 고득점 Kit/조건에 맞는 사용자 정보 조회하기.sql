SELECT 
    U.USER_ID,
    U.NICKNAME,
    -- 시, 도로명 주소, 상세 주소를 공백으로 연결하여 "전체주소"로 출력
    CONCAT_WS(' ', U.CITY, U.STREET_ADDRESS1, U.STREET_ADDRESS2) AS "전체주소",
    -- 전화번호를 3자리-4자리-4자리 형태로 하이픈을 넣어 "전화번호"로 출력
    CONCAT(SUBSTR(U.TLNO, 1, 3), '-', SUBSTR(U.TLNO, 4, 4), '-', SUBSTR(U.TLNO, 8, 4)) AS "전화번호"
FROM 
    USED_GOODS_USER U
JOIN 
    USED_GOODS_BOARD B ON U.USER_ID = B.WRITER_ID
GROUP BY 
    -- GROUP BY절을 사용할 때 SELECT절에 포함된 모든 비집계 컬럼
    -- (집계 함수에 감싸이지 않은 일반 컬럼)을 GROUP BY 목록에 명시해야 함
    U.USER_ID, U.NICKNAME, U.CITY, U.STREET_ADDRESS1, U.STREET_ADDRESS2, U.TLNO
HAVING 
    COUNT(B.BOARD_ID) >= 3
ORDER BY 
    U.USER_ID DESC;