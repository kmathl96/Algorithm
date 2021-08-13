-- 우유와 요거트가 담긴 장바구니
-- GROUP BY, DISTINCT

SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME = 'Milk' OR NAME = 'Yogurt' -- 상품이 우유나 요거트인 것
GROUP BY CART_ID -- 장바구니 아이디를 기준으로 그룹화
HAVING COUNT(DISTINCT NAME) >= 2 -- 상품 종류(중복 제거)가 2개 이상 (= 우유와 요거트 둘 다 구입)
ORDER BY CART_ID; -- 장바구니 아이디 순으로 정렬