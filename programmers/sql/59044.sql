-- 오랜 기간 보호한 동물(1)
-- JOIN

SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I LEFT JOIN ANIMAL_OUTS O -- 들어온 정보는 있고 보낸 정보는 없어야 함
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL -- 입양을 가지 않은 동물
ORDER BY I.DATETIME -- 보호 시작일 순으로 조회
LIMIT 3; -- 3마리