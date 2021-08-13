-- 입양 시각 구하기(1)
-- GROUP BY

SELECT DATE_FORMAT(DATETIME, '%H') AS HOUR, COUNT(*) AS COUNT -- 시간대와 그 건수
FROM ANIMAL_OUTS
GROUP BY HOUR -- 시간대로 그룹화
HAVING HOUR BETWEEN 9 AND 19 -- 입양 시각이 9:00 ~ 19:59 사이인 경우
ORDER BY HOUR; -- 시간대 순으로 정렬