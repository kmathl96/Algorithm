-- 오랜 기간 보호한 동물(2)
-- String, Date

SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O JOIN ANIMAL_INS I
ON O.ANIMAL_ID = I.ANIMAL_ID
ORDER BY O.DATETIME-I.DATETIME DESC
LIMIT 2;