## CASE

* Case문은 어떠한 상황에서 데이터를 조작해서 사용할 수 있습니다.

```python
-- CASE문 구조 예시
-- country가 1인 경우는 미국을 country가 1인 경우에는 프랑스를 출력하시오.
SELECT 
    id,
    CASE
        WHEN country = 1 THEN '미국'
        WHEN country = 2 THEN '프랑스'
    END AS 국가명
FROM tableexample
LIMIT 2;

-- id   국가명
-- --   -----
-- 1    미국
-- 2    프랑스

```



## SUBQUERY

* 메인 쿼리에서 어떠한 값을 대체해서 사용하는 것을 서브 쿼리라고 합니다.