-- 동명 동물 수 찾기
-- GROUP BY

SELECT NAME, COUNT(NAME) AS COUNT -- 이름과 해당 이름이 쓰인 횟수
FROM ANIMAL_INS
GROUP BY NAME -- 이름으로 그룹화
HAVING COUNT(NAME) >= 2 -- 해당 이름의 개수가 2개 이상인 것
ORDER BY NAME; -- 이름 순으로 정렬