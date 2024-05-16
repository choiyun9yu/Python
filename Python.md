# Python

### Dictionary 자료 구조에서 .get() 메서드 vs 대괄호 표기법 
- Dictaionary 자료 구조에서 key 값으로 조회하는 방법은 크게 2가지가 있다.
####
  # 방법1. .get() 메서드 사용
  dict.get(key)

  # 방법2. 대괄호 표기법 
  dict.['key']

- Key 값이 없을 때
  - 방법1: 해당하는 key가 없을 경우 None 반환
  - 방법2: 해당하는 key가 없을 경우 KeyError 반환 
- 기본 값 설정
  - 방법1 에서 dict.get(key, default_value)로 조회하는 경우
    key 값이 없으면 default_value 로 반환
- 읽기 전용 속성
  - 방법1: 해당 딕셔너리를 읽기 전용으로 조회하여 수정 불가
  - 방법2: 해당 key 값에 새로운 값을 할당하여 딕셔너리 수정 가능
