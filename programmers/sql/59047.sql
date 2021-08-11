-- 이름에 el이 들어가는 동물 찾기
-- String, Date

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
-- 1. 개
-- 2. 이름에 'el'이 들어감 => LIKE와 %를 활용
WHERE ANIMAL_TYPE = "Dog" AND NAME LIKE "%el%"
ORDER BY NAME; -- 이름을 기준으로 정렬