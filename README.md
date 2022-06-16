# django_drf

1. args, kwargs를 사용하는 예제 코드 짜보기

![스크린샷 2022-06-15 오후 5 06 38](https://user-images.githubusercontent.com/55477835/173776002-f05e88cb-55ff-45d8-8487-205d040fba28.png)

 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기

- mutable
```python
name = 'joo'
tmp_name = name

tmp_name += 'joo'

```
mutable은 tmp_name에 메모리 주소를 주는 것이 아니라 값을 넘겨준다.
따라서 위 코드에서 변수들을 프린트 해보면 name은 joo로 나오고 tmp_name은 joojoo로 실행될 것이다.
mutable은 bool,int,float,tuple,str 등 기본 변수와 tuple로 이루어져 있다.
- immutable
```python
names = ['joo' , 'jin', 'won']

tmp_names = names

tmp_names.append('woo')

```
immutable은 위와 같이 다른 변수에 할당하면 메모리 주소를 넘겨준다. 그러므로 위와 같이 어펜드를 했을 때
메모리 주소에 직접 값을 넣기 때문에 names도 tmp_names도 프린트를 하면 ['woo']가 추가되어 나오는 것을 확인할 수 있다.
immutable은 list, set, dict 등 자료구조형들이 이에 속하는 것으로 보인다.
만약 immutable을 mutable처럼 값만 전달하고 싶다면 tmp_names = copy.deepcopy(names)를 사용하면 된다.

3. DB FIELD에서 사용되는 Key 종류와 특징 서술하기

- pk : primary key의 약자로 테이블의 필드값이 가지는 고유값이라고 할 수 있다. pk는 필드값을 대표하므로 두개 이상 존재할 수 없다. fk를 사용하여 다른 테이블을 참조하면 이 pk값을 통해 조회한다.
- fk : foreign key의 약자로 연관이 있는 다른테이블을 참조할 때 사용하는 값이다. fk는 다른 테이블의 pk값이다.
- uk : unique key의 약자이다. pk와 비슷해보이지만 반드시 존재해야하는 값은 아니며 고유하다는 특징만 공유한다.

4. django에서 queryset와 object는 어떻게 다른지 서술하기

QuerySet이란 object의 리스트 형태이다. 모델.objects.all() 이나 모델.objects.filter()를 통해 전달받을 수 있는 형태로 생성한 db의 row값들이 담겨 있다.
이 QuerySet을 for문으로 조회하여 각 object들을 얻을 수 있으며 .name .user_id 이런식으로 담겨있는 칼럼 값을 조회할 수도 있고 각 값들을 이용해서 프론트에 필요한 정보를 보내줄 수 있다.
