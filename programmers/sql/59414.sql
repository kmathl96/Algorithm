-- DATETIME에서 DATE로 형 변환
-- String, Date

-- 날짜를 (년-월-일)로 보여주기 (ex. 2021-08-12)
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID; -- 아이디 순으로 정렬