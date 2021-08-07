-- 어린 동물 찾기
-- SELECT

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged' -- 젊은 동물 : Aged가 아닌 경우
ORDER BY ANIMAL_ID; -- 아이디 순으로 정렬