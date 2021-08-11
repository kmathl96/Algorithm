-- 중성화 여부 파악하기
-- String, Date

SELECT
	ANIMAL_ID, NAME,
    -- 중성화 여부 파악
    -- SEX_UPON_INTAKE 컬럼에 'Neutered', 'Spayed'가 들어있으면 'O'
    CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
    ELSE 'X' -- 아니면 'X'
    END AS '중성화' -- 컬럼 이름은 '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID; -- 아이디 순으로 정렬