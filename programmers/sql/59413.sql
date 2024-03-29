-- 입양 시각 구하기(2)
-- GROUP BY

-- HOUR(값: 0~23)를 컬럼으로 갖는 TIME 테이블 만들기
WITH RECURSIVE TIME AS(
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR+1 FROM TIME WHERE HOUR < 23)

SELECT T.HOUR AS HOUR, COUNT(ANIMAL_ID) AS COUNT -- 시간대별 입양 건수
FROM ANIMAL_OUTS O RIGHT JOIN TIME T -- TIME의 모든 시간대를 확인
ON DATE_FORMAT(O.DATETIME, '%H') = HOUR
GROUP BY HOUR -- 시간대로 그룹화
ORDER BY HOUR; -- 시간대 순으로 정렬