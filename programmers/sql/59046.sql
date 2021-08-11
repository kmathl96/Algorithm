-- 루시와 엘라 찾기
-- String, Date

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE -- 아이디와 이름, 성별 및 중성화 여부
FROM ANIMAL_INS
WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty") -- 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물
ORDER BY ANIMAL_ID; -- ID순으로 정렬