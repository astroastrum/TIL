## JOIN

* JOIN은 동사로 '가입하다', '참여하다', '참가하다'라는 의미를 가지고 있습니다. 데이터베이스에서는 테이블 하나만 있는게 아니라 여러 개로 분산하여 이를 결합하기도 합니다. 여러 개를 결합해서 효율적으로 데이터를 관리합니다.

* JOIN의 종류
  * INNER JOIN, OUTER JOIN, CROSS JOIN

* INNER JOIN  (내부 조인)

  * 테이블 1과 2가 있을 때 두 테이블의 다이어그램을 합치면 공통된 부분을 볼 수 있습니다. 

  * 공통된 부분이 안쪽(INNER = 내부)에 있기 때문에 INNER JOIN입니다.
  * INNER JOIN문에서 INNER은 생략 가능합니다.

* INNER JOIN 쿼리

  ```PYTHON
  SELECT *
  FROM 테이블1 [INNER] JOIN 테이블2
  	ON 테이블1.칼럼 = 테이블2.칼럼;
  ```

  



* OUTER JOIN 종류 (외부 조인)

  * LEFT, RIGHT, FULL

  * LEFT OUTER JOIN은 좌 테이블을 기준으로, RIGHT OUTER JOIN은 우 테이블을 기준으로 결합합니다.

* OUTER JOIN 쿼리

  ```PYTHON
  SELECT *
  FROM 테이블1 [LEFT|RIGHT|FULL] OUTER JOIN 테이블2
    ON 테이블1.칼럼 = 테이블2.칼럼;
  ```





*  CROSS JOIN (교차 조인)
  * 두 테이블의 모든 경우의 수를 결합하는 형태입니다.