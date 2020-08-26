# 성적에 관한 함수

# 성적 합계(a는 리스트 또는 튜플 형식으로 받을 것)
def total(a):
    return sum(a)

# 성적 평균(합계를 a 수만큼 나눠준다)
def avg(a):
    return sum(a)/len(a)