-- NULL 처리하기
-- IS NULL

-- 1. IFNULL를 활용한 방법
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE -- NAME이 NULL이면 'No name'으로 표시
FROM ANIMAL_INS
ORDER BY ANIMAL_ID; -- ID 순으로 정렬

-- 2. CASE와 IS NULL을 활용한 방법
SELECT
	ANIMAL_TYPE,
	CASE WHEN NAME IS NULL THEN 'No name' -- 이름이 NULL이면 'No name'
    ELSE NAME -- 아니면 자신의 이름
    END AS NAME,
    SEX_UPON_INTAKE
FROM ANIMAL_INS;