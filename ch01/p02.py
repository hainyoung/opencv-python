# class 생성
# class : 새로운 자료형
# 우리가 알고 있는 자료형 : int, float 등 기본 자료형들
# 기본 자료형이 아닌 사용자가 새로운 자료형을 정의해서 사용할 수 있다
# 그것을 class 자료형이라고 보면 된다, 사용자 정의 자료형

class Person:
    # class 안에는 함수를 정의하고 __init__(self) 생성
    # class 의 첫 글자는 대문자로 하는 게 암묵적인 룰
    def __init__(self, name, age):
        # class 안에 있는 속성들을 초기화 할 때 사용함, '초기자' 라고 한다
        # class 안의 속성들이 처음부터 어떤 특정 값을 갖겠다, 초기값을 갖겠다, 초기화 시켜주는 역할이
        # init 이다
        # self 란, class 자기 자신을 뜻한다
        # 자기 자신의 객체인 name 의 속성을 '홍길동' 이라 하겠다, age 의 속성을 25로 하겠다
        self.name = name
        self.age = age
        # 오른쪽의 name 과 age == 위의 name, age -> 즉, 함수를 전달하는 매개변수
        # self. 뒤의 name 과 age 는 class 내부에서 사용하는 class 안의 인스턴스 변수이다


# 새로 만든 자료형을 사용해보자
# Person()
# class 이름을 그대로 적고 함수를 쓰는 것처럼 ()를 붙여준다
# 출력되는 것은 없음, 메모리상에 해당 class 가 올라가있기만 한 상태
# 무언가 출력이 되게 하려면 저 클래스를 변수로 선언해주고 사용하면 된다

# p = Person()
# print(p.name)
# print(p.age)

# 홍길동
# 25

# 여러 사람을 만들고 싶다면?
# p1, p2 이런 식으로

# p1 = Person()
# p2 = Person()
#
# print(p1.name)
# print(p1.age)
# print(p2.name)
# print(p2.age)

# 똑같이 홍길동 25만 출력된다
# 의도한 방향과 다르다
# 어떻게 해결할 수 있을까?
# class 뒤에 매개변수 같이 적어주고
# 이를 전달받기 위해서는 처음 생성한 class 뒤에
# 받을 매개변수 자리를 만들어준다, self 를 남겨두고

p1 = Person('홍길동', 25)
p2 = Person('하이디', 28)

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
