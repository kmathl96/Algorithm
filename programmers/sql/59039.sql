-- 이름이 없는 동물의 아이디
-- IS NULL

SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL -- 이름이 없는 동물
ORDER BY ANIMAl_ID; -- ID 오름차순 정렬