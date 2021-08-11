-- 없어진 기록 찾기
-- JOIN

SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I RIGHT JOIN ANIMAL_OUTS O -- ANIMAL_OUTS에는 기록이 있어야 하므로 RIGHT JOIN
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL -- ANIMAL_INS에 기록이 없는 동물
ORDER BY O.ANIMAL_ID; -- ID순으로 정렬