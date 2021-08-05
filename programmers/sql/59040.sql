-- 고양이와 개는 몇 마리 있을까
-- GROUP BY

SELECT ANIMAL_TYPE, count(*) -- 생물 종과 해당 종의 데이터의 개수
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE -- 생물 종으로 그룹화
ORDER BY ANIMAL_TYPE; -- 생물 종을 기준으로 정렬