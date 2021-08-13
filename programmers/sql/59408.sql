-- 중복 제거하기
-- SUM, MAX, MIN

SELECT COUNT(DISTINCT NAME) count -- NULL이 아닌 이름의 개수 + 중복 제거
FROM ANIMAL_INS;