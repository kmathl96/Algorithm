-- 헤비 유저가 소유한 장소

SELECT *
FROM PLACES
WHERE HOST_ID IN -- 유저가 헤비 유저인 경우
	-- 헤비 유저들의 아이디 구하기
    (SELECT HOST_ID
     FROM PLACES
     GROUP BY HOST_ID -- 유저의 아이디로 그룹화
     HAVING COUNT(ID) >= 2) -- 등록한 공간이 두 개 이상
ORDER BY ID; -- 아이디 순으로 정렬